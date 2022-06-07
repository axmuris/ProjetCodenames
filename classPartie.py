#Projet de Majeur Image : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier classPartie : 
    #Defintion de la classe Partie : Gestion de la partie de Code Names

#Constructeur : créer une grille vide de taille n et lui envoyer l'image de d'init
            #Genere liste mot maitre espion, puis affiche (console)

#MAJ partie : MAJ listes mot maitre espion + MAJ etat partie(list mot vide OU assassin)

from classCarte import Carte
from classGrille import Grille

class Partie () :
    ################################################
    #Initialisation
    def __init__(self, screen) :
        self.__plateau = Grille(5, screen)
        if self.__plateau.GetAccord()==0:
            return 

        self.__motRouge = []
        self.__motBleu = []
        self.__etatPartie = 0 # Initial = 0 , En cours = 1 , Fini = 2
        self.__motifFin = 'n' 
            # En cours = n , Rouge gagnant = r, Bleu gagnant = b, Assassin trouve = a

        for carte in self.__plateau.GetGrille() : 
            if carte.GetColor() == 'r' : 
                self.__motRouge.append(carte.GetWord())
            elif carte.GetColor() == 'b' :
               self.__motBleu.append(carte.GetWord())
            elif carte.GetColor() == 'a' : 
                self.__assassin = carte.GetWord()

        print('Maître espion rouge : ', self.__motRouge)
        print('\nMaître espion bleu : ', self.__motBleu)
        print("\nL'assasin est : ", self.__assassin)

        self.__etatPartie = 1

    ################################################
    #Getters
    def GetPlateau(self,) : 
        return self.__plateau

    def GetMotifFin(self,) : 
        return self.__motifFin

    def GetAccord(self,) :
        return self.__plateau.GetAccord()

    ################################################
    #Setter
    def SetMotifFin(self, motif) : 
        self.__motifFin = motif
    
    def SetAccord(self, Accord) : 
        self.__plateau.SetAccord(Accord)

    ################################################
    #Methodes
    def MAJ_Partie(self,) : # TODO : A tester
        self.__motBleu = []
        self.__motRouge = []
        for carte in self.__plateau.GetGrille() : 
            #MAJ des listes maitre espion
            if carte.GetColor() == 'r' and carte.GetFind() == False : 
                self.__motRouge.append(carte.GetWord())
            elif carte.GetColor() == 'b' and carte.GetFind() == False : 
                self.__motBleu.append(carte.GetWord())

            #Verification assassin
            elif carte.GetColor() == 'a' and carte.GetFind() == True : 
                self.__motifFin = 'a'

        print('Maître espion rouge : ', self.__motRouge)
        print('\nMaître espion bleu : ', self.__motBleu)
        print("\nL'assasin est : ", self.__assassin)

        #Verification si gagnant
        if self.__motBleu == [] : 
            self.__motifFin = 'b'
        elif self.__motRouge == [] :
            self.__motifFin = 'r'

        return
