#Projet de Majeur Image : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier classGrille : 
    #Defintion de la classe Grille

#Constructeur : créer une matrice vide de taille nn
                #detcetion des cartes à partir du screen, puis création des objets cartes
                #Attribution des couleurs aux cartes (fonction à part)

#Atribution des couleurs : Par défauts toutes les cartes sont neutres
                        #Dans l'ordre genere aleatoirement rouge, bleu, puis assassin
                        #Attention : Vérif mot sans couleur

#MAJ Grille : A partir screen + couleur carte = verifie localement la couleur du centre de la carte (recouverte ou non)
            #MAJ attribut des cartes (recouverte ou non)
            #Check error

from ctypes import sizeof
import numpy as np
import math
import cv2
import random
import easyocr
from classCarte import Carte

def getMask(image,color): #get the color mask of the screen
    image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

    if color=='red':
        mask1 = cv2.inRange(image, (0, 75, 50), (25, 255, 255)) 
        mask2 = cv2.inRange(image, (155, 75, 50), (180, 255, 255))

        imask = mask1>0
        imask += mask2>0
        

    elif color=='blue':
        mask = cv2.inRange(image, (70, 65, 25), (140, 255, 255)) 
        
        imask = mask>0
        

    elif color=='purple':
        mask = cv2.inRange(image, (120, 15, 15), (170, 255, 225)) 

        imask = mask>0
        

    elif color=='green':
        mask = cv2.inRange(image, (20, 5, 80), (90, 80, 245)) 
        
        imask = mask>0
        

    maskFin = np.zeros_like(image, np.uint8)
    maskFin[imask] = image[imask]

    return maskFin

def detectColor(centre,mask):
    xside=30
    yside=40
    coord=[[centre[0]-xside,centre[1]],[centre[0]-xside,centre[1]-yside],[centre[0]+xside,centre[1]-yside],[centre[0]+xside,centre[1]]]
    pixcol=0
    for x in range (coord[0][0],coord[2][0]):
        for y in range (coord[1][1],coord[0][1]):
            if mask[y,x].all()!=np.zeros((3,1)).all():
                pixcol +=1
    pourcent=pixcol/(xside*2*yside)
    return pourcent

