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
import random
import easyocr
from classCarte import Carte

class Grille () : 
    ################################################
    #Initialisation
    def __init__(self, n, screen) :
        self.__grille = []

        #Creation des cartes
        matCarte = self.fDetecCarte(screen)
        for ID in range (n*n) : 
            #self.__grille[ID] = Carte(ID, matCarte[ID][0], matCarte[ID][1])
            self.__grille.append(Carte(ID, [ID,'0'], "Hello"))

        #Attribution des couleurs
        self.fSetColors(n)

    ################################################
    #Getter
    def GetGrille(self,) : 
        return self.__grille

    ################################################
    #Methodes
    def fDetecCarte(self, screen,n) : 
        matCarte = []
        screen = 0
        reader = easyocr.Reader(['fr']) # this needs to run only once to load the model into memory
        result = reader.readtext(screen)

        indiceSuppr=[] #Liste d'indice des mot à supprimer
        for resul in result:
            if resul[2]<=0.1: #retire le mot si proba<0.1
                indiceSuppr.append(result.index(resul))
            elif len(resul[1])<=2: #retire le mot si 2 lettres ou moins
                indiceSuppr.append(result.index(resul))
            else: #retire le mot si présence d'un caractère bizarre
                sup=0
                for lettre in resul[1]:
                    l=ord(lettre) #conversion de la lettre en code Ascii
                    if ((l in range(33,64)) or (l in range(91,96)) or (l in range(123,126))): #liste des caractères étranges
                        sup=1
                if sup==1:
                    indiceSuppr.append(result.index(resul))

        for i in sorted(indiceSuppr, reverse=True): #suppression des mots de la liste d'indice
            del(result[i])

        #test du nombre de mot 
        if len(result)<(n*n): #Si pas assez de mot, message d'erreur (et renvoit code erreur?) 
            print("Erreur, tous les mot n'ont pas été détecté. Vérifiez qu'il y ai bien un carré de",n,"*",n,"sur la grille.")
        
        elif len(result)>n*n: #Si trop de mot, supprime les mots les plus improbables
            while len(result)!=n*n:
                probmin=1
                for resul in result:
                    if resul[2]<probmin:
                        probmin=resul[2]
                        motfaible=resul
                result.pop(result.index(motfaible))
        

        #set mot


        return matCarte

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

    def MAJ_Grille(self, screen) : #TODO : A tester
        for carte in self.GetGrille() : 
            #TODO : Defintion couleur au centre, pictColor
            pictColor = 'r'
            realColor = carte.GetColor()
            if pictColor != realColor : 
                print("Error : La couleur de la tuile ne correspond pas à la couleur associée à la carte")
            else : 
                carte.SetFind(True)

