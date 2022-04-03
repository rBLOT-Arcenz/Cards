from JeuEtHistoire import *
import sys
class Partie:

    def __init__(self):
        self.commencer()

    def commencer(self):
        '''
        Permet de lancer le jeu
        '''
        print("=============================================================================================\n\n")
        print("                                         Cards\n")
        print("Tapez:                           1 - Commencer le Jeu\n\n")
        print("=============================================================================================")
        selectionmenu = input()
        ##Les choix possibles et leurs actions
        if selectionmenu == "1":
            jeu = Jeu()
            jeu.histoire()
        elif selectionmenu == "2":
            a=1
        elif  not(selectionmenu == "2" or selectionmenu == "1"):
            print("Erreur, veuillez entrer une valeur valide.", file=sys.stderr)

p = Partie()

