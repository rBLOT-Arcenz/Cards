from JeuEtHistoire import *
from Combat import *
class camp:

    def choix(h):
        '''
        Entrée : Le Hero
        Action : Permet de choisir quoi faire dans le camp
        '''
        print("=============================================================================================\n\n")
        print("                       Vous trouver un feu de camp. Choisissez :\n")
        print("Tapez:     1 - Récupérer 30% de la santé max           2 - Améliorer une carte\n\n")
        print("=============================================================================================")
        choixcamp=input()

        ##Les valeurs possibles et leurs actions
        if choixcamp == "1":
            camp.soigner(h)
        if choixcamp == "2":
            camp.amecarte(h)

    def soigner(h):
        '''
        Entrée : Le Hero
        Action : Soigne le Héro
        '''
        print("Vous avez choisi de vous soigner. Vous récupérez", h._pvMax*0.4, "PV.")
        h.pv += h._pvMax*0.4  ##Soins
        if h.pv > h._pvMax: ##Si les pv dépasse la limite
            h.pv = h._pvMax
        print("Vous avez donc maintenant", h.pv,"/",h._pvMax,"PV")

    def amecarte(h):
        '''
        Entrée : Le Hero
        Action : Améliore une carte
        '''
        ##Print des cartes améliorables
        print("=============================================================================================\n\n")
        print("                           Choisissez une Carte à améliorer\n")
        cartes = ""
        compteurpascompté = 0  ##Ce compteur sert à ne pas afficher et prendre en compte les cartes déjà afficher
        for i in range(len(h._Deck)):
            Temp_Deck = h._Deck[i]
            if Temp_Deck["Amelioration"] == "":
                i+=1
                cartes += str(i-compteurpascompté)
                cartes += " - "
                i -= 1
                cartes += Temp_Deck['Nom']
                cartes += "    "
            else:
                compteurpascompté +=1

            if i == 4:
                cartes+= "\n"
        cartes += "\n"
        print(cartes)
        print("=============================================================================================")

        choix = int(input())
        i = 1
        for j in h._Deck:  ##Application de l'amélioration
            if not(j["Amelioration"] == "+"):
                i += 1
            if i == choix+1:
                j["Amelioration"] = "+"
                print("Vous avez amélioré la carte", j["Nom"], "\n Vous quittez le feu de camp.\n")
                return True

