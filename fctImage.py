    #TP de traitement d'image
    #Ligne de partage des eaux

    #Alice Malosse & Axel Nael

import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

def fMajAff( partie,Irgb) :
    Igray = cv2.cvtColor(Irgb, cv2.COLOR_BGR2GRAY)
    ImLabel = fImCarte(Igray)
    ImGrad = fImGrad(Igray)

    ImContour = fDessinContour(partie, Irgb, ImLabel, ImGrad)
    ImFinal = fDessinTuile(partie, ImContour, ImLabel)

    return ImFinal

def fLPE(Ilabel, carteDist) :
    #################################################################
    #Algorithme LPE

    #Initialisation FAH
    FAH_x = []
    FAH_y = []
    for i in range (255) : 
        FAH_x.append([])
        FAH_y.append([])

    n,m = np.shape(Ilabel)

    for x in range (n) :
        for y in range (m) :
            if Ilabel[x,y] != 0 : #si pixel dans un marqueur
                color = int (carteDist[x,y])

                FAH_x[color].append(x)
                FAH_y[color].append(y)

    #Implementation de l'algorithme
    i = 0
    while FAH_x != [] :
        #Suppression des listes de priorite vide
        if FAH_x[0] == [] :
            FAH_x.pop(0)
            FAH_y.pop(0)
            i += 1
        else :
            #Extraction d'un pixel
            coord_x = FAH_x[0].pop(0)
            coord_y = FAH_y[0].pop(0)

            #Definition des 4 voisins 
            voisin = [[coord_x+1, coord_y], [coord_x-1, coord_y], [coord_x, coord_y+1], [coord_x, coord_y-1]]

        #Definition du label des voisins
            for nbV in range (len(voisin)) :
                xV = voisin[nbV][0]
                yV = voisin[nbV][1]
                #Verification pixel dans l'image
                if ((xV>=0) and (yV>=0) and (xV!=n) and (yV!=m)) :
                    #Si pas de label
                    if Ilabel[xV, yV] == 0 :
                        #Attribution d'un label
                        Ilabel[xV, yV] = Ilabel[coord_x, coord_y]
                        #Ajout du pixel a FAH
                        color = int (carteDist[xV, yV]) - i
                        if color < 0 :
                            color = 0
                        FAH_x[color].append(xV)
                        FAH_y[color].append(yV)

    return Ilabel

#Definition de l'image de label des cartes
def fImCarte (I) :
    #################################################################
    #Obtention des marqueurs

    #Seuillage de l'image
    [th, Iseuil] = cv2.threshold(I, 100, 255, cv2.THRESH_BINARY)

    #Definition de l'element structurant
    s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    #Erosion de l'image pour obtenir les marqueurs
    Imark = cv2.erode(Iseuil, s)
    Ifond = cv2.dilate(Iseuil, s)
    #Ajout du marqueu de fond
    Imark = Imark + (255 - Ifond)

    #Attribution des labels uniques aux marqueurs
    [nLabel, Ilabel] = cv2.connectedComponents(Imark)

    #################################################################
    #Obtention de la carte des distances

    #NB : noir = priorite eleve
    carteDist = cv2.distanceTransform(Iseuil, cv2.DIST_L2, 3)
    carteDist = (255*carteDist)/np.amax(carteDist)  #maximum a 255
    carteDist = Iseuil - carteDist

    #################################################################
    #Application de l'algorithme de LPE
    ImLabel = fLPE(Ilabel, carteDist)

    return ImLabel


#Defintion des labels des gradient des cartes 
def fImGrad (I) : 
    #Seuillage de l'image
    [th, ImSeuil] = cv2.threshold(I, 100, 255, cv2.THRESH_BINARY)

    #Isolation des cartes
    s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    
    ImSeuil = cv2.morphologyEx(ImSeuil, cv2.MORPH_OPEN, s)
    ImSeuil = cv2.morphologyEx(ImSeuil, cv2.MORPH_CLOSE, s)

    #Calcul du gradient pour avoir le contour des cartes (marqueurs)
    s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    ImGrad = cv2.erode(ImSeuil, s, 1) - cv2.dilate(ImSeuil, s, 1)

    #Ajustement
    s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    ImGrad = cv2.dilate(ImGrad, s, 1)

    #Attribution des labels uniques aux marqueurs
    [nLabel, ImGrad] = cv2.connectedComponents(ImGrad)

    return ImGrad

#Fonction dessinant les contours sur la current frame
    #plus attribution des labels aux cartes
def fDessinContour (partie,Irgb, ImLabel, ImGrad) : 
    for carte in partie.GetPlateau().GetGrille() : 
        #Attribution du label associer a la carte
        carte.SetLabel(ImLabel[carte.GetCoord()[0][1], carte.GetCoord()[0][0]])

        #Initialisation de la couleur
        color = [0,0,0]
        if carte.GetColor() == 'b' :
            color = [0,0,1]
        elif carte.GetColor() == 'r' : 
            color = [1,0,0]
        elif carte.GetColor() == 'a' :
            color = [0.18, 0.1, 0.3]
        else :  #cartes neutre
            color = [0.95, 0.8, 0.6]

        #Initialisation du label de gradient de la carte
        x = carte.GetCoord()[0]  #[x,y]
        while ImGrad[x[1], x[0]] == 0 :
            x[1] -= 1
        labelGrad = ImGrad[x[1], x[0]]

        #Colorisation des contours des cartes
        for y in range (np.shape(Irgb)[0]):
            for x in range (np.shape(Irgb)[1]) :
                if ImGrad[y,x] == labelGrad :
                    Irgb[y, x , 0] = math.floor(color[0]*255)
                    Irgb[y, x , 1] = math.floor(color[1]*255)
                    Irgb[y, x , 2] = math.floor(color[2]*255)

    return Irgb


#Fonction colorisant une carte si elle est recouverte
def fDessinTuile(partie, Irgb, ImLabel) :
    for carte in partie.GetPlateau().GetGrille() : 

        if carte.GetFind() == True : 
            #Initialisation de la couleur
            color = [0,0,0]
            if carte.GetColor() == 'b' :
                color = [0,0,1]
            elif carte.GetColor() == 'r' : 
                color = [1,0,0]
            elif carte.GetColor() == 'a' :
                color = [0.18, 0.1, 0.3]
            else :  #cartes neutre
                color = [0.95, 0.8, 0.6]

            #Colorisation des contours des cartes
            for y in range (np.shape(Irgb)[0]):
                for x in range (np.shape(Irgb)[1]) :
                    if ImLabel[y,x] == carte.GetLabel() :
                        Irgb[y, x , 0] = math.floor(color[0]*255)
                        Irgb[y, x , 1] = math.floor(color[1]*255)
                        Irgb[y, x , 2] = math.floor(color[2]*255)

    return Irgb
