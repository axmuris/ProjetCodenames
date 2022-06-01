#Projet de Majeur Image : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier Camera :
    # Gere les envois de la camera, et l'affichage du stream
  
import cv2
import matplotlib.pyplot as plt
import numpy as np

from affichage import fAffichage
from classPartie import Partie

# 0 = Use  local webcam
# 1 = Use peripheric webcam
cam = 0

cap = cv2.VideoCapture(cam)

if not cap:
    print("!!! Failed VideoCapture: invalid parameter!")

#Premère capture
ret, current_frame = cap.read()

#Initialisation de la partie
newPartie = Partie(current_frame) #screen a definir
current_frame = fAffichage(newPartie, current_frame)

while(True): #Condition arret = partie finie

    # Capture frame-by-frame
    ret, current_frame = cap.read()

    #MAJ Partie
    newPartie.GetPlateau().MAJ_Grille()
    etat, motifEnd = newPartie.MAJ_Partie()
    
    #MAJ Affichage 
    current_frame = fAffichage(newPartie, current_frame)

    #retour webcam
    cv2.imshow('retour',current_frame)

    #q pour fermer la fenêtre
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# release the capture
cap.release()
cv2.destroyAllWindows()
