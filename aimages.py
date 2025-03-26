import pygame
pygame.init()
info = pygame.display.Info()
largeur, hauteur = info.current_w,info.current_h-100
plateau = pygame.display.set_mode((largeur, hauteur))

loading = pygame.image.load("LoadingScreen.png")
loading = pygame.transform.scale(loading, (largeur, hauteur))
plateau.blit(loading, (0, 0))
pygame.display.flip()


# les boutons
BModeHistoirei = pygame.image.load('BModeHistoire.png')
Bbonusi = pygame.image.load('Bbonus.png')
Bgaragei = pygame.image.load('Bgarage.png')
Bparametrei = pygame.image.load('Bparametre.png')
Bquitteri = pygame.image.load('Bquitter.png')
BretourPi = pygame.image.load('BretourP.png')
Bshopi = pygame.image.load('Bshop.png')
BretourGi = pygame.image.load('BretourG.png')
Bsloti = pygame.image.load('Bslot.png')
BslotBuyi = pygame.image.load('BslotBuy.png')
BslotEquipei = pygame.image.load('BslotEquipe.png')
# décors de chaques niveaux
Factoryi = pygame.image.load('Factory.png')
Concerti = pygame.image.load('Concert.png')
Sawmilli = pygame.image.load('Sawmill.png')
Parki = pygame.image.load('Park.png')
Mountaini = pygame.image.load('Mountain.png')
Oceani = pygame.image.load('Ocean.png')
NewNewYorki = pygame.image.load('NewNewYork.png')
# points de vie
LifeBarFulli = pygame.image.load('LifeBarFull.png')
LifeBarHalfi = pygame.image.load('LifeBarHalf.png')
LifeBarCritici = pygame.image.load('LifeBarCritic.png')
NoMoreLifei = pygame.image.load('NoMoreLife.png')
LifeBarNotLogici = pygame.image.load('LifeBarNotLogic.png')


# triggers des animations
Trigi = pygame.image.load('Trigger.png')
Triggerlongi = pygame.image.load('Triggerlong.png')
Trigballi = pygame.image.load('Trigball.png')
#liste des pieces
piecei = pygame.image.load('piece.png')


# piques tests
trianglei = pygame.image.load('triangle.png')
# rampes tests
RampeMi = pygame.image.load('RampeM.png')
RampeLi = pygame.image.load('RampeL.png')
# carres cubiques tests
carrenoiri = pygame.image.load('carrenoir.png')
plateformi = pygame.image.load('plateform.png')


# piques du niveau parc
BusColairei = pygame.image.load('BusColaire.png')
WelcomeParki = pygame.image.load('WelcomePark.png')
Bienvenuei = pygame.image.load('Bienvenue.png')
FileAttentei = pygame.image.load('FileAttente.png')
BlockTowi = pygame.image.load('BlockTow.png')
WelToweri = pygame.image.load('WelTower.png')
DropToweri = pygame.image.load('DropTower.png')
PlaneRidei = pygame.image.load('PlaneRide.png')
FerrisWeeli = pygame.image.load('FerrisWeel.png')
CoasterStationi = pygame.image.load('CoasterStation.png')
BegRailsi = pygame.image.load('BegRails.png')
RailMontei = pygame.image.load('RailMonte.png')
Rail1i = pygame.image.load('Rail1.png')
RailFall1i = pygame.image.load('RailFall1.png')
RailEnversi = pygame.image.load('RailEnvers.png')
RailFall2i = pygame.image.load('RailFall2.png')
Rail2i = pygame.image.load('Rail2.png')
RailDesentei = pygame.image.load('RailDesente.png')
RailBrakei = pygame.image.load('RailBrake.png')
Canoni = pygame.image.load('Canon.png')
fuseei = pygame.image.load('fusee.png')
rollercoaster1i = pygame.image.load('rollercoaster1.png')
rollercoaster2i = pygame.image.load('rollercoaster2.png')
ArtificeVerti = pygame.image.load('ArtificeVert.png')
ArtificeJaunei = pygame.image.load('ArtificeJaune.png')
ArtificeRosei = pygame.image.load('ArtificeRose.png')
# carres du niveau parc
FerrisBoundi = pygame.image.load('FerrisBound.png')


# piques de concert
barremusik0i = pygame.image.load('barremusik0.png')
barremusik1i = pygame.image.load('barremusik1.png')
barremusik2i = pygame.image.load('barremusik2.png')
barremusik3i = pygame.image.load('barremusik3.png')
musik1i = pygame.image.load('musik1.png')
musik2i = pygame.image.load('musik2.png')
musik3i = pygame.image.load('musik3.png')
bouteillei = pygame.image.load('bouteille.png')
bouchoni = pygame.image.load('bouchon.png')
fumeei = pygame.image.load('fumee.png')


# carres du niveau montagne
volcani = pygame.image.load('volcan.png')
# piques du niveau montagne
roc1i = pygame.image.load('roc1.png')
roc2i = pygame.image.load('roc2.png')
arbrei = pygame.image.load('roc2.png')


# carres du niveau ocean
contener1i = pygame.image.load('contener1.png')
contener2i = pygame.image.load('contener2.png')
contener3i = pygame.image.load('contener3.png')
contener4i = pygame.image.load('contener4.png')
contener5i = pygame.image.load('contener5.png')
contener6i = pygame.image.load('contener6.png')
Balli = pygame.image.load('Ball.png')
coquei = pygame.image.load('coque.png')
Fougerei = pygame.image.load('Fougere.png')
# piques de l'ocean
para1i = pygame.image.load('para1.png')
para2i = pygame.image.load('para2.png')
alguei = pygame.image.load('algue.png')
rocheri = pygame.image.load('rocher.png')