#Projet de Majeur Image : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier affichage :
    # Defintion des fonctions d'affichage 

import numpy as np
import math
from matplotlib import pyplot as plt
import math

#Methoed modifiant une image pour afficher la couleur des cartes
def fAffichage(newPartie, screen) : 
    #NB : Dessine le rectangle autour du mot
    #TODO : A revoir (pour un rectagle autour de la carte != autour du mot)
    [Ly, Lx, K] = np.shape(screen)
    for carte in newPartie.GetPlateau().GetGrille() : 
        
        print('new carte',carte.GetColor(), carte.GetWord())
        x0 = [math.ceil(carte.GetCoord()[0][0]),math.ceil(carte.GetCoord()[0][1])]
        x1 = [math.ceil(carte.GetCoord()[1][0]),math.ceil(carte.GetCoord()[1][1])]
        x2 = [math.ceil(carte.GetCoord()[2][0]),math.ceil(carte.GetCoord()[2][1])]
        x3 = [math.ceil(carte.GetCoord()[3][0]),math.ceil(carte.GetCoord()[3][1])]

        #Calcul du point de milieu
        middle = [math.floor((x0[0]+x1[0])/2) , math.floor((x0[1]+x3[1])/2)]
        print(middle)
        x_step = math.floor(110/2)
        up_step = 18
        bottom_step = 66-up_step
        
        if carte.GetColor() == 'b' : #Rectangle bleu
            for i_x in range (2*x_step+1):
                x = middle[0] - x_step + i_x
                if i_x == 0 or i_x == 2*x_step or carte.GetFind() == True:
                    for i_y in range (bottom_step+up_step+1) : 
                        y = middle[1] - bottom_step + i_y
                        screen[y, x , 0] = 0
                        screen[y, x , 1] = 0
                        screen[y, x , 2] = 255
                else : 
                    for i_y in [middle[1] - bottom_step , middle[1] + up_step] : 
                        screen[i_y, x , 0] = 0
                        screen[i_y, x , 1] = 0
                        screen[i_y, x , 2] = 255

        elif carte.GetColor() == 'r' : #Rectangle rouge
            for i_x in range (2*x_step+1):
                x = middle[0] - x_step + i_x
                if i_x == 0 or i_x == 2*x_step or carte.GetFind() == True:
                    for i_y in range (bottom_step+up_step+1) : 
                        y = middle[1] - bottom_step + i_y
                        screen[y, x , 0] = 255
                        screen[y, x , 1] = 0
                        screen[y, x , 2] = 0
                else : 
                    for i_y in [middle[1] - bottom_step , middle[1] + up_step] : 
                        screen[i_y, x , 0] = 255
                        screen[i_y, x , 1] = 0
                        screen[i_y, x , 2] = 0

        elif carte.GetColor() == 'r' : #Rectangle rouge
            for i_x in range (x1[0]-x0[0]):
                x = x0[0] + i_x
                if i_x == 0 or i_x == x1[0]-x0[0]-1 or carte.GetFind() == True:
                    for i_y in range (x3[1]-x0[1]+1) : 
                        screen[x0[1] + i_y, x , 0] = 0
                        screen[x0[1] + i_y, x , 1] = 0
                        screen[x0[1] + i_y, x , 2] = 255
                else : 
                    for i_y in [x3[1],x0[1]] : 
                        screen[i_y, x , 0] = 0
                        screen[i_y, x , 1] = 0
                        screen[i_y, x , 2] = 255

        elif carte.GetColor() == 'a' :  #Rectangle noir
            for i_x in range (2*x_step+1):
                x = middle[0] - x_step + i_x
                if i_x == 0 or i_x == 2*x_step or carte.GetFind() == True:
                    for i_y in range (bottom_step+up_step+1) : 
                        y = middle[1] - bottom_step + i_y
                        screen[y, x , 0] = 125
                        screen[y, x , 1] = 0
                        screen[y, x , 2] = 125
                else : 
                    for i_y in [middle[1] - bottom_step , middle[1] + up_step] : 
                        screen[i_y, x , 0] = 125
                        screen[i_y, x , 1] = 0
                        screen[i_y, x , 2] = 125
    
        
    return screen