import pygame
from aimages import*
from aclass import*

# les boutons
Bmode_hist = Obstacle((BModeHistoirei), 0.39*largeur, 0.4*hauteur)
Bbonus = Obstacle((Bbonusi), 0.045*largeur, 0.30*hauteur)
Bgarage = Obstacle((Bgaragei), 0.74*largeur, 0.4*hauteur)
Bparametre = Obstacle((Bparametrei), 0.95*largeur, 0.16*hauteur) 
Bquitter = Obstacle((Bquitteri), 0.03*largeur, 0.03*hauteur) 
Bretour = Obstacle((BretourPi), 0.005*largeur, 0.01*hauteur) 
Bshop = Obstacle((Bshopi), 0.456*largeur, 0.61*hauteur)
retour = Obstacle((BretourGi), 0.001*largeur, 0.01*hauteur)
# les boutons slots (voiture)
slotCar1 = Slot((Bsloti), 0.072*largeur, 0.02*hauteur, 10, 1)
slotCar2 = Slot((Bsloti), 0.23*largeur, 0.02*hauteur, 11, 0)
slotCar3 = Slot((Bsloti),0.38*largeur, 0.02*hauteur, 12, 0)
slotCar4 = Slot((Bsloti),0.072*largeur, 0.17*hauteur, 13, 0)
slotCar5 = Slot((Bsloti),0.23*largeur, 0.17*hauteur, 14, 0)
slotCar6 = Slot((Bsloti),0.38*largeur, 0.17*hauteur, 15, 0)
slotCar7 = Slot((Bsloti),0.072*largeur, 0.32*hauteur, 16, 0)
slotCar8 = Slot((Bsloti),0.23*largeur, 0.32*hauteur, 17, 0)
slotCar9 = Slot((Bsloti),0.38*largeur, 0.32*hauteur, 18, 0)
slotCar10 = Slot((Bsloti),0.072*largeur, 0.48*hauteur, 19, 0)
slotCar11 = Slot((Bsloti),0.23*largeur, 0.48*hauteur, 19, 0)
slotCar12 = Slot((Bsloti),0.38*largeur, 0.48*hauteur, 19, 0)
slotCar13 = Slot((Bsloti),0.072*largeur, 0.64*hauteur, 19, 0)
slotCar14 = Slot((Bsloti),0.23*largeur, 0.64*hauteur, 19, 0)
slotCar15 = Slot((Bsloti),0.38*largeur, 0.64*hauteur, 19, 0)
slotCar16 = Slot((Bsloti),0.072*largeur, 0.79*hauteur, 19, 0)
slotCar17 = Slot((Bsloti),0.23*largeur, 0.79*hauteur, 19, 0)
slotCar18 = Slot((Bsloti),0.38*largeur, 0.79*hauteur, 19, 0)
# les boutons slots (avion)
slotPlane1 = Slot((Bsloti), 0.532*largeur, 0.02*hauteur, 20, 1)
slotPlane2 = Slot((Bsloti), 0.69*largeur, 0.02*hauteur, 21, 0)
slotPlane3 = Slot((Bsloti),0.84*largeur, 0.02*hauteur, 22, 0)
slotPlane4 = Slot((Bsloti),0.532*largeur, 0.17*hauteur, 23, 0)
slotPlane5 = Slot((Bsloti),0.69*largeur, 0.17*hauteur, 24, 0)
slotPlane6 = Slot((Bsloti),0.84*largeur, 0.17*hauteur, 25, 0)
slotPlane7 = Slot((Bsloti),0.532*largeur, 0.32*hauteur, 26, 0)
slotPlane8 = Slot((Bsloti),0.69*largeur, 0.32*hauteur, 27, 0)
slotPlane9 = Slot((Bsloti),0.84*largeur, 0.32*hauteur, 28, 0)
slotPlane10 = Slot((Bsloti),0.532*largeur, 0.48*hauteur, 29, 0)
slotPlane11 = Slot((Bsloti),0.69*largeur, 0.48*hauteur, 30, 0)
slotPlane12 = Slot((Bsloti),0.84*largeur, 0.48*hauteur, 31, 0)
slotPlane13 = Slot((Bsloti),0.532*largeur, 0.64*hauteur, 32, 0)
slotPlane14 = Slot((Bsloti),0.69*largeur, 0.64*hauteur, 33, 0)
slotPlane15 = Slot((Bsloti),0.84*largeur, 0.64*hauteur, 34, 0)
slotPlane16 = Slot((Bsloti),0.532*largeur, 0.79*hauteur, 35, 0)
slotPlane17 = Slot((Bsloti),0.69*largeur, 0.79*hauteur, 36, 0)
slotPlane18 = Slot((Bsloti),0.84*largeur, 0.79*hauteur, 37, 0)
# liste des boutons
liste_boutons = [[],
                 [Bmode_hist, Bbonus, Bgarage, Bparametre, Bquitter],
                 [Bretour, Bshop],
                 [Bretour],
                 [Bretour],
                 [],
                 []]
