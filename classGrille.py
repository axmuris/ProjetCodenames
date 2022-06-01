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
    def fDetecCarte(self, screen) : 
        matCarte = []
        screen = 0
        #TODO : Detection des mots
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

