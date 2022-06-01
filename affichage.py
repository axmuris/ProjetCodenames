#Projet de Majeur Image : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier affichage :
    # Defintion des fonctions d'affichage 

import numpy as np

def fAffichage(newPartie, screen) : 
    #NB : Colorie le rectangle autour du mot
    #TODO : A revoir (pour un rectagle autour de la carte != autour du mot)
    for carte in newPartie.GetPlateau().GetGrille() : 
        x0 = carte.GetCoord[0]
        x1 = carte.GetCoord[1]
        x2 = carte.GetCoord[2]
        x3 = carte.GetCoord[3]
        #On dessine un rectangle
        x = np.arange(x0[0], x1[0], 1)
        y =  (x0[1], x3[1])
        #Si la carte est recouverte, on colorie le rectangle
        if carte.GetFind() == True :
            y =  np.arange(x0[1], x3[1], 1)
        if carte.GetColor() == 'b' : #Rectangle bleu
            screen[x, y , 0] = 0
            screen[x , y , 1] = 0
            screen[x , y , 2] = 255
        elif carte.GetColor() == 'r' : #Rectangle rouge
            screen[x , y , 0] = 255
            screen[x , y , 1] = 0
            screen[x , y , 2] = 0
        if carte.GetColor() == 'a' :  #Rectangle noir
            screen[x , y , 0] = 0
            screen[x , y , 1] = 0
            screen[x , y , 2] = 0
    return screen