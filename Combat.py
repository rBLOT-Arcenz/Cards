import random
from JeuEtHistoire import *

class Color: # Permet de changer la couleur du texte à afficher
    End = '\033[0m'
    Red          = "\033[31m"
    Green        = "\033[32m"
    Blue         = "\033[34m"
    Magenta      = "\033[35m"
    LightMagenta = "\033[95m"
    Bold       = "\033[1m"

    # Exemple d'utilisation : print(Color.Red + "Texte en rouge" + Color.End)


class Hero:
    ## Liste de toutes les cartes du jeu
    _BiblioCartes=[{'Nom':'Épée','Type':'A','Dmg':10,'Stamina':1,'Description': "Un coup d'épée simple. Inflige 10 de dégats. Consome 1 de stamina","DescAmélioration":"+5 dégats"},
                    {'Nom':'Bouclier','Type':'D','Défence':10,'Stamina':1,'Description': "Une protection simple. Gain de 10 de défence. Consome 1 de stamina","DescAmélioration":"+5 défence"},
                    {'Nom':'Inventaire','Type':'S','Stamina':2,'Description': "Pioche 2 carte dans le deck et les rajoute à la main. Consome 2 de Stamina.","DescAmélioration":"Consome 1 de Stamina au lieu de 2"},
                    {'Nom':'Soin','Type':'S','Stamina':2,'Description': "Soigne le Héro pour 1/4 des PV max. La carte est retirée du deck jusqu'à la fin du combat. Consome 2 de Stamina","DescAmélioration":"Soigne le Héro pour 1/2 des PV max au lieu de 1/4."},
                    {'Nom':'Peau de roche','Type':'D','Défence':30,'Stamina':3,'Description': "Une protection résistante. Gain de 30 de défence. Consome 3 de stamina","DescAmélioration":"+15 défence"},
                    {'Nom':'Hache de guerre','Type':'A','Dmg':36,'Stamina':3,'Description': "Une arme puissante mais très lourde. Inflige 36 de dégats. Consomme 3 de stamina","DescAmélioration":"Consome 2 de stamina"},
                    {'Nom':'Lame cachée','Type':'S','Dmg':12,'Stamina': 2,'Description': "Lance un couteau vous permettant de prendre des lames cachée dans votre veste. Inflige 12 de dégat. Consomme 2 de stamina. Ajout de 3 cartes 'Couteau de lancer' dans le deck. La carte est retirée du deck jusqu'à la fin du combat.  \n\n 'Couteau de lancer' : Petite dague conçue pour être lancée. Inflige 6 de dégats. Consomme 0 Stamina. Est consommée après utilisation. Est perdue à la fin du combat","DescAmélioration":"Ajout de 1 carte 'Couteau de lancer +' dans la main qui inflige 12 de dégat au lieu de 6."},
                    {'Nom':'Couteau de lancer','Type':'S','Dmg':6,'Stamina':0,'Description': "Petite dague conçue pour être lancée. Inflige 6 de dégats. Consomme 0 Stamina. Est consommée après utilisation. Est perdue à la fin du combat","DescAmélioration":"Inflige 12 de dégat au lieu de 6"},
                    {'Nom':'Méditation','Type':'S','Dmg':0,'Stamina':0,'Description': "Vous vous reposer au milieu du combat. Consomme 0 de stamina. Gain de 2 stamina. La carte est retirée du deck jusqu'à la fin du combat.","DescAmélioration":"Gain de 3 de stamina au lieu de 2"},
                    {'Nom':'Carte blindées','Type':'S','Défence':10,'Stamina':4,'Description': "Vos Carte vous recouvre et vous protège. Gain de 10 de défence pour chaque carte dans le deck. Consomme 4 stamina. La carte est retirée du deck jusqu'à la fin du combat.","DescAmélioration":"Gain de 15 de défence au lieu de 10"}]
    ## Liste du deck de départ
    _Deck = [{'Nom': 'Épée','Amelioration': '+'},{'Nom': 'Épée','Amelioration': '+'},{'Nom': 'Épée','Amelioration': ''},{'Nom': 'Épée','Amelioration': ''},{'Nom': 'Épée','Amelioration': ''},{'Nom': 'Bouclier','Amelioration': '+'},{'Nom': 'Bouclier','Amelioration': ''},{'Nom': 'Bouclier','Amelioration': ''},{'Nom' :'Inventaire','Amelioration': ''},{'Nom' :'Inventaire','Amelioration': ''}]
    _MainHero = []
    _defausse = []
    _Pack = []
    Argent = 100
    AmeStamina = 0

    def __init__(self): ## construction du héro
        self.nom= "Hero"
        self.pv = 80
        self._pvMax = 80
        self.defense = 0
        random.shuffle(self._Pack)

    def Action(self,c):
        '''
        Entrée : Liste de monstre du combat
        Action : continue la séléction de carte jusqu'à ce que le joueur finisse son tour
        '''

        self.defense = self.defense//2  #chaque tour la defence est divisée pas deux
        continuer = 1
        Stamina = 3
        Stamina += self.AmeStamina ## ajout des amélioration de stamina 
        self.monstres=c

        if self.monstres.debut_combat==1: ## Initialisation de _Pack et _MainHero à chaque début de combat 
            self._MainHero=[]
            self._Pack=[]
            for i in self._Deck:
                self._Pack.append(i)
            random.shuffle(self._Pack)     ##Mélange de _Pack
            self.monstres.debut_combat = 0 ##sortie du début de combat 
        elif len(self._Pack)==0:           ## remplisage de _Pack quand celui-ci est vide
            self.RefillDeck()
        if self._MainHero==[]:             ##Pioche de cartes
            self.Pioche(5)
        elif len(self._Pack) < 3:
            self.Pioche(len(self._Pack))
        elif len(self._MainHero)<5:
            while len(self._MainHero)<5 :
                self.Pioche(1)


        while continuer == 1:
            cheatcode=0

            print("=============================================================================================\n\n") ##Print des cartes utilisables, des infos du joueurs et des monstres
            print("                                     Choisissez une Carte\n")
            cartes = "fuire - fuit le combat (-40Pv, 60/80 pv requis)\n\n desc - Description des cartes    0 - Finir tour    "

            for i in range(len(self._MainHero)):
                Temp_Mainhero = self._MainHero[i]
                i+=1
                cartes += str(i)         ## Numéro de la position de la carte
                cartes += " - "
                i -= 1
                cartes += Temp_Mainhero["Nom"]  ##Nom de la carte
                if Temp_Mainhero["Amelioration"] == "+":
                        cartes += "+"
                cartes += " ("
                for j in self._BiblioCartes:
                        if Temp_Mainhero["Nom"] == j['Nom'] and Temp_Mainhero["Amelioration"] == "+" and (j['Nom'] == "Inventaire" or j['Nom'] == "Hache de guerre"):
                            cartes += str(j['Stamina']-1)
                        elif j['Nom'] == Temp_Mainhero["Nom"]:
                            cartes += str(j['Stamina'])
                cartes += ")"
                cartes += "    "
                if i == 3:
                    cartes+= "\n"
            cartes += "\n"
            print(cartes)   ##Affichage des cartes
            print("Status :")   ##Affichage status du Héro
            print("PV :",self.pv,"/",self._pvMax,".")
            print("Défense :",self.defense)
            print("Stamina :", Stamina)
            print("Nombre de cartes dans le deck :",len(self._Pack),"/",len(self._Deck),"\n")
            print("Ennemi(s) sur le terrain :")
            Ennemis = ''
            for y in range(len(self.monstres.listeMonstres)):   ##Affichage status des Ennemis
                Ennemis += self.monstres.listeMonstres[y].Nom
                Ennemis += ",  PV : "
                Ennemis += str(self.monstres.listeMonstres[y].Pv)
                Ennemis += ",  Attaque : "
                Ennemis += str(self.monstres.listeMonstres[y].atk[0])
                Ennemis += "~"
                Ennemis += str(self.monstres.listeMonstres[y].atk[1])
                Ennemis += '\n'
            print(Ennemis)

            print("=============================================================================================")

            choix = input()

            ##Les cheat codes en combat
            if choix == "/kill @a":
                print("Une force mystérieusement cubique vous permet de tuer tout les ennemis d'un seul coup\n")
                self.monstres.listeMonstres=[]
                cheatcode+=1
                input()
            elif choix == "iddqd":
                print("God Mode. Vous regagner vos pv et votre défense augmente de 100.")
                self.pv = self._pvMax
                self.defense += 100
                cheatcode+=1
            elif choix == "flowey":
                print("It's kill or BE killed. Vos pv passent à 1, vous perdez également votre défense.")
                self.pv = 1
                self.defense = 0
                cheatcode+=1
            elif choix == "player.setav magicka":
                print("Hey, you. Vous avez choisi de determiner la valeur de votre stamina. C'est un peu de la triche non ? C'est pas très RP.")
                print("Et bah choisissez la valeur alors, et déconnez pas, si vous mettez du text le jeu plante, et ça c'est pas cool:")
                Stamina = int(input())
                cheatcode+=1
                print("Voilà, t'es content maintenant que tu vas rouler le jeu ?")

            ##La description des cartes
            elif choix == "desc":
                cheatcode += 1
                self.description(self._MainHero)
                
            elif choix == "fuire":
                cheatcode+=1
                if self.pv < 60 :
                    print("Impossible de fuir.")
                else:
                    print("Vous utiliser votre technique spécial de fuite pour tuer tout vos adversaires. Vous perdez donc 40pv.\n Vous gagner votre carte, mais pas votre Argent.")
                    self.pv -= 48
                    self.Argent -=50
                    self.monstres.listeMonstres=[]
                    



            ##L'utilisation des cartes
            if cheatcode == 0:

                choix = int(choix)
                if choix == 0:
                    continuer = 0
                elif choix <= len(self._MainHero): ##On Scan chaque cartes pour savoir quoi faire
                    j=0
                    while self._BiblioCartes[j]['Nom']!=self._MainHero[choix-1]['Nom']:
                        j+=1
                    i=self._BiblioCartes[j]
                    cartejouer = self._MainHero[choix-1]
                    if i['Nom'] == cartejouer["Nom"]:

                        if i['Type'] == 'A': ##Si c'est une carte attaque classique
                            if Stamina >= i['Stamina']: ##Test du stamina

                                print('\nAttaquer quel Ennemi : \n')    ##choix de l'attaque des ennemis
                                Ennemis = ''
                                for y in range(len(self.monstres.listeMonstres)): ##Affichage des ennemis
                                    Ennemis += str(y+1)
                                    Ennemis += '- '
                                    Ennemis += self.monstres.listeMonstres[y].Nom
                                    Ennemis += '  '
                                print(Ennemis)

                                ##Application de l'effet
                                monstreAttaque=int(input())
                                if monstreAttaque > len(self.monstres.listeMonstres):
                                    print('Veuiller entrer une valeur valide')
                                else:
                                    if cartejouer["Amelioration"] == "+" and cartejouer["Nom"] == "Épée": ##Si améliorée
                                        self.Attaque(self.monstres.listeMonstres[monstreAttaque-1],i['Dmg']+i['Dmg']//2)
                                        Stamina -= i['Stamina']
                                    elif cartejouer["Amelioration"] == "+" and cartejouer["Nom"] == "Hache de guerre": ##Si améliorée
                                        self.Attaque(self.monstres.listeMonstres[monstreAttaque-1],i['Dmg'])
                                        Stamina -= i['Stamina']-1
                                    else: ##Si non améliorée
                                        self.Attaque(self.monstres.listeMonstres[monstreAttaque-1],i['Dmg'])
                                        Stamina -= i['Stamina']
                                    self._defausse.append(self._MainHero[choix-1]) ##On enlève la carte de la main
                                    del self._MainHero[choix-1]
                            else:
                                print('Stamina insuffisante')


                        elif i['Type'] == 'D': ##Si c'est une carte défense classique
                            if Stamina >= i['Stamina']: ##Test du stamina
                                if cartejouer["Amelioration"] == "+": ##Si améliorée
                                    print(Color.Blue + ' Gain de', i['Défence']+i['Défence']//2, 'défence. Votre défence est de',self.defense + i['Défence']+i['Défence']//2, Color.End)
                                    self.defense += i['Défence']+i['Défence']//2 ##Application de la défense
                                else: ##Si non améliorée
                                    print(Color.Blue + ' Gain de', i['Défence'], 'défence. Votre défence est de',self.defense + i['Défence'], Color.End)
                                    self.defense += i['Défence'] ##Application de la défense
                                Stamina -= i['Stamina'] ##Baisse du Stamina
                                self._defausse.append(self._MainHero[choix-1]) ##On enlève la carte de la main et l'ajoute dans la defausse
                                del self._MainHero[choix-1]
                            else:
                                print('Stamina insuffisante')



                        elif i['Type'] == 'S':  ##Si c'est une autre type de carte (Structure similaire aux autres cartes)

                            if i['Nom'] == 'Inventaire':
                                if cartejouer["Amelioration"] == "+":
                                    if Stamina >= i['Stamina']-1: ##Test du stamina-1, car carte améliorer
                                        if len(self._Pack) < 2:
                                            self.Pioche(len(self._Pack))

                                        else:
                                            self.Pioche(2)
                                        Stamina -= i['Stamina']-1 
                                        self._defausse.append(self._MainHero[choix-1]) ##On enlève la carte de la main et l'ajoute dans la defausse
                                        del self._MainHero[choix-1]
                                    else:
                                        print('Stamina insuffisante')
                                else:
                                    if Stamina >= i['Stamina']: ##Test du stamina
                                        if len(self._Pack) < 2:
                                            self.Pioche(len(self._Pack))

                                        else:
                                            self.Pioche(2)
                                        Stamina -= i['Stamina']
                                        self._defausse.append(self._MainHero[choix-1]) ##On enlève la carte de la main et l'ajoute dans la defausse
                                        del self._MainHero[choix-1]
                                    else:
                                        print('Stamina insuffisante')


                            elif i['Nom'] == 'Soin':
                                if Stamina >= i['Stamina']: ##Test du stamina
                                    if cartejouer["Amelioration"] == "+":
                                        ##Application du soin
                                        self.pv += self._pvMax//2
                                        if self.pv > self._pvMax:
                                            self.pv = self._pvMax

                                        print(Color.Blue + ' Gain de', self._pvMax//2, 'PV. Vos PV sont maintenant à',self.pv,"/",self._pvMax,".", Color.End)
                                    else:
                                        ##Application du soin
                                        self.pv += self._pvMax//4
                                        if self.pv > self._pvMax:
                                            self.pv = self._pvMax

                                        print(Color.Blue + ' Gain de', self._pvMax//4, 'PV. Vos PV sont maintenant à',self.pv,"/",self._pvMax,".", Color.End)
                                    Stamina -= i['Stamina']
                                    del self._MainHero[choix-1] ##On enlève la carte de la main mais pas d'ajout dans la defausse car la carte est consummée
                                else:
                                    print('Stamina insuffisante')


                            elif i['Nom'] == 'Lame cachée' or i['Nom'] == 'Couteau de lancer':
                                if Stamina >= i['Stamina']:

                                    print('\nAttaquer quel Ennemi : \n')        ##Choix de l'ennemi à attaquer
                                    Ennemis = ''
                                    for y in range(len(self.monstres.listeMonstres)):   ##Affichage des ennemis
                                        Ennemis += str(y+1)
                                        Ennemis += '- '
                                        Ennemis += self.monstres.listeMonstres[y].Nom
                                        Ennemis += '  '
                                    print(Ennemis)

                                    monstreAttaque=int(input())
                                    if monstreAttaque > len(self.monstres.listeMonstres):
                                        print('Veuiller entrer une valeur valide')
                                    else:
                                        if i['Nom'] == 'Lame cachée':
                                            if cartejouer["Amelioration"] == "+":
                                                self._MainHero.append({'Nom': 'Couteau de lancer','Amelioration': '+'}) ##Ajout d'une carte 'couteau de lancer' dans la Main(Effet carte améliorée)
                                            self.Attaque(self.monstres.listeMonstres[monstreAttaque-1],i['Dmg'])    ##Attaque de l'ennemi
                                            for m in range(3):  ##Application effet Lame Cachée
                                                    self._Pack.append({'Nom': 'Couteau de lancer','Amelioration': ''}) ##ajout de 3 carte 'couteau de lancer' dans le Pack
                                            Stamina -= i['Stamina']
                                            del self._MainHero[choix-1] ##On enlève la carte de la main mais pas d'ajout dans la defausse car la carte est consummée
                                        if i['Nom'] == 'Couteau de lancer':
                                            if cartejouer["Amelioration"] == "+":
                                                self.Attaque(self.monstres.listeMonstres[monstreAttaque-1],i['Dmg']*2)  ##Attaque l'ennemi
                                            else:
                                                self.Attaque(self.monstres.listeMonstres[monstreAttaque-1],i['Dmg'])    ##Attaque l'ennemi
                                            del self._MainHero[choix-1] ##On enlève la carte de la main mais pas d'ajout dans la defausse car la carte est consummée
                                else:
                                    print('Stamina insuffisante')

                            elif i['Nom'] == 'Méditation':
                                if Stamina >= i['Stamina']:
                                    if cartejouer["Amelioration"] == "+":
                                        Stamina += 3 ##Ajout du Stamina, effet de la carte (+)
                                    else:
                                        Stamina += 2 ##Ajout du Stamina, effet de la carte (+)
                                    del self._MainHero[choix-1] ##On enlève la carte de la main mais pas d'ajout dans la defausse car la carte est consummée
                                else:
                                    print('Stamina insuffisante')



                            elif i['Nom'] == 'Carte blindées':
                                if Stamina >= i['Stamina']:
                                    if cartejouer["Amelioration"] == "+":
                                        self.defense += (i['Défence']+5)*len(self._Pack) ##Ajout de défense * nombre de cartes possédée
                                        print(Color.Blue + ' Gain de', (i['Défence']+5)*len(self._Pack), 'défence. Votre défence est de',self.defense + (i['Défence']+5)*len(self._Pack), Color.End)
                                    else:
                                        print(Color.Blue + ' Gain de', i['Défence']*len(self._Pack), 'défence. Votre défence est de',self.defense + i['Défence']*len(self._Pack), Color.End)
                                        self.defense += i['Défence']*len(self._Pack) ##Ajout de défense * nombre de cartes possédée
                                    Stamina -= i['Stamina']
                                    del self._MainHero[choix-1] ##On enlève la carte de la main mais pas d'ajout dans la defausse car la carte est consummée
                                else:
                                    print('Stamina insuffisante')

                else:
                    print('Veuiller entrer une valeur valide')
            if len(self.monstres.listeMonstres)==0 :
                continuer=0

    def ChoixNouvelleCarte(self):
        '''
        A chaque fin de combat peut choisir parmis 3 carte, 1 carte qui pourra être utilisée plus tard
        '''
        carte_choix=0
        cartes=[]
        temp = ''
        while carte_choix<3:##Séléction au hasard des cartes choisissables
            temp = random.choice(self._BiblioCartes)
            temp = {'Nom':temp['Nom'], "Amelioration": ''}
            if not(temp['Nom'] == 'Épée' or temp['Nom'] == 'Bouclier' or temp['Nom'] == 'Couteau de lancer'):
                cartes.append(temp)
                carte_choix+=1
        choix_carte=1

        while choix_carte==1:  ##Affichage des cartes choisissables
            print("=============================================================================================\n\n")
            print("                        Choisissez une Carte que vous voulez obtenir\n")
            affichage = "desc - Description d'une carte   "
            for i in range(len(cartes)):
                affichage += str(i+1)
                affichage += " - "
                affichage += cartes[i]['Nom']
                affichage += "   "
                if i == 3:
                    affichage+= "\n"
            affichage += "\n\n"
            print(affichage)
            print("=============================================================================================")

            ##Affichage de la bonne description
            choix=input()
            if choix=='desc':
                self.description(cartes)
            else:
                self._Deck.append(cartes[int(choix)-1]) ##Ajout de la nouvelle carte dans le deck
                choix_carte=0   ##Sortie de la boucle


    def description(self,liste):
        '''
        Entrée : Le Hero, la liste des cartes à décrire
        Action : Donne la  descriptions d'une carte donnée
        '''
        continuer_desc=1 ##Boucle qui sert à revenir dans se menue
        while continuer_desc==1:
            print("=============================================================================================\n\n") ##Print des cartes descriptibles
            print("               Choisissez une Carte dont vous voulez connaitre la description\n")
            cartes = "0 - Retour    "
            for i in range(len(liste)):
                Temp_Mainhero = liste[i]
                i+=1
                cartes += str(i)
                cartes += " - "
                i -= 1
                cartes += Temp_Mainhero["Nom"]
                if Temp_Mainhero["Amelioration"] == "+":
                        cartes += "+"
                cartes += " ("
                for j in self._BiblioCartes:
                        if Temp_Mainhero["Nom"] == j['Nom'] and Temp_Mainhero["Amelioration"] == "+" and j['Nom'] == "Inventaire":
                            cartes += "1"
                        elif j['Nom'] == Temp_Mainhero["Nom"]:
                            cartes += str(j['Stamina'])
                cartes += ")"
                cartes += "    "
                if i == 3:
                    cartes+= "\n"
            cartes += "\n\n"
            print(cartes)
            print("=============================================================================================")

            choix_desc=int(input()) ##choix de la carte
            if choix_desc == 0:
                continuer_desc=0
            elif choix_desc <= len(self._MainHero): ##Affichage de la bonne description
                j=0
                while self._BiblioCartes[j]['Nom']!=self._MainHero[choix_desc-1]['Nom']:
                    j+=1
                print(self._BiblioCartes[j]['Description'])
                if self._MainHero[choix_desc-1]['Amelioration'] == '+':
                    print("\nAmélioration :",self._BiblioCartes[j]["DescAmélioration"])
                print("\n\nAppuyer sur entrée pour continuer\n")
                input()

    def Pioche(self,nbcarte):
        '''
        Entée: valeur(x), liste
        Action: rajoute 'x' carte dans la main du hero
        '''
        i=0
        while i!=nbcarte:
            self._MainHero.append(self._Pack[0])    ##Pioche première carte du Pack (Pack mélanger préalablement)
            del self._Pack[0]
            i+=1


    def RefillDeck(self):
        '''
        Entée: self
        Action: Remet les carte déffausser dans le pack (donc les rend rejouable)
        '''
        self._Pack=self._defausse   ##La defausse est vidée dans le Pack
        self._defausse=[]
        random.shuffle(self._Pack)      ##Mélange de _Pack

    def Attaque(self,cible,dmgDealt):
        '''
        Entée: Hero, la cible, et les dégat à effectuer
        Action: attaque un adversaire
        '''
        if cible.Pv + cible.defense > dmgDealt :##Si la cible peut survivre
            if cible.defense > dmgDealt : ##Si sa défense est suffisante
                cible.defense -= dmgDealt
            else: ##Si sa défense est insuffisante
                dmgDealt -= cible.defense   ##On retire des dégats la défence 
                cible.defense = 0   
                cible.Pv -= dmgDealt ##On inflige les domages
            print("\n",Color.Blue + "---- ", cible.Nom, "à perdu ", dmgDealt, "pv. Il lui reste", cible.Pv, "pv."+Color.End)
        else : ##Si la cible meurt
            cible.Pv = 0
            print(Color.Blue + "\n---- ", cible.Nom, "à été vaincu après avoir recu", dmgDealt,'de dégat', Color.End)
            self.monstres.listeMonstres.remove(cible) ##On enlève la cible de la liste des monstres


class Ennemi:
    '''
    Entrée : str
    Action : suivant le str (nom de l'ennemis) donné crée un monstre avec vie aléatoire
    '''
    ## Liste de tout les monstres du jeu
    _BiblioMonstres = [{"Nom":"Slime","Vie":(12,20),"Atk":(5,10)},{"Nom":"Gobelin","Vie":(25,40),"Atk":(10,15)},{"Nom":"Orc","Vie":(35,50),"Atk":(15,25)},{"Nom":"Gardien de la porte","Vie":(150,200),"Atk":(30,50)},{"Nom":"Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞","Vie":(500,1000),"Atk":(50,70)}]

    def __init__(self, nom):    ##construction des monstres
        i = 0
        while self._BiblioMonstres[i]["Nom"] != nom:
            i += 1
        self.Nom = self._BiblioMonstres[i]['Nom']
        self.Pv = self._SetPvMax(self._BiblioMonstres[i]['Vie']) ##choix aléatoire de la vie du monstre
        self.atk = self._BiblioMonstres[i]["Atk"]  ##L'attaque est sous forme de fourchette et le monstre fera toujour des dégats différent dans celle-ci
        self.defense = 0


    def _SetPvMax(self,fourchetteDeVie):
        '''
        Entrée : le mob, sa fourchette de vie
        Action : Définition des pv du mob
        '''
        pvmax = random.randint(fourchetteDeVie[0],fourchetteDeVie[1])     ##Choix aléatoire de la vie du monstre
        return pvmax

    def Attaque(self, cible):
        '''
        Entrée : le mob, le Hero
        Action : Attaque le Hero
        '''
        self.dmgDealt = random.randint(self.atk[0],self.atk[1]) ##Définition des dégats selon la fourchette donnée avec le mob dans _BiblioMonstres
        temp= self.dmgDealt
        if cible.pv + cible.defense > self.dmgDealt : ##Si le hero peut survivre
            if cible.defense > self.dmgDealt : ##Si la défense du héro est suffisant
                cible.defense -= self.dmgDealt
                print(Color.Red + "\n---- ", cible.nom, "à perdu ", self.dmgDealt,"de défense suite à l'attaque de", self.Nom, ". Il vous reste", cible.defense,"points de défense." +Color.End)
                print("Pressez Entrée pour continuer le combat")
            else: ##Si la défense du héro est insuffisante
                self.dmgDealt -= cible.defense
                cible.defense = 0
                cible.pv -= self.dmgDealt
                print(Color.Red + "\n---- ", cible.nom, "à perdu ", self.dmgDealt,"pv suite à l'attaque de", self.Nom, ". Il vous reste", cible.pv,"/", cible._pvMax, "pv "+Color.End)
                print("Pressez Entrée pour continuer le combat")

        else : ##Si le hero ne peut survivre
            cible.pv = 0


    def Infos(self):
        print(Color.Bold + "\n---- ", self.Monstre["Nom"], "(PV : ", self.pv, " / ", self.pvmax, " ; ", " ATK : ", self.atk, ")"+Color.End)

class Combat:
    '''
    Entrée: liste d'ennemis ; Hero
    Action: commence un combat avec les monstres préciser dans la liste jusqu'à victoire ou défaite
    '''
    listeMonstres=[]

    def __init__(self,monstres,h):  ##construction du combat
        self.listeMonstres = monstres 
        self.h = h
        self.pv_pour_sauv = h.pv ##Variable qui sert pour remettre (et ajouter un peu) de pv en cas de mort

    def BoucleCombat(self):
        self.debut_combat = 1   ##Varible permetant ensuite d'initialiser le combat seulement lors du premier tour
        while self.listeMonstres!=[] and self.h.pv>0:   ##Si il y a encore des monstres en vie ou que le Héro est encore en vie
            self.h.Action(self)   ##Tour du Héro
            for i in self.listeMonstres:    ##Tour du/des ennemis
                i.Attaque(self.h)
                input()
        if self.h.pv<=0:    ##Condition de défaite
            print("Défaite ! Les Ennemis vous ont vaicus. Vous recommencez le combat avec 50 pourcents de vie en plus. Pressez Entrée")
            input()
            self.h.pv = self.pv_pour_sauv + ((self.h._pvMax - self.pv_pour_sauv)//2)
            return False
        else:           ##Condition de victoire
            print("\nVitoire ! Tous les Ennemis ont été vaicus.")
            print("Status de fin de combat",self.h.pv,"/",self.h._pvMax,".\nVous remporter 50 d'Argents.\nVous regagnez 8 PV.\n---------------------------------------------------------------------------------------------\n\n")
            self.h.Argent += 50 ##Ajout d'argent
            self.h.pv+=8
            if self.h.pv > self.h._pvMax:
                self.h.pv = 80
            input()
            self.h.ChoixNouvelleCarte() ## Choix d'une nouvelle carte à ajouter dans le deck
            return True
        

