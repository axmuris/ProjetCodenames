#Projet de Majeur Image : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier Camera :
    # Gere les envois de la camera, et l'affichage du stream
  
import cv2, platform,time
import matplotlib.pyplot as plt
import numpy as np
import classCarte,classGrille,classPartie

from classPartie import Partie

# 0 = Use  local webcam
# 1 = Use peripheric webcam
cam = 0

cap = cv2.VideoCapture(cam)

if not cap:
    print("!!! Failed VideoCapture: invalid parameter!")

ret, current_frame = cap.read()

#Prendre un screen


#Initialisation de la partie
newPartie = Partie(screen) #screen a definir
#Maj affichage ???

while(True): #Condition arret = partie finie

    # Capture frame-by-frame
    ret, current_frame = cap.read()

    #MAJ Partie
    newPartie.GetPlateau().MAJ_Grille()
    etat, motifEnd = newPartie.MAJ_Partie()
    
    #MAJ Affichage 
    Affichage(screen)

    #retour webcam
    cv2.imshow('retour',current_frame)

    #q pour fermer la fenêtre
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# release the capture
cap.release()
cv2.destroyAllWindows()


def Affichage(screen) : 
    #NB : Ne colorie qu'un seul pixel pour l'instant
    #TODO : A revoir / Completer
    for carte in newPartie.GetPlateau().GetGrille() : 
        if carte.GetColor() == 'b' : 
            screen[carte.GetCoord[0][0], carte.GetCoord[0][1], 0] = 0
            screen[carte.GetCoord[0][0], carte.GetCoord[0][1], 1] = 0
            screen[carte.GetCoord[0][0], carte.GetCoord[0][1], 2] = 255
        elif carte.GetColor() == 'r' : 
            screen[carte.GetCoord[0][0], carte.GetCoord[0][1], 0] = 255
            screen[carte.GetCoord[0][0], carte.GetCoord[0][1], 1] = 0
            screen[carte.GetCoord[0][0], carte.GetCoord[0][1], 2] = 0
        if carte.GetColor() == 'a' : 
            screen[carte.GetCoord[0][0], carte.GetCoord[0][1], 0] = 0
            screen[carte.GetCoord[0][0], carte.GetCoord[0][1], 1] = 0
            screen[carte.GetCoord[0][0], carte.GetCoord[0][1], 2] = 0