liste_slots = [[slotCar1, slotCar2, slotCar3, slotCar4, slotCar5, slotCar6, slotCar7, slotCar8, slotCar9, slotCar10, slotCar11,
              slotCar12, slotCar13, slotCar14, slotCar15, slotCar16, slotCar17, slotCar18], [slotPlane1, slotPlane2, slotPlane3,
              slotPlane4, slotPlane5, slotPlane6, slotPlane7, slotPlane8, slotPlane9, slotPlane10, slotPlane11, slotPlane12,
              slotPlane13, slotPlane14, slotPlane15, slotPlane16, slotPlane17, slotPlane18]]
        
        

#décors de chaques niveaux
Mapyork = Decor((NewNewYorki), 9)
Testmap = Decor((Oceani), 10)
Mapusine = Decor((Factoryi), 11)
Mapconcert = Decor((Concerti), 12)
Mapscierie = Decor((Sawmilli), 13)
Mappark = Decor((Parki), 14)
Mapmontagne = Decor((Mountaini), 15)
Mapocean = Decor((Oceani), 16)
niveau_used = Testmap
# points de vie
LifeBar = Placeholder((LifeBarFulli), largeur*0.7, hauteur*0.1)



# piques tests
pique = Obstacle((trianglei), largeur * -2, 0)
pique1 = Obstacle((trianglei), largeur * -2, 0)
pique2 = Obstacle((trianglei), largeur * -2, 0)
pique3 = Obstacle((trianglei), largeur * -2, 0)
# rampes tests
rampe = Rampe((RampeMi), largeur * -2, 0)
rampe1 = Rampe((RampeMi), largeur * -2, 0)
rampe2 = Rampe((RampeLi), largeur * -2, 0)
rampe3 = Rampe((RampeLi), largeur * -2, 0)
# carres tests
carre = Carre((carrenoiri), largeur * -2, 0)
carre1 = Carre((carrenoiri), largeur * -2, 0)
carre2 = Carre((plateformi), largeur * -2, 0)
carre3 = Carre((carrenoiri), largeur * -2, 0)


