#Projet de Majeur Image : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier Camera :
    # Gere les envois de la camera, et l'affichage du stream
  
import cv2, platform,time
import matplotlib.pyplot as plt
import numpy as np

# 0 = Use  local webcam
# 1 = Use peripheric webcam
cam = 1

cap = cv2.VideoCapture(cam)



if not cap:
    print("!!! Failed VideoCapture: invalid parameter!")

while(True): #Condition arret = partie finie
    # Capture frame-by-frame
    ret, current_frame = cap.read()

    #retour webcam
    cv2.imshow('retour',current_frame)

    #q por fermer la fenêtre
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #MAJ Partie
        #MAJ Grille + MAJ Partie
    
    #MAJ Affichage 


# release the capture
cap.release()
cv2.destroyAllWindows()
