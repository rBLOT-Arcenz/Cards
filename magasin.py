from JeuEtHistoire import *
from Combat import *
from camp import *

class magasin:


    def choix(h):
        '''
        Entrée : Le Hero
        Action : Permet à l'utilisateur de choisir quoi acheter
        '''
        choixmagasin = "99"
        while not(choixmagasin == "0"):
            print("=============================================================================================\n\n")
            print("                       Vous trouver un magasin. Choisissez quoi acheter:\n")
            print("                                     0 - Quitter le Magasin\n")
            print("Tapez:     1 - +1 de Stamina (200)           2 - Améliorer une carte (70)\n")
            print("           3 - Acheter une carte (50~200)    4 - Supprimer une carte (70)\n")
            print("Argent = ", h.Argent, "\n\n")
            print("=============================================================================================")
            choixmagasin=input()

        ## Les choix possible
            if choixmagasin == "1":
                magasin.staminaplus(h)

            elif choixmagasin == "motherlode":  ##Code triche
                h.Argent+=1000
                print("Vous êtes pauvre. Votre maman vous donne 1000 d'Argent.")

            elif choixmagasin == "money 0":
                h.Argent = 0
                print("Vous avez choisi de vous même de diminuer votre argent ? Vous êtes quelqu'un de bizarre, mais soit, c'est votre droit.")

            elif choixmagasin == "2":
                if h.Argent < 70 :
                    print("Vous n'avez assez d'argent pour acheter cette article.")
                else:
                    camp.amecarte(h)
                    h.Argent -= 70

            elif choixmagasin == "3":
                magasin.carteplus(h)

            elif choixmagasin == "4":
                magasin.supprcarte(h)
            
            elif not(choixmagasin == "0"):
                print("Veuillez entrer une valeur valide.")

              

    def staminaplus(h):
        '''
        Entrée : Le Hero
        Action : Augmente la stamina minimum contre de l'argent
        '''
        if h.Argent < 200 :
            print("Vous n'avez assez d'argent pour acheter cette article.")
            return True
        else:
            h.AmeStamina +=1
            h.Argent -= 200
            print("Vous avez maintenant", h.AmeStamina+3,"point de stamina.")
            return False
    


    def carteplus(h):
        '''
        Entrée : Le Hero
        Action : Permet d'acheter une carte
        '''
        entrainachatcarte = 1  ##Boucle permettant d'acheter plusieurs cartes
        while entrainachatcarte == 1:

            if h.Argent < 50:  ##si pas assez d'argents
                print("Vous n'avez assez d'argent pour acheter cette article.")
                return False

            else:
                print("=============================================\n")  ##Print des cartes achetable
                print("0 - Revenir au menu précédent.\n")
                print("             Choisissez une carte\n")
                for i in range(len(h._BiblioCartes)):
                    temp_BiblioCartes = h._BiblioCartes[i]
                    print (i+1," - ", temp_BiblioCartes["Nom"],", Prix = ",50*((temp_BiblioCartes["Stamina"]+1)/2),", Prix(+) = ",100*((temp_BiblioCartes["Stamina"]+1)/2), ".\n")
                print("Veuillez choisir une valeur, et non du texte.\n")
                print("\n=============================================")

                choixachatcarte = int(input())

                if choixachatcarte == 0:  ##Pour retourner au menu précédent
                    entrainachatcarte = 0
                    print("Vous retournez au menu précédent (presser entrée).")
                    input()

                elif choixachatcarte > len(h._BiblioCartes) or choixachatcarte < 0:
                    print("Veuillez entrer une valeur valide.")
                else:
                    armeaajouter = h._BiblioCartes[choixachatcarte-1]
                    print("\nVoulez-vous acheter cette carte en améliorée (plus cher) ?")
                    print("1 - Oui")
                    print("2 - Non")
                    choixamelioration = int(input())

                    if choixamelioration == 1:  ##Si la carte à acheter est améliorée
                        if h.Argent >= 100*((armeaajouter["Stamina"]+1)/2):
                            h._Deck.append({'Nom':  armeaajouter['Nom'], 'Amelioration': '+'})
                            h.Argent-=100*((armeaajouter["Stamina"]+1)/2)
                            print("Vous avez acheter",armeaajouter['Nom'], "amélioré. Vous avez maintenant", h.Argent,"Argent.")
                            print("Appuyer sur Entrée pour continuer")
                            input()
                        else:
                            print("Vous n'avez pas assez d'Argents pour acheter ceci.")
                            return False

                    elif choixamelioration == 2: ##Si la carte à acheter n'est pas améliorée
                        if h.Argent >= 50*((armeaajouter["Stamina"]+1)/2):
                            h._Deck.append({'Nom':  armeaajouter['Nom'], 'Amelioration': ''})
                            h.Argent-=50*((armeaajouter["Stamina"]+1)/2)
                            print("Vous avez acheter",armeaajouter['Nom'], ". Vous avez maintenant", h.Argent,"Argent.")
                            print("Appuyer sur Entrée pour continuer")
                            input()
                        else:
                            print("Vous n'avez pas assez d'Argents pour acheter ceci.")
                            return False

                    else :
                        print("Veuillez entrer une valeur valide.")
        return False ##Return qui permet le retour au menu précédent sans problème



    def supprcarte(h):
        '''
        Entrée : Le Hero
        Action : Permet de supprimer une carte
        '''
        if h.Argent < 70:
                print("Vous n'avez assez d'argent pour acheter cette article.")
                return False

        entrainsupprcarte = 1  ##Boucle permettant de supprimer plusieurs cartes
        while entrainsupprcarte == 1:

            print("=============================================\n") ##Affichage des cartes supprimable
            print("0 - Revenir au menu précédent.\n")
            print("      Choisissez une Carte à supprimer\n")
            cartes=""
            for i in range(len(h._Deck)):
                Temp_Deck = h._Deck[i]
                i+=1
                cartes += str(i)
                cartes += " - "
                i -= 1
                cartes += Temp_Deck["Nom"]
                if Temp_Deck["Amelioration"] == "+":
                    cartes += "+"
                cartes+= "\n"
            cartes += "\n"
            print(cartes)
            print("=============================================")

            choixsupprcarte = int(input())
            if choixsupprcarte == 0:  ##Si retour en arrière
                entrainsupprcarte = 0
                print("Vous retournez au menu précédent (presser entrée).")
                input()

            elif entrainsupprcarte > len(h._Deck) or entrainsupprcarte < 0: ##Si valeur invalide
                print("Veuillez entrer une valeur valide.")
            
            else:
                if h.Argent >= 70: ##Si tout va bien
                    del h._Deck[choixsupprcarte-1]
                    h.Argent-=70
                else:
                    print("Vous n'avez assez d'argent pour acheter cette article.")
                    return False
        return False