# Rolling-At-All-Cost
## Type de projet 
Jeu vidéo de **plateformes** en **auto-scroller**, où les mouvements de la caméra contraignent les déplacements du joueur. 
## Scénario
Pour l'instant il n'y en a pas.

## Gameplay
Lors d'un niveau, le joueur est mis aux commandes d'un véhicule parmi **deux** (d'autres pourraient être ajoutés dans le futur) :  
**Sauteroule :** Une petite voiture inspirée d'une Wolkswagen beetle et d'une sauterelle. Elle avance en ligne droite, ne supporte pas d'être frappée par des obstacles ou de se coincer contre des plateformes. Pour éviter toute inconvénience, pressez la touche "flèche du haut" lui permet de sauter. Laisser le bouton enfoncé permet de sauter à répétition.  
**Boing Boeing :** Un petit avion inspiré d'un avion Boeing et d'un condor noir. Celui ci permet d'explorer l'écran dans son ensemble. Appuyer sur "flèche du haut" lui donne un léger coup de boost vers le haut, lâcher le bouton le fait redescendre. Appuyer à répétition sur le bouton permet de monter plus vite, et même de rester sur du vol en ligne droite. Laisser le bouton enfoncé le fait monter jusqu'à qu'il soit lâché. Contrairement à la Sauteroule, tomber sur la route principale lui fait des dégât, et monter trop haut le tue, pour éviter qu'il ne quitte la caméra.

## Navigation 
### Écran de connexion
Un écran possédant un bouton "connexion", et un bouton "créer". Dessous chaque bouton est présent un champ de texte ne pouvant accueillir que 12 caractères maximum. Cliquer sur un champ de caractère l'active et vous permet d'écrire dedans. Écrire dans le champ "créer", puis appuyer sur le bouton du même nom va créer un enregistrement dans notre base de données, avec un ID aléatoire, votre pseudo (à retenir pour de futures connexions), et un compte tout neuf prêt à être rempli par vos exploits, en plus de vous envoyer vers l'**écran d'accueil** . Écrire dans le champ "connexion", puis appuyer sur le bouton du même nom va vous permettre de vous connecter à un compte déjà créé et reprendre votre progression. Si le compte n'existe pas, un message d'erreur s'affiche, et vous pouvez tenter à nouveau de vous connecter dans quelques secondes. Notez qu'appuyer dans un champ de texte supprime ce que vous avez écris dans l'autre.  
⚠️**Attention** : Les caratères non reconnus par la police de caractère utilisée ne s'afficheront pas, mais seront enregistrés avec le reste. Cela s'applique aussi aux appuis de boutons n'ayant pas d'effet sur le texte. Exemple : la touche "Enter", qui si elle est pressée, devra être renseignée à chaque connexion comme faisant partie du mot de passe. Un moyen idéal de sécuriser son pseudo/mot de passe, mais aussi perturbant pour des maneuvres rapides. 

### Écran d'accueil 
Cet écran est le hub central du jeu. Il contient de nombreux boutons.  
**Mode histoire** : Probablement le bouton le plus important, il renvoie l'utilisateur sur le premier monde du jeu (actuellement le seul).  
**Bonus** : Ce bouton renvoie vers un autre écran de sélection, qui permet de s'essayer dans des minis jeux (actuellement un seul fonctionnel).  
**Garage** : Ce bouton renvoie vers le profil du joueur.  
**Quitter** : Ce bouton permet de fermer la page Pygame. Idéal lorsque l'on joue en grand écran sans avoir accès à la croix. Notez que la base de données sauvegarde toutes les données instantanément, il n'y a donc pas de sauvegarde requise avant de quitter.  
**Paramètres** : Ce bouton renvoie vers une liste de paramètres aussi accessibles via l'écran de connexion. Le joueur peut choisir d'éteindre la musique du jeu ou de la rallumer, le cas échéant. Il peut aussi changer de langue (entre le français, l'allemand et l'anglais) pour les écrans de navigation.  

### Monde 1 : Atoll Atellage
Le premier monde du jeu, ressemble à une petite île paradisiaque... ou presque ! Entre industries, travail du bois, commerce et tourisme, on n'est pas prêt de s'ennuyer ici ! Chaque niveau est représenté par une puce rouge, placée à coté du décor étant un avant goût du thème du niveau. La puce en forme d'étoile serait là pour accueillir un boss, bien que pour l'instant, il n'en est rien ! Les niveaux sont numérotés de haut en bas en partant de la gauche.  
**1 - Intrusion Industrielle (ébauche à peine commencée) :** Roulez à travers une usine en pleine production. Ne vous faites pas écraser par une presse hydraulique !  
**2 - Assaut Sonore (ébauche bien avancée) :** Volez au dessus d'un concert déjanté, car les spectateurs vont vous en faire un fête ! Et attention aux fausses notes...  
**3 - Embûches Bucheronnes (pas encore commencé) :** Roulez au milieu des troncs et des scies de cette scierie à l'activité élevée !  
**4 - Grande Fuite (globalement fini) :** Un parc d'attraction c'est censé être sécurisé, et pourtant montagnes russes et grandes roues vous mettrons des bâtons dans les ailes !  
**5 - Écueils Caillouteux (ébauche) :** Volez au dessus des plus hauts sommets... Et redescendez poussés par un éboulement !  
**6 - Algues Au Rythme (ébauche presque finie) :** Roulez sur des containers et utilisez vos talents de véhicule waterproof pour nager comme un poisson dans l'eau !

### Bonus 
Cet écran donne accès à des minis jeux permettant de booster :  
-Vos scores personnels, à comparer avec vos amis.  
-Votre bourse en vous récompensant avec des pièces (à programmer).  
-Votre égo.  
Pour l'instant, seul un seul mini jeu est disponnible :  
**Flappy Tower :** Inspiré du système de défilement infini de Flappy Bird, le joueur, aux commandes du **Boing Boeing**, doit éviter des immeubles (équivalents des tuyaux) dont la hauteur est générée aléatoirement. Chaque couple d'immeubles passé récompense d'un point

### Garage
Ici, le joueur a accès à toutes ses statistiques. En haut à droite se trouve son total de pièces Mot'or (collectées dans les niveaux, permettant de personnaliser son véhicule). Leur total est mis à jour à chaque gain de pièce ou d'achat. Au milieu, dans deux cadres, se trouvent ses véhciules équipés. Son score pour le seul mini jeu dispnnible est aussi affiché dans un des cadres latéraux. Le bouton "Véhicules" au milieu permet d'accéder au magasin, et d'équiper un véhicule.

### MoreAuto
Le magasin de RAAC ! Le joueur a ici accès à plusieurs slots contenant chacun un véhicule (ou rien). Chaque véhicule proposé est une coloration différente du véhicule de base. Chaque variation coute une pièce. Une fois acheté, le joueur peut cliquer sur un de ses véhicules disponnibles pour l'équiper, justifié par une pastille verte. Les slots bleus (voitures) sont indépendants des slots rouges (avions).  
Des skins alternatifs des personnages sont en réflexion, ceux ci coûtant plus chers que de simples colorations.  
⚠️**Attention** : Lorsque que vous arrivez sur cet écran, les pastilles vertes de vos véhicules équipés n'apparaitront pas, mais cela n'a aucune incidence sur le code intérieur. Aussi, il est déconseillé d'acheter et d'équiper un slot vide, ce qui pourrait faire buger le jeu et vous empêcher définitivement l'accès au magasin, ou même à votre compte, à cause des conflits entre enregistrements de bases de données et code Python.

### Requis pour utiliser le code
Python 3.10.11 
Pygame 2.5.2  
Random  
Sqlite3 (pour les requêtes sur la base de données)  
JSON  
Time
