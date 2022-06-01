    #TP de traitement d'image
    #Ligne de partage des eaux

    #Alice Malosse & Axel Nael

import numpy as np
import cv2
from matplotlib import pyplot as plt


def fLPE(I) :
    #################################################################
    #Obtention des marqueurs

    #Seuillage de l'image
    [th, Iseuil] = cv2.threshold(I, 100, 255, cv2.THRESH_BINARY)

    #Isolation des marqueurs

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
    carteDist = Iseuil - carteDist  #priorite au centre des bonbons

    #################################################################
    #Algorithme LPE

    #Initialisation FAH
    FAH_x = []
    FAH_y = []
    for i in range (255) : 
        FAH_x.append([])
        FAH_y.append([])

    n, m = Ilabel.shape

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



def fImGrad (I) : 
    [th, ImSeuil] = cv2.threshold(I, 100, 255, cv2.THRESH_BINARY)

    s = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
    
    ImSeuil = cv2.morphologyEx(ImSeuil, cv2.MORPH_CLOSE, s)
    ImSeuil = cv2.morphologyEx(ImSeuil, cv2.MORPH_OPEN, s)

    ImGrad = cv2.Laplacian(ImSeuil, cv2.CV_64F)
    ImGrad = cv2.erode(ImSeuil, s, 1) - cv2.dilate(ImSeuil, s, 1)

    return ImGrad