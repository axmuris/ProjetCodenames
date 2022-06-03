#Projet de Majeur I : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier Main : 
    #Lancement du code principal avec paramètres
    #A termes sera remplace par la fonction de gestion de la Caméra

import cv2
import matplotlib.pyplot as plt
import numpy as np

from fctImage import *
from classPartie import Partie

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
"""
Irgb = cv2.imread('grille.png')
partie1 = Partie(Irgb)
partie1.SetMotifFin('a')

ImFinal = fAffFin(partie1)

plt.figure()
plt.imshow(ImFinal)
plt.show()
"""

#Test detection de mot
#reader = easyocr.Reader(['fr']) # this needs to run only once to load the model into memory
#result = reader.readtext("prout.jpg")
#print( result)

#Test Final avec image
current_frame = cv2.imread('resultat.png')

#Initialisation de la partie
newPartie = Partie(current_frame)

createFin()
current_frame, ImGrad, ImLabel = fInitAff(newPartie, current_frame)

while True:
    cv2.imshow('plateau',current_frame)

    #q por fermer la fenêtre
    if cv2.waitKey(33):
        stop=1
        break

while(newPartie.GetMotifFin()=='n'): #Condition arret = partie finie
    
    while(True):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #MAJ Partie
    newPartie.GetPlateau().MAJ_Grille(current_frame)
    newPartie.MAJ_Partie()
    
    #MAJ Affichage 
    current_frame = fMajAff(newPartie, current_frame, ImGrad, ImLabel)

    #retour webcam
    cv2.imshow('plateau',current_frame)

#MAJ Partie
newPartie.GetPlateau().MAJ_Grille(current_frame)
newPartie.MAJ_Partie()

#MAJ Affichage 
current_frame = fMajAff(newPartie, current_frame, ImGrad, ImLabel)

#retour webcam
cv2.imshow('plateau',current_frame)

while(True):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#Affichage du motif de fin de partie
if newPartie.GetMotifFin() == 'r' : 
    ImFin = cv2.imread('ImFinRouge.png')
elif newPartie.GetMotifFin() == 'b' : 
    ImFin = cv2.imread('ImFinBleu.png')
else :
    ImFin = cv2.imread('ImFinAssassin.png')
cv2.imshow('plateau',ImFin)


while(True):
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

print("Fin de partie")

# release the capture
cv2.destroyAllWindows()