#Projet de Majeur I : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier Main : 
    #Lancement du code principal avec paramètres
    #A termes sera remplace par la fonction de gestion de la Caméra

import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import math
from PIL import Image, ImageFont, ImageDraw

from classCarte import Carte
from classGrille import Grille
from classPartie import Partie
from affichage import fAffichage
from fctImage import fAffFin, fMajAff

#Test Creation d'une carte : OK
#carte1 = Carte(0, [1,1], 'HELLO')
#carte2 = Carte(25, [12,90], 'SOLEIL')
#carte2.SetColor('r')
#carte2.SetFind(True)

#Test Creation d'une grille : OK
#grille1 = Grille(4, 0)

#Test Creation d'une partie
"""
I = cv2.imread('grille.png', 0)

partie1 = Partie(I)


ImLabel = fImCarte(I)

ImGrad = fImGrad(I)

Irgb = cv2.imread('grille.png')
ImContour = fDessinContour(partie1, Irgb, ImLabel, ImGrad)

plt.figure()
plt.imshow(Irgb)
plt.show()

carte = partie1.GetPlateau().GetGrille()[5]
carte.Affichage()
carte.SetFind(True)
carte.Affichage()

Irgb = fDessinTuile(partie1, ImContour, ImLabel)

for carte in partie1.GetPlateau().GetGrille() :
    carte.SetFind(True)

Irgb = fDessinTuile(partie1, ImContour, ImLabel)

plt.figure()
plt.imshow(Irgb)
plt.show()
"""
"""
#Test fMajAff
Irgb = cv2.imread('grille.png')
partie1 = Partie(Irgb)

ImFinal = fMajAff(Irgb, partie1)
plt.figure()
plt.imshow(ImFinal)
plt.show()
"""

"""
carte = partie1.GetPlateau().GetGrille()[5]
carte.Affichage()
carte.SetFind(True)

IColor = fAffichage(partie1, I)

plt.figure()
plt.imshow(IColor)
plt.show()
"""

#Test affichage de fin
Irgb = cv2.imread('grille.png')
partie1 = Partie(Irgb)
partie1.SetMotifFin('a')

ImFinal = fAffFin(partie1)

plt.figure()
plt.imshow(ImFinal)
plt.show()

#Test detection de mot
#reader = easyocr.Reader(['fr']) # this needs to run only once to load the model into memory
#result = reader.readtext("prout.jpg")
#print( result)