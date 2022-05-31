#Projet de Majeur Image : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier Main : 
    #Lancement du code principal avec paramètres
    #A termes sera remplace par la fonction de gestion de la Caméra

from classCarte import Carte
from classGrille import Grille
from classPartie import Partie

#Test Creation d'une carte : OK
carte1 = Carte(0, [1,1], 'HELLO')
carte1.Affichage()

carte2 = Carte(25, [12,90], 'SOLEIL')
carte2.Affichage()

carte2.SetColor('r')
carte2.Affichage()

carte2.SetFind(True)
carte2.Affichage()

#Test Creation d'une grille : OK
grille1 = Grille(4, 0)

#Test Creation d'une partie
partie1 = Partie(0)