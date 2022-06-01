#Projet de Majeur Image : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier Main : 
    #Lancement du code principal avec paramètres
    #A termes sera remplace par la fonction de gestion de la Caméra

import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

from classCarte import Carte
from classGrille import Grille
from classPartie import Partie
from affichage import fAffichage

#Test Creation d'une carte : OK
carte1 = Carte(0, [1,1], 'HELLO')
carte2 = Carte(25, [12,90], 'SOLEIL')
carte2.SetColor('r')
carte2.SetFind(True)

#Test Creation d'une grille : OK
#grille1 = Grille(4, 0)

#Test Creation d'une partie
Image = cv2.imread('grille.png')

print (np.shape(Image), '\n')

partie1 = Partie(Image)
ImageColor = fAffichage(partie1, Image)

plt.figure()
plt.imshow(ImageColor)
plt.show()

carte = partie1.GetPlateau().GetGrille()[5]
carte.Affichage()
carte.SetFind(True)

ImageColor = fAffichage(partie1, Image)

plt.figure()
plt.imshow(ImageColor)
plt.show()


#Test detection de mot
#reader = easyocr.Reader(['fr']) # this needs to run only once to load the model into memory
#result = reader.readtext("prout.jpg")
#print( result)