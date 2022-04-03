from Combat import *
from camp import *
from magasin import *
class Jeu:
    ## Attribut statique nécéssaire au bon fonctionnement du jeu (notamment l'histoire)
    h = Hero()
    histoire1 = [". (appuyez simplement sur entrer pour passer au dialogue suivant)", "....", "...hmm...", "** J'ouvre les yeux **", "** Je me trouve dans un endroit qui m'est complétement inconnue **", "Hero :\nMais, où suis-je ? Comment je suis arrivé là ?", "** C'est un endroit très lugubre où je suis, on croirait presque une salle de jeux vidéos. Enfin là, un jeu vidéo vachement flippant, vu le décors **", "** Il y a des tâches rouges sur le murs, je n'ôse même pas s'avoir ce que c'est **", "** J'avoue que je commence à avoir peur **", "...", "Hero : \nBon, pour l'instant, essayons de rester calme, c'est pas en m'affolant que je vais réussir à trouver une sortie.", "** En me redressant, je sens un certain poids sur mon bras droit, je le regarde **", "Hero : \nUne machine ? Des cartes ? Qu'est ce que c'est que tout ça ?", "??? : \n...hmm...", "** ????. J'entends une voix de petite fille juste à côté de moi, comme si elle était en train de se réveiller. Je tourne la tête **", "** Une petite fille, qui à l'air d'avoir à peu près 8 ans, en train de dormir **", "Hero : \nQue fait une petite dans ce genre d'endroit ? Enfin... moi non plus je sais pas pourquoi je suis ici...", "** Je décide de tenter de la réveiller **", "Hero : \nEh petite, eh !", "??? : \n...hmm?", "Hero : \nAh, tu te reveille.", "** Elle se lève puis regarde un peu partout autour d'elle, puis prend peur d'un seul coup. Elle se met à pleurer **", "??? : \nQui êtes vous ?! Qu'est-ce que je fais ici ?! J'ai peur....", "Hero : \nEh eh, calme toi. Moi non plus je ne sais pas pourquoi nous sommes ici.", "** Je tente de m'approcher d'elle. Elle me rejette **", "??? : \nN'approchez pas !", "** Elle recule **", "** Je tente de la suivre pour clarifier la situation. Puis d'un coup, je tombe de frayeur **", "Hero : \nQu'est ce que c'est que ça ??", "** Un monstre, comme on pourrait en voir dans un jeu vidéo. Devant mes yeux **", "** Le monstre cours, tente d'attaquer la petite. Je me lève... **", "Hero : \nAttention petite !", "** ...Puis fonce sur elle pour la faire éviter l'attaque **", "** Le monstre fonce donc à toute vitesse sur moi **", "Hero : \nHein ? Que se passe-t-il ?", "** La machine sur mon bras se met à briller ?! **", "Hero : \nAaaaaaaaah!"]
    histoire2 = ["Hero : \n....", "Hero : \n*essoufler* Qu'est ce qu'il vient de se passer là ?", "** Vraiment, c'est quoi ces cartes ? Enfin, je verrai ça plus tard, il y a plus important. Je tourne la tête **", "Hero : \nPetite, tout va bien ? ", "** Toujours effrayée, elle me dit simplement qu'elle va bien grâce à un hochement de tête **", "Hero : \nTant mieux ! Sinon, est-ce que je peux de demander ton prénom ?", "** Je veux pas qu'elle ai peur de moi (ce qui est tout de même logique au vu de la situation), alors j'essai d'être le plus gentil possible **", "Emily : \nE... Emily.", "Hero : \nJe vois, Emily! C'est vraiment un joli nom !", "Emily : \n... Et vous ?", "** ... **", "** ??? **", "** C'est vrai, comment je m'appelle ? Je ne m'en souvien même plus ! **", "** D'ailleurs, je ne me souvien même plus de ce que je faisais avant d'attérir ici. **", "** .... Ça commence beaucoup m'inquiéter toute cette histoire, quoique je trouve que j'arrive à rester bien calme **", "** Enfin, j'ai pour l'instant plus important à faire que retrouver ma mémoire, protéger Emily **", "** Après tout, elle ne peut pas se battre, enfin en tout cas, elle n'a pas la petite machine à cartes, je suis donc le seul à pouvoir nous défendre **", "** Mais attends, elle vient de me poser une question, je lui répond quoi du coup ? **", "** Bah, inventer un nom serai pas très gentil je trouve, autant dire la vérité **", "Hero : \nJe ... ne me souviens pas de mon nom... ni même de mon passé.", "Emily : \nJe vois...", "Hero : \nBref, tu peux m'appeler comme tu v...", "** D'un seul coup, j'entends un bruit derrière moi, je me retourne **", "Hero : \nEncore un monstre... nan, plusieurs ??", "** Y'a pas à dire, ils font vraiment peur ces monstres, mais je dois protéger Emily **", "Hero : \nEmily, cache toi derrière moi, je vais vaincre ces monstres", "Emily : \nOk..", "** Je m'en doutais, elle a encore un peu peur de moi. Enfin, elle se cache tout de même derrière moi, donc j'imagine que les monstres lui font encore plus peur **", "Hero : \nAllez, amenez-vous !", "** Y'a pas à dire, ils font vraiment peur ces monstres, mais je dois protéger Emily **"]
    histoire3 = ["Hero : \nPfiouu, c'était beaucoup plus compliqué cette fois.", "** Bon, je fini sans trop de dégats, alors ça va **", "Hero : \nEmily, tout vas bien pour toi ?", "Emily : \nOui, tout vas bien pour moi.", "** Tiens, elle m'as répondu avec une voix beaucoup plus sûre d'elle, où du moins, elle ne semble plus effrayer **", "(Bruit de porte mécanique qui souvre (criant de réalisme))", "** Nous deux nous retournons immédiatement **", "Hero : \nUne porte ? Il y avait donc une sortie.", "** Enfin, on ne sait pas où cette porte mène, donc il vaut mieux faire attention **", "Hero : \nEmily, on va y aller. Restes bien derrière moi.", "Emily : \nMmh", "** On franchi la porte, et après à peine quelques mètres, on tombe sur... **", "Emily : \nUn feu de camp ?", "Hero : \nÇa me surprend aussi, je pensais qu'on tomberai sur quelque chose de plus horrible, genre des monstres.", "Emily : \nOn peut aller s'y reposer ou pas ? Je me sens fatigué après toutes ces histoires...", "Hero : \nEt bien, je dois bien avouer que je me sens aussi fatigué. Mais je ne sais pas si on peut faire confiance à ce feu de camps", "Emily : \nDonc on ne peut pas ?", "** Elle me fait en ce moment une espèce de moue. Comment veut-elle que je dise non si elle fait une tête si mignone ??? **", "** Bon, elle doit sûrement être encore plus fatigué que moi **", "Hero : \nBon, allons-y, mais il faut qu'on reste sur nos gardes, d'accord ?", "Emily : \nD'accord !", "** Et sur ceci, nous décidons de rester se reposer à ce camps **"]
    histoire4 = ["Hero : \nDit moi Emily, est-ce que tu te souviens de ce que tu faisais avant de te retrouver ici ?", "Emily : \nChetai en trchain d'aller dormir.", "** Me répond-t-elle en mangeant en même temps de la nourriture trouvé près du feu (que j'ai évidemment tester avant elle) **", "Hero : \nTu pourrais au moins finir ce que t'as dans ta bouche avant de me répondre...", "Emily : \nAh oui pardon. Je disais, je me préparais à aller dormir.", "Hero : \nTu étais chez toi ?", "Emily : \nOui.", "** Elle me répond cela d'un ton un peu sec, je décide donc de lui poser la question suivante : **", "Hero : \nTu me parrais franchement calme malgré la situation dans laquelle on est, tu es sûr que tout va bien", "Emily : \nNon ça ne va pas du tout, je suis extrêmement apeurée, mais j'essaie de rester calme le plus possible, comme tu le fait", "** Dit donc, c'est qu'elle est forte la petite pour rester à arriver calme malgré tout ça **", "Emily : \nEt je me dit que ça n'est pas en étant morte de trouille que j'arriverai à sortir, déjà que je ne peux pas me battre...", "Emily : \nJe ne serai qu'une gêne pour toi sinon....", "Emily : \nJe ne veux pas que tu m'abandonne dans cette endroit.... *sob*", "Emily : \nJe ne veux juste le plus vite possible revoir mes parents, ma famille.... *sob**sob*", "Emily : \nJ'ai peur...", "Emily : \nJ'ai vraiment peur...", "** Ok, elle se met à pleurer. J'aurai peut-être pas du lui poser cette question, je pense que c'était trop **", "Hero : \nTu sais, je ne compte pas t'abandonner ici, je serais franchement un connard si je faisais.", "Hero : \nAu contraire, j'ai décidé de te protéger et de tout faire pour que tu puisse sortir d'ici.", "Hero : \nJe ferai en tout cas de mon mieux pour.", "Hero : \nAlors n'ai pas peur.", "** Moi ça va, après tout j'ai perdu la mémoire, mais pour elle, ça doit être extrêment dur tout ce qui se passe **", "Hero : \nEt puis, ne dit pas que tu sert à rien. Sans toi, je me serai sûrement laisser mourrir ici. Tu m'as donnée une raison de me battre pour sortir, alors je te remercie.", "Emily : \n*sob* C'est vrai ? Tu m'abandonneras pas ?", "Hero : \nNon, hors de question de je fasse ça.", "** Elle essuie ses larmes avec ces mains **", "Emily : \nDites Monsieur, comme vous ne vous souvenez pas de votre prénom, est-ce que je peux vous appeler 'Hero'", "Hero : \n'Hero' ???", "Emily : \nBah oui ! Après tout, vous faites tout pour me sauver, vous êtes un Héro donc !", "** Ça serait quand même super prétentieux de ma part d'accepter ce nom **", "** Mais bon c'est quand même de s'appeler comme ça, et ça donne un côté mystérieux, alors autant accepter **", "Hero : \nAppelle moi comme tu veux !", "** Dit-je donc sans cacher ma fierté **", "Emily : \nMh !", "** Et finalement, après tout ça, elle s'endormit près du feu **", "Hero : \nJe te ramènerai chez toi Emily, coûte que coûte, ne t'inquiètes pas.","** Puis peut après... **","Hero : \nC'est bon, tu es réveiller ?","Emily : \nEt en pleine forme !","Hero : \nTant mieux ! Mais moi aussi j'aimerai bien dormir, réveille moi si il y a un problème.","Emily : \nAh, euuh, ok !","** Puis je dormis... **","Hero : \nOk, repartons et sortons d'ici le plus vite possible."]
    histoire5 = ["Hero : \nUn Gobelin?? Franchement, je commence à me demander si on est encore sur Terre.", "** En disant ça, le visage d'Emily se crispe... **", "Hero : \nEnfin, je n'en sait rien. Ne t'inquiète pas, ça doit juste être un coup monté par quelqu'un.", "** ...Puis de soulage un peu **", "Emily : \nEt bien, j'espère que tu te trompe...", "Hero : \nOui, moi aussi.", "Hero : \nBon, continuons."]
    histoire6 = ["Emily : \nOn dirait que ça devient de plus en plus dur, tout vas bien ?", "Hero : \nOuai, t'en fais pas pour moi, je vais tenir le coup, je le dois.", "Emily : \nOn peux s'arrêter et faire une pause hein.", "Hero : \nNan, je peux encore continuer, il faut qu'on sorte d'ici le plus vite possible.", "** Elle a l'air inquiète, mais on ne peut vraiment pas rester ici plus longtemps, après tout, on ne siat même pas où se trouve la sortie **", "Hero : \nContinuons.", "Emily : \nSi tu dis que tout vas bien, alors...", "Emily : \nTiens, c'est quoi ça là-bas ? Une personne ? Sur un tapis ?", "??? : \nACHETEEEEZZZZ!", "Emily : \nAH!", "** Elle poussa un petit crie de peur, elle ne s'attendait sûrement pas à une voix aussi effrayante **", "Hero : \nQu'on achète ? Vous êtes un vendeur ? Quesque vous faites ici ?", "Vendeur : \nPAS IMPORTAANT, ACHTEEEZ!", "** Emily ce cache encore dérrière moi **", "Hero : \nPas beaucoup de vocabulaire hein... Vous vendez quoi ? Et je dois utiliser quoi pour acheter, les petites pièces que j'ai eu en combattant ?", "Vendeur : \nACHETEEEEZZZZ!", "Hero : \nOk, vraiment pas envie de parler..; BAh je vais voir ce que vous vendez par moi même alors. Emily, reste loin, on sait jamais."]
    histoire7 = ["Hero : \nIl était vraiment étrange ce vendeur", "Emily : \nIl faisais surtout très peur...", "Hero : \nOuai, ça c'est vrai, mais bon, j'ai pu acheter plein de trucs qui nous seront sûrement utile pour la suite.", "Emily : \nOui, ça devrais mieux se passer maintenant, du moins je l'espère...", "** Des ennemis approchent **", "Hero : \nBon, bah on va voir ça.", "** Je devrais peut-être moins m'enflammer, ça pourrais être dangeureux **"]
    histoire8 = ["** Un Orc ?? Je commence vraiment à croire qu'on est pas sur Terre... Mais bon, je vais pour l'instant éviter de parler de ça à Emily **", "** Et les Ennemis deviennent vraiment de plus en plus fort **", "** Je commence vraiment à me demander si on va réussir à sortir d'ici **", "** Mais bon, j'ai promis à Emily qu'on sortirai, alors je vais faire de mon mieux **"]
    histoire9 = ["Emily : \nCe combat avais vraiment l'air compliqué, tu es sûr de ne pas vouloir te poser ?", "Hero : \nNan t'inquiètes vraiment pas, je vais bien.", "** Bon en fait je vais pas très bien, fin je suis vraiment fatigué **", "Emily : \nSi je te dit ça, c'est parce que je vois un feu de camp au loin.", "Emily : \nJe le vois bien que tu es fatigué, repose toi, ne t'en fait pas pour moi.", "Hero : \nÇa se voit tant que ça? Bon, posons nous alors...", "Emily : \nBien ! On ne sortira pas si tu es trop fatigué.", "** Oui, elle n'a pas tort... Sans elle je serai sûrement vraiment déjà mort **", "Emily : \nAller, dors. Je vais surveiller.", "Hero : \nOk, reveille moi si il y a quelque chose."]
    histoire10 = ["Hero : \n...hm...", "Emily : \nAh, tu te reveille.", "Hero : \n...Bonjour Emily... Enfin, je ne sais même pas si il fait jour ou pas...", "Emily : \nTu te sens mieux maintenant ?", "Hero : \nOuai beaucoup mieux, je ne suis plus fatigué. On va pouvoir repartir après avoir manger", "Emily : \nOk, n'en fait pas trop cette fois-ci, ok ?", "Hero : \nOuai t'inquiètes, j'ai compris mon erreur.", "** Puis nous mangeâmes **", "Hero : \nOk, on reprend la route !"]
    histoire11 = ["Hero : \nTrois ennemis, c'est presque de la triche ça !", "Emily : \nHa ha ha, je dois dire que je suis impressionée que tu arrive à dire ce genre de phrase dans ce genre de situation.", "Hero : \nToi aussi, tu était beaucoup moins *joyeuse* au début. Enfin, si on peut être joyeux ici...", "** Puis elle pris peur **", "Hero : \nQue se passe-t-il ?", "** Ahhh, je comprend maintenant **", "Hero : \nEncore vous, comment vous avez fais pour arriver ici avant nous ?", "Vendeur : \nACHETEEEZ", "Hero : \nOui oui je sais, je dois acheter oui.", "Hero : \nEt bien, voyons voir ce qu'il y a à vendre."]
    histoire12 = ["Hero :\n Au revoir !","Emily : \nHmm?", "Hero : \nQue se passe-t-il ?", "Emily : \nJ'ai senti un courant d'air... Ça m'a un peu surprise.", "Hero : \nEhh, c'es très bon signe ça.", "Emily : \nPourquoi ?", "Hero : \nParce que ça veut dire qu'on approche de la sortie.", "Emily : \nVraiment ?", "Hero : \nVraiment !", "Emily : \nYoupiii !", "** Elle se met à sauté de joie un peu partout **", "Hero : \nOk, sortons d'ici le plus vite possible !", "Emily : \nOuai !", "** Elle à vraiment l'air heureuse. Je suis content, on va pouvoir sortir **"]
    histoire13 = ["Hero : \nMe gêner pas les monstres, je veux vite sortir.", "Emily : \nAttention Hero, y'en a d'autres.", "Hero : \nSerieux ?... Bon, bah vener vous battre !", "Emily : \nN'en fait pas trop !", "Hero : \nOuai t'inquiètes ! Vous, venez là !"]
    histoire14 = ["Hero : \nC'est bon, y'a plus d'adversaire ?", "Emily : \nJ'en vois aucun moi.", "Hero : \nEt bah, y'en avait beaucoup, on va enfin pouvoir réavancer", "** Puis la routine, Emily se crispe **", "Hero :\nLe magasin j'imagine... Comment tu fais pour le sentir d'aussi loin ?", "Hero :\nBref, allons le voir... Attend, y'a aussi un feu de camp ? C'est la salle avant le boss ou quoi ?", "Emily : \n...", "Hero : \nBon, tu peux aller te reposer, moi je vais aller marchander. Je te rejoindrai après, ok ?", "Emily : \nhm."]
    histoire15 = ["Hero : \nC'est bon, tu t'es reposée, on peut y aller ?", "Emily : \nOui !", "Hero : \nAlors avançons !", "** Puis après quelques minutes de marches, nous arrivons devant une porte **", "Emily : \nAlors c'est bon, on va pouvoir sortir, enfin ?", "Hero : \nIl n'y a qu'un seul moyen de la savoir.", "** Avec le sourrire aux lèvres, on ouvre la porte... **", "** ...Pour au final être déçus **", "Hero : \nUne autre porte ? Et... Une statue ?", "Emily : \nJe croyais qu'on allais enfin pouvoir s'en aller.... ?", "** Dit-elle au bord des larmes **", "Hero : \nAttends, il y a une autre porte, essayons de l'ouvrir", "** Mais en s'en approchant... **", "kriii", "Hero : \nLa statue... Bouge ?", "** Emily se cache **", "** La machine sur mon bras se met à briller **", "Hero : \nQuoi ?? Je vais devoir combattre ce gros machin ??? Serieux ???", "** Ok, la j'ai peur pour ma vie **", "Hero : \nVraiment ??", "** Puis je me rapelle de manière pas très cliché la promesse que j'ai fait avec Emily **", "Hero : \nOk... Viens là !!!"]
    histoire16 = ["Hero : \n*respirations fortes**respirations fortes* Enfin... Ça veut dire qu'on va pouvoir sortir, enfin ?", "Emily : \nHerooo !", "** Puis elle me fait un câlin, elle doit être vraiment heureuse **", "Hero : \nOn va pouvoir sortir Emily !! Enfin !", "Emily : \nhm!!", "** Elle pleure, mais de joie **", "Hero : \nOk, allons ouvrir cette fichu porte et sortir de ce fichu endroit", "** On s'approche de la porte **", "Emily : \nHero ! On ouvre en même temps la porte, ok !", "Hero : \nOuai ça marche !", "Tout les deux : \n Un.. Deux.. Trois !!", "** Enfin, on peut maintenant sentir la lumière du soleil et le vent dans nos cheveux **", "** Nous sommes dehors, mais il y a un problème **", "Hero : \nOù sommes nous, c'est quoi cette endroit ??", "** Emily prend une tête terrorisée **", "** Des plantes inconnus, des animaux inconnus au loin **", "** Une chose est sûr... **", "** ...Nous ne sommes pas sur Terre. Nous sommes dans un autre monde... **", ".....", "...", "Monsieur, merci d'avoir jouer à notre jeu, on espère qu'il vous a plu un minimum, et qu'il n'y a pas eu trop de problème.\n On espère aussi que vous avez aimé le peu d'histoire qu'on a mis, avec 2 semmaines, développer un histoire complète est quasiment impossible.\n Encore merci d'avoir jouer. On se revoie en cours. Au revoir Monsieur", "Appuyez sur Entrée pour fermer le jeu."]

    def __init__(self):
        self.case = 0

    def CaseCombat(Ennemis, h):
        '''
        Entrée : Liste de monstre du combat puis le Hero
        Action : Lance le combat puis le boucle tant que le combat n'est pas remporté
        '''
        print("Vous rencontrez des ennemis !")
        Cresult = False
        while Cresult == False:
            EnnemisListe = []
            for i in Ennemis: ##Remise des PV des Ennemis à leurs état d'origine en cas de défaite
                EnnemisListe.append(Ennemi(i))
            C = Combat(EnnemisListe,h)
            Cresult = C.BoucleCombat()

    def histoire(self):
        '''
        Action : Lis l'histoire, lance les combats, les camps, etc... C'est un peu la colonne vertebrale du jeu. 
        '''
        longhist1 = len(Jeu.histoire1)
        i=0
        while self.case == 0 and i+1 <= longhist1:
            print(Jeu.histoire1[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 1
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 1

        Jeu.CaseCombat(["Slime"],Jeu.h)

        longhist2 = len(Jeu.histoire2)
        i=0
        while self.case == 1 and i+1 <= longhist2:
            print(Jeu.histoire2[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 2
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 2
        
        Jeu.CaseCombat(["Slime", "Slime"],Jeu.h)

        longhist3 = len(Jeu.histoire3)
        i=0
        while self.case == 2 and i+1 <= longhist3:
            print(Jeu.histoire3[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 3
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 3
        
        camp.choix(Jeu.h)

        longhist4 = len(Jeu.histoire4)
        i=0
        while self.case == 3 and i+1 <= longhist4:
            print(Jeu.histoire4[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 4
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 4

        Jeu.CaseCombat(["Gobelin"],Jeu.h)

        longhist5 = len(Jeu.histoire5)
        i=0
        while self.case == 4 and i+1 <= longhist5:
            print(Jeu.histoire5[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 5
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 5

        Jeu.CaseCombat(["Gobelin","Gobelin"],Jeu.h)
        
        longhist6 = len(Jeu.histoire6)
        i=0
        while self.case == 5 and i+1 <= longhist6:
            print(Jeu.histoire6[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 6
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 6

        magasin.choix(Jeu.h)

        longhist7 = len(Jeu.histoire7)
        i=0
        while self.case == 6 and i+1 <= longhist7:
            print(Jeu.histoire7[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 7
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 7
        
        Jeu.CaseCombat(["Orc"],Jeu.h)

        longhist8 = len(Jeu.histoire8)
        i=0
        while self.case == 7 and i+1 <= longhist8:
            print(Jeu.histoire8[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 8
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 8

        Jeu.CaseCombat(["Orc","Gobelin"],Jeu.h)

        longhist9 = len(Jeu.histoire9)
        i=0
        while self.case == 8 and i+1 <= longhist9:
            print(Jeu.histoire9[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 9
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 9

        camp.choix(Jeu.h)

        longhist10 = len(Jeu.histoire10)
        i=0
        while self.case == 9 and i+1 <= longhist10:
            print(Jeu.histoire10[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 10
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 10
        
        Jeu.CaseCombat(["Orc","Gobelin","Slime"],Jeu.h)

        longhist11 = len(Jeu.histoire11)
        i=0
        while self.case == 10 and i+1 <= longhist11:
            print(Jeu.histoire11[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 11
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 11

        magasin.choix(Jeu.h)

        longhist12 = len(Jeu.histoire12)
        i=0
        while self.case == 11 and i+1 <= longhist12:
            print(Jeu.histoire12[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 12
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 12

        Jeu.CaseCombat(["Orc","Gobelin"],Jeu.h)

        longhist13 = len(Jeu.histoire13)
        i=0
        while self.case == 12 and i+1 <= longhist13:
            print(Jeu.histoire13[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 13
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 13

        Jeu.CaseCombat(["Orc","Orc"],Jeu.h)

        longhist14 = len(Jeu.histoire14)
        i=0
        while self.case == 13 and i+1 <= longhist14:
            print(Jeu.histoire14[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 14
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 14

        camp.choix(Jeu.h)
        magasin.choix(Jeu.h)

        longhist15 = len(Jeu.histoire15)
        i=0
        while self.case == 14 and i+1 <= longhist15:
            print(Jeu.histoire15[i])
            inp = input()
            if inp == "p":
                print ("\nVous avez passé la scène\n")
                self.case = 15
            if inp == "Monika":
                print("JustTͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞")
                Jeu.CaseCombat(["Tͣͯ̒̽̈́̈́̓̇͏̤̥̼̖͔͔̤͈͟ỡ̎̉͏͚̝̼̪̟͎̘ ̘̱̭̘̠͔̤̫͖̏í̷͓̣̣͇͒̓̔̄ͩͅn̷̼̲̼͎̘͕͚͕ͯͨ͘v̴̹̲̔ͯ͒̅ͩ͛͑́̚͞"],Jeu.h)
            i+=1
        self.case = 15

        Jeu.CaseCombat(["Gardien de la porte"],Jeu.h)

        longhist16 = len(Jeu.histoire16)
        i=0
        while self.case == 15 and i+1 <= longhist16:
            print(Jeu.histoire16[i])
            inp = input()
            i+=1

        print("Vous avez fini le jeu")
        input()




