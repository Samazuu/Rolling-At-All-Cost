# main.py
Ce fichier est la base du code. Elle permet de le lancer, gère la classe des véhicules et toutes les méthodes expliquant comment ceux ci interagissent avec les différents objets. Elle contient aussi la fonction deroulement_niveau() qui permet de faire déplacer les objets dans les niveaux, gère les collisions capricieuses (le programme ne gère qu'une seule hitbox à la fois) et effectue des calculs pour la hitbox des véhicules. Elle gère aussi les différents écrans du jeu.

# aclass.py
Ce fichier gère toutes les classes du code à l'exception de la classe Voiture().

# afonctions 
Ce fichier contient toutes les fonctions essentielles au programme, respectivement, l'application des paramètres musicaux  
des paramètres de langues  
l'affichage du seul record de mini jeu disponnible  
la gestion des niveaux réussis et leur enregistrement dans la database  
l'affichage de la barre de vie  
la gestion des véhicules équipés avec la database  
la gestion des achats dans la boutique  
l'affichage du message impossible lors d'un achat sans assez de pièces  

# aobjets
Ce fichier contient tous les objets nécessaires au programme, niveaux, obstacles, trigger, boutons, slots, excepté les véhicules créés dans *main.py*. Il contient aussi des listes de listes remplies de ces objets, celles ci étant essentielles pour la fonction *deroulement_niveau()* qui utilise ces listes pour faire bouger les objets.

# aimages
Ce fichier contient toutes les images nécessaires au jeu et les charge toutes au lancement, ce qui explique le temps de chargement qui pourra durer quelques secondes, en fonction des performances de votre appareil.

# aFlappyTour
Ce fichier contient tout le mini jeu Flappy Tower. Il gère la génération aléatoire des tours et le défilement infini grâce à des illusions d'arrière plan, mais globalement, fonctionne comme un niveau normal. 
