#Projet de Majeur Image : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier Camera :
    # Gere les envois de la camera, et l'affichage du stream
  
import cv2
import matplotlib.pyplot as plt
import numpy as np

from affichage import fAffichage
from fctImage import *
from classPartie import Partie

# 0 = Use  local webcam
# 1 = Use peripheric webcam (contrast=4%, brigthness=0%) 
cam = 1

cap = cv2.VideoCapture(cam)

if not cap:
    print("!!! Failed VideoCapture: invalid parameter!")

#Premère capture
ret, current_frame = cap.read()

#Initialisation de la partie
newPartie = Partie(current_frame)

current_frame = fMajAff(newPartie, current_frame)


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

    # Capture frame-by-frame
    ret, current_frame = cap.read()

    #MAJ Partie
    newPartie.GetPlateau().MAJ_Grille(current_frame)
    newPartie.MAJ_Partie()
    
    #MAJ Affichage 
    current_frame = fMajAff(newPartie, current_frame)

    #retour webcam
    cv2.imshow('retour',current_frame)


#affichage écran fin


# release the capture
cap.release()
cv2.destroyAllWindows()
