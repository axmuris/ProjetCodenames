#Projet de Majeur Image : 
#Suivi d'une partie de Cone Names

#Alice Malosse & Axel Nael

#Fichier classCarte : 
    #Definition de la classe Carte

#Attributs : ID(indice dans la matrice grille), position (dans image), mot, couleur(neutre), recouverte
#Constructeur : Initiialisation des atributs par défauts
                #Analyse du mot (finalement dans grille) et MAJ attribut mot

class Carte () :
    ################################################
    #Initialisation
    def __init__ (self, ID, pos, mot):
        self.__ID = ID
        self.__coord = pos
        self.__word = mot
        self.__color = 'n'
            #neutre = n, rouge = r, bleu = b, assassin = a
        self.__find = False
        self.__label = 0
    
    ################################################
    #Getters
    def GetID(self,) :
        return self.__ID

    def GetCoord(self,) : 
        return self.__coord

    def GetWord(self,) : 
        return self.__word

    def GetColor(self,) : 
        return self.__color

    def GetFind(self,) : 
        return self.__find

    def GetLabel(self,) : 
        return self.__label

    ################################################
    #Setters
    def SetColor(self, couleur) :
        self.__color = couleur

    def SetFind(self, recouverte) : 
        self.__find = recouverte

    def SetLabel(self, label) : 
        self.__label = label

    ################################################
    #Methode
    def Affichage(self,) : 
        print("ID : ", self.__ID, " Position : ", self.__coord, " Mot : ", self.__word, " Couleur : ", self.__color, " Recouverte : ", self.__find, " Label : ", self.__label, "\n")