# triggers du niveau parc
trigDrop1 = Trigger((Trigi), largeur * -2, 0)
trigDrop2 = Trigger((Trigi), largeur * -2, 0)
trigDrop21 = Trigger((Trigi), largeur * -2, 0)
trigDrop3 = Trigger((Trigi), largeur * -2, 0)
trigDrop31 = Trigger((Trigi), largeur * -2, 0)
trigCoast1 = Trigger((Trigi), largeur * -2, 0)
trigCoastEnv = Trigger((Trigi), largeur * -2, 0)
trigCoastDroit = Trigger((Trigi), largeur * -2, 0)
trigCoast2 = Trigger((Trigi), largeur * -2, 0)
trigCoast3 = Trigger((Trigi), largeur * -2, 0)
trigRail1 = Trigger((Trigi), largeur * -2, 0)
trigRail2 = Trigger((Trigi), largeur * -2, 0)
trigFeu1 = Trigger((Trigi), largeur * -2, 0)
trigFeu2 = Trigger((Trigi), largeur * -2, 0)
trigFeu3 = Trigger((Trigi), largeur * -2, 0)
trigBoom1 = Trigger((Trigi), largeur * -2, 0)
trigBoom2 = Trigger((Trigi), largeur * -2, 0)
trigBoom3 = Trigger((Trigi), largeur * -2, 0)
# piques du niveau parc
bus = Obstacle((BusColairei), largeur * -2, 0)
bienvenue = Obstacle((WelcomeParki), largeur * -2, 0)
pancarte = Obstacle((Bienvenuei), largeur * -2, 0)
waitline1 = Obstacle((FileAttentei), largeur * -2, 0)
waitline2 = Obstacle((FileAttentei), largeur * -2, 0)
waitline3 = Obstacle((FileAttentei), largeur * -2, 0)
blocktower = Obstacle((BlockTowi), largeur * -2, 0)
welcometower = Obstacle((WelToweri), largeur * -2, 0)
drop1 = Obstacle((DropToweri), largeur * -2, 0)
drop2 = Obstacle((DropToweri), largeur * -2, 0)
drop3 = Obstacle((DropToweri), largeur * -2, 0)
planeR1 = Obstacle((PlaneRidei), largeur * -2, 0)
planeR2 = Obstacle((PlaneRidei), largeur * -2, 0)
planeR3 = Obstacle((PlaneRidei), largeur * -2, 0)
granderoue = Obstacle((FerrisWeeli), largeur * -2, 0)
station = Obstacle((CoasterStationi), largeur * -2, 0)
railsdebut = Obstacle((BegRailsi), largeur * -2, 0)
railmonte = Obstacle((RailMontei), largeur * -2, 0)
rail1 = Obstacle((Rail1i), largeur * -2, 0)
railtombe1 = Obstacle((RailFall1i), largeur * -2, 0)
railenvers = Obstacle((RailEnversi), largeur * -2, 0)
railtombe2 = Obstacle((RailFall2i), largeur * -2, 0)
rail2 = Obstacle((Rail2i), largeur * -2, 0)
raildescend = Obstacle((RailDesentei), largeur * -2, 0)
railfrein = Obstacle((RailBrakei), largeur * -2, 0)
canon = Obstacle((Canoni), largeur * -2, 0)
fusee1 = Obstacle((fuseei), largeur * -2, 0)
fusee2 = Obstacle((fuseei), largeur * -2, 0)
fusee3 = Obstacle((fuseei), largeur * -2, 0)
coaster1 = Obstacle((rollercoaster1i), largeur * -2, 0)
coaster2 = Obstacle((rollercoaster2i), largeur * -2, 0)
artificeV = Obstacle((ArtificeVerti), largeur * -2, 0)
artificeJ = Obstacle((ArtificeJaunei), largeur * -2, 0)
artificeR = Obstacle((ArtificeRosei), largeur * -2, 0)
# carres du niveau parc
ferrisB = Carre((FerrisBoundi), largeur * -2, 0)


# piques de concert
barre1 = Obstacle((barremusik3i), largeur * -2, 0)
barre2 = Obstacle((barremusik1i), largeur * -2, 0)
barre3 = Obstacle((barremusik2i), largeur * -2, 0)
barre4 = Obstacle((barremusik2i), largeur * -2, 0)
barre5 = Obstacle((barremusik1i), largeur * -2, 0)
barre6 = Obstacle((barremusik2i), largeur * -2, 0)
barre7 = Obstacle((barremusik3i), largeur * -2, 0)
barre8 = Obstacle((barremusik0i), largeur * -2, 0)
barre9 = Obstacle((barremusik1i), largeur * -2, 0)
barre10= Obstacle((barremusik2i), largeur * -2, 0)
musik10 = Obstacle((musik1i), largeur * -2, 0)
musik11 = Obstacle((musik1i), largeur * -2, 0)
musik20 = Obstacle((musik2i), largeur * -2, 0)
musik21 = Obstacle((musik2i), largeur * -2, 0)
musik22 = Obstacle((musik2i), largeur * -2, 0)
musik30 = Obstacle((musik3i), largeur * -2, 0)
musik31 = Obstacle((musik3i), largeur * -2, 0)
musik32 = Obstacle((musik3i), largeur * -2, 0)
bouteille1 = Obstacle((bouteillei), largeur * -2, 0)
bouteille2 = Obstacle((bouteillei), largeur * -2, 0)
bouteille3 = Obstacle((bouteillei), largeur * -2, 0)
bouchon1 = Obstacle((bouchoni), largeur * -2, 0)
bouchon2 = Obstacle((bouchoni), largeur * -2, 0)
bouchon3 = Obstacle((bouchoni), largeur * -2, 0)
fumee = Obstacle((fumeei), largeur * -2, 0)
#triggers du niveau concert
trigbouteille1 = Trigger((Triggerlongi), largeur * -2, 0)
trigbouteille2 = Trigger((Triggerlongi), largeur * -2, 0)
trigbouteille3 = Trigger((Triggerlongi), largeur * -2, 0)