class Grille () : 
    ################################################
    #Initialisation
    def __init__(self, n, screen) :
        self.__grille = []
        self.__Accord = 0

        #Creation des cartes        
        matCarte = self.fDetecCarte(screen, n)
        if matCarte==0:
            self.__Accord=0
        else :
            verif=int(input("Fin de la détection de grille, les mots sont-ils corrects? 0=Non 1=Oui"))
            if verif==0:
                self.__Accord=0
            if verif!=0:
                self.__Accord=1

        if self.__Accord==0:
            return

        for ID in range (n*n) : 
            self.__grille.append(Carte(ID, [[math.ceil(matCarte[ID][0][0][0]),math.ceil(matCarte[ID][0][0][1])],[math.ceil(matCarte[ID][0][1][0]),math.ceil(matCarte[ID][0][1][1])],[math.ceil(matCarte[ID][0][2][0]),math.ceil(matCarte[ID][0][2][1])],[math.ceil(matCarte[ID][0][3][0]),math.ceil(matCarte[ID][0][3][1])]], matCarte[ID][1].upper()))

        #Attribution des couleurs
        self.fSetColors(n)

    ################################################
    #Getter
    def GetGrille(self,) : 
        return self.__grille
    
    def GetAccord(self,) :
        return self.__Accord

    ################################################
    #Setter
    def SetAccord(self,Accord) : 
        self.__Accord=Accord

    ################################################
    #Methodes

    #Fonction de detection des cartes : lis les mots sur les cartes et renvoie une matrice contenant 
        #Les coordonées du rectangle autour du mot, le mot trouvé, la probabilité que le resultat soit juste
    def fDetecCarte(self, screen,n) : 
        matCarte = []

        message=1
        while True:
            if message==1:
                print("Press Q to continue")
                message=0
            cv2.imshow('plateau',screen)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                message=1
                break
        
       

        reader = easyocr.Reader(['fr']) # this needs to run only once to load the model into memory
        #screen=cv2.cvtColor(screen,cv2.COLOR_RGB2GRAY)

        screen=cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        matCarte = reader.readtext(screen)

        indiceSuppr=[] #Liste d'indice des mot à supprimer
        for resul in matCarte:
            if resul[2]<=0.1: #retire le mot si proba<0.1
                indiceSuppr.append(matCarte.index(resul))
            elif len(resul[1])<=2: #retire le mot si 2 lettres ou moins
                indiceSuppr.append(matCarte.index(resul))
            else: #retire le mot si présence d'un caractère bizarre
                sup=0
                for lettre in resul[1]:
                    l=ord(lettre) #conversion de la lettre en code Ascii
                    if ((l in range(33,64)) or (l in range(91,96)) or (l in range(123,126))): #liste des caractères étranges
                        sup=1
                if sup==1:
                    indiceSuppr.append(matCarte.index(resul))

        for i in sorted(indiceSuppr, reverse=True): #suppression des mots de la liste d'indice
            del(matCarte[i])



        #test du nombre de mot 
        if len(matCarte)<(n*n): #Si pas assez de mot, message d'erreur (et renvoit code erreur?) 
            print(len(matCarte))
            print("Erreur, tous les mot n'ont pas été détecté. Vérifiez qu'il y ai bien un carré de",n,"*",n,"sur la grille.")
            return(0)
        elif len(matCarte)>n*n: #Si trop de mot, supprime les mots les plus improbables
            while len(matCarte)!=n*n:
                probmin=1
                for resul in matCarte:
                    if resul[2]<probmin:
                        probmin=resul[2]
                        motfaible=resul
                matCarte.pop(matCarte.index(motfaible))
        """
        

        
        
        matCarte = [ ([[28, 81], [99, 81], [99, 95], [28, 95]], 'RESTAURANT', 0.3543044810415938), 
                     ([[180, 86], [206, 86], [206, 94], [180, 94]], 'CHEF', 0.10739509761333466), 
                     ([[301, 85], [331, 85], [331, 97], [301, 97]], 'VERT', 0.571911096572876), 
                     ([[413, 81], [471, 81], [471, 93], [413, 93]], 'SORCIERE', 0.9196322129966619), 
                     ([[547, 81], [589, 81], [589, 93], [547, 93]], 'SORTIE', 0.9055120984439944), 
                     ([[51, 165], [75, 165], [75, 179], [51, 179]], 'COL', 0.9923612595314808), 
                     ([[167, 171], [213, 171], [213, 185], [167, 185]], 'CANARD', 0.35200526778006613), 
                     ([[297, 171], [331, 171], [331, 183], [297, 183]], 'MARS', 0.42295193672180176), 
                     ([[431, 173], [453, 173], [453, 187], [431, 187]], 'CLÉ', 0.6550630934645527), 
                     ([[549, 171], [595, 171], [595, 183], [549, 183]], 'MAJEUR', 0.5234042927810376), 
                     ([[41, 257], [75, 257], [75, 271], [41, 271]], 'MODE', 0.9980067610740662), 
                     ([[161, 261], [215, 261], [215, 275], [161, 275]], 'JOURNAL', 0.9976108833635754), 
                     ([[293, 257], [343, 257], [343, 271], [293, 271]], 'VOITURE', 0.9955675990735964), 
                     ([[427, 257], [467, 257], [467, 269], [427, 269]], 'HEROS', 0.8950141461416548), 
                     ([[553, 255], [599, 255], [599, 269], [553, 269]], 'LOUCHE', 0.9548048855023848), 
                     ([[35, 353], [75, 353], [75, 367], [35, 367]], 'REGLE', 0.15960075392331474), 
                     ([[171, 351], [215, 351], [215, 365], [171, 365]], 'SOLDAT', 0.656859524822165), 
                     ([[299, 355], [337, 355], [337, 369], [299, 369]], 'ALPES', 0.9946365503141505), 
                     ([[427, 349], [475, 349], [475, 363], [427, 363]], 'CELLULE', 0.8809420902083333), 
                     ([[567, 349], [593, 349], [593, 361], [567, 361]], 'ARC', 0.5181232227533413), 
                     ([[31, 451], [75, 451], [75, 465], [31, 465]], 'CANON', 0.9889419254176187), 
                     ([[161, 449], [209, 449], [209, 463], [161, 463]], 'ÉPONGE', 0.9983187244315853), 
                     ([[299, 447], [339, 447], [339, 461], [299, 461]], 'DANSE', 0.9961014605773721), 
                     ([[421, 445], [479, 445], [479, 461], [421, 461]], 'FANTOME', 0.46388805167658925), 
                     ([[559, 447], [605, 447], [605, 461], [559, 461]], 'ESPION', 0.9934963953204257)    ] 
        """

                ######Test mot, à supprimer après######
        moyenne=0
        probmin=1
        min=0
        for i in matCarte:
            print(i,"\n")
            moyenne=moyenne+i[2]
            if i[2]<probmin:
                probmin=i[2]
                min=i

        moyenne=moyenne/len(matCarte)
        print("Moyenne:",moyenne)
        print("Min:",min,"\n")
        ######Test mot, à supprimer après######

        return matCarte

    #Methode permettant de definir les couleurs des cartes pour les maîtres espions en début de partie
    def fSetColors(self, n) : 
        CartesID = [ID for ID in range (n*n)]
        random.shuffle(CartesID)

        N = math.floor((n*n)/3)
        color = ['r', 'b'] ; random.shuffle(color)
        
        for ID in CartesID[0:N+1] : 
            self.__grille[ID].SetColor(color[0])
        for ID in CartesID[N+1:2*N+1] : 
            self.__grille[ID].SetColor(color[1])
        self.__grille[CartesID[2*N+1]].SetColor('a')

    #Methode permettant de mettre a jour le parametre find des cartes en fonction de l'avancement dans le partie
    def MAJ_Grille(self, screen) : #TODO : A tester

        for color in ['red','blue','green','purple']:

            mask=getMask(screen,color)

            for carte in self.GetGrille() : 
                #TODO : Defintion couleur au centre, pictColor
                x0 = [math.ceil(carte.GetCoord()[0][0]),math.ceil(carte.GetCoord()[0][1])]
                x1 = [math.ceil(carte.GetCoord()[1][0]),math.ceil(carte.GetCoord()[1][1])]
                x2 = [math.ceil(carte.GetCoord()[2][0]),math.ceil(carte.GetCoord()[2][1])]
                x3 = [math.ceil(carte.GetCoord()[3][0]),math.ceil(carte.GetCoord()[3][1])]
                centre=[math.ceil((x0[0]+x2[0])/2),math.ceil((x0[1]+x2[1])/2)]

                pctCol=detectColor(centre,mask)  #r:50%, #bleu:30%, #green:22% #violet:X%
                
                if color=='red':
                    carte.SetpctColor(0, pctCol)

                elif color=='blue':
                    carte.SetpctColor(1, pctCol)

                elif color=='green':
                    carte.SetpctColor(2, pctCol)

                elif color=='purple':
                    carte.SetpctColor(3, pctCol)

        seuilColor=[0.5,0.3,0.25,0.5] #Pourcentage de détection pour chaque couleur

        for carte in self.GetGrille():
            nbCol=0

            if carte.GetpctColor()[0]>=seuilColor[0]:
                pictColor= 'r'
                nbCol=nbCol + 1
            
            if carte.GetpctColor()[1]>=seuilColor[1]:
                pictColor= 'b'
                nbCol=nbCol + 1

            if carte.GetpctColor()[2]>=seuilColor[2]:
                pictColor= 'n'
                nbCol=nbCol +1
            
            if carte.GetpctColor()[3]>=seuilColor[3]:   #A modifier quand on aura testé l'assassin
                pictColor= 'a'
                nbCol=nbCol +1

            if nbCol==0:
                pictColor='no'
            
            elif nbCol >1:
                print('Erreur, plusieurs couleurs ont été détectées pour la carte',carte.GetWord())
                pictColor='err'

            realColor = carte.GetColor()
            if pictColor == realColor :
                print(carte.GetColor())
                carte.SetFind(True)
            elif pictColor != realColor and pictColor != 'no': 
                print("Error : La couleur de la tuile ne correspond pas à la couleur associée à la carte")