# carres du niveau montagne
volcan = Carre((volcani), largeur * -2, 0)
# piques du niveau montagne
roc10 = Obstacle((roc1i), largeur * -2, 0)
roc11 = Obstacle((roc1i), largeur * -2, 0)
roc12 = Obstacle((roc1i), largeur * -2, 0)
roc20 = Obstacle((roc2i), largeur * -2, 0)
roc21 = Obstacle((roc2i), largeur * -2, 0)
roc22 = Obstacle((roc2i), largeur * -2, 0)
arbre = Obstacle((arbrei), largeur * -2, 0)
# triggers du niveau montagne
trigroc = Trigger((Trigballi), largeur * -2, 0)
trigarbre = Trigger((Trigballi), largeur * -2, 0)


# triggers du niveau ocean
trigcont4 = Trigger((Trigi), largeur * -2, 0)
trigcont5 = Trigger((Trigi), largeur * -2, 0)
trigcont6 = Trigger((Trigi), largeur * -2, 0)
trigtide = Trigger((Trigi), largeur * -2, 0)
trigball = Trigger((Trigballi), largeur * -2, 0)
# carres du niveau ocean
contener1 = Carre((contener1i), largeur * -2, 0)
contener2 = Carre((contener2i), largeur * -2, 0)
contener3 = Carre((contener3i), largeur * -2, 0)
contener4 = Carre((contener4i), largeur * -2, 0)
contener5 = Carre((contener5i), largeur * -2, 0)
contener6 = Carre((contener6i), largeur * -2, 0)
balle = Carre((Balli), largeur * -2, 0)
coque = Carre((coquei), largeur * -2, 0)
fougere = Carre((Fougerei), largeur * -2, 0)
# piques du niveau ocean
para1 = Obstacle((para1i), largeur * -2, 0)
para2 = Obstacle((para2i), largeur * -2, 0)
algue1 = Obstacle((alguei), largeur * -2, 0)
algue2 = Obstacle((alguei), largeur * -2, 0)
rocher = Obstacle((rocheri), largeur * -2, 0)


#liste des carres du jeu
liste_carres = [[carre, carre1, carre2, carre3],
                [],
                [],
                [],
                [ferrisB],
                [volcan],
                [contener1, contener2, contener3, contener4, contener5, contener6, balle, coque, fougere]]
prochain_c = liste_carres[0][0]

#liste des piques du jeu
liste_piques = [[pique, pique1, pique2, pique3],
                [],
                [musik10, musik11, musik20, musik21, musik22, musik30, musik31, musik32, bouteille1, bouteille2, bouteille3, bouchon1, bouchon2, bouchon3, fumee,
                 barre1, barre2, barre3, barre4, barre5, barre6, barre7, barre8, barre9, barre10],
                [],
                [bus, waitline1, waitline2, waitline3, bienvenue, pancarte, welcometower, blocktower, drop1, drop2, drop3, planeR1, planeR2, planeR3, granderoue,
                station, railsdebut, rail1, rail2, railmonte, raildescend, railenvers, railtombe1, railtombe2, railfrein, canon, fusee1, fusee2, fusee3, artificeV, artificeJ,
                artificeR, coaster1, coaster2],
                [roc10, roc11, roc12, roc20, roc21, roc22, arbre],
                [para1, para2, algue1, algue2, rocher]]

#liste de toutes les rampes du jeu
liste_rampes = [[rampe, rampe1, rampe2, rampe3], [], [], [], [], [], []]
prochain_r = liste_rampes[0][0]

#liste des triggers
liste_trig = [[],
              [],
              [trigbouteille1, trigbouteille2, trigbouteille3],
              [],
              [trigDrop1, trigDrop2, trigDrop21, trigDrop3, trigDrop31, trigCoast1, trigCoastEnv, trigCoast2, trigCoast3, trigCoastDroit,
              trigRail1, trigRail2, trigFeu1, trigFeu2, trigFeu3, trigBoom1, trigBoom2, trigBoom3],
              [trigroc, trigarbre],
              [trigcont4, trigcont5, trigcont6, trigtide, trigball]]

#liste des pieces
piece1 = Piece((piecei), largeur * -2, 0)
piece2 = Piece((piecei), largeur * -2, 0)
piece3 = Piece((piecei), largeur * -2, 0)
liste_piece = [piece1, piece2, piece3]