import pygame
import sqlite3
from random import*
from time import*
import json
from aimages import*
from aobjets import*
from aclass import*
from afonctions import*
from aniveaux import*
from aFlappyTour import*

conn = sqlite3.connect('RAACbasedonnee.db')
cursor = conn.cursor()

clock = pygame.time.Clock() #permet de définir un système d'horloge.
FPS = 20
temp_piece = [0, 0, 0]

#Définition du nom de la fenêtre : ce sera le nom du jeu
pygame.display.set_caption("Rolling At All Cost")

#Chargement puis définition de l'icone de la fenêtre
image = pygame.image.load("RAAClogo.png")
pygame.display.set_icon(image)

def taille_img(img):
    return pygame.transform.scale(img, (img.get_width()*largeur//1600, img.get_height()*hauteur//1000))
def largeur_img(img):
    return img.get_width()*largeur//1600
def hauteur_img(img):
    return img.get_height()*hauteur//1000
    
class Voiture :
    #cette classe permet de définir comment fonctionne les personnages jouables du jeu
    def __init__(self, x, y, sol_voiture, img, imgActu, vehicule, pv=2, maxpv=2):
        #le constructeur
        self.x = x
        self.y = y
        self.img = img
        self.imgActu = taille_img(imgActu)
        self.sol_voiture = sol_voiture 
        self.rect = self.imgActu.get_rect(topleft=(0, 0), size=(largeur_img(self.imgActu), hauteur_img(self.imgActu)))
        self.sol_avion = sol_voiture
        self.pv = pv
        self.maxpv = maxpv
        self.timejumping = 6
        self.timesprite = 0
        self.timesprite_avion = 0
        self.vehicule = vehicule
    
    #les getters
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_img(self):
        return self.img
    def get_imgActu(self):
        return self.imgActu
    def get_pv(self):
        return self.pv
    def get_maxpv(self):
        return self.maxpv
    def get_rect(self):
        return self.rect
    def get_sol_voiture(self):
        return self.sol_voiture
    def get_sol_avion(self):
        return self.sol_avion
    def get_vehicule(self):
        return self.vehicule
    
    #les setters
    def set_x(self, newx):
        self.x = newx
    def set_y(self, newy):
        self.y = newy
    def set_img(self, newimg):
        self.img = newimg
    def set_imgActu(self, newimgActu):
        self.imgActu = taille_img(newimgActu)
    def set_pv(self, newpv):
        self.pv = newpv
    def set_ID(self, newID):
        self.ID = newID
    def set_rect(self, newrect):
        self.rect = newrect
    def set_sol_voiture(self, newsol_voiture):
        self.sol_voiture = newsol_voiture
    def set_sol_avion(self, newsol_avion):
        self.sol_avion = newsol_avion
    def set_vehicule(self, newvehicule):
        self.vehicule = newvehicule
    
    
    def compteur_sprite(self):
        '''
        Cette méthode permet de gérer les cycles de la variable permettant de faire tourner les sprites de la voiture.
        Elle réinitiallise la variable "timesprite" à la fin d'un tour de roue ou d'un temps d'invincibilité.
        '''
        if self.timesprite == 7 or self.timesprite == 30 :
            self.timesprite = -1
    

    def compteur_sprite_avion(self):
        '''
        Cette méthode fonctionne de la même manière que "compteur_sprite()", mais existe en raison du nombre d'images différentes de l'avion.
        '''
        if self.timesprite_avion == 12 or self.timesprite_avion == 30 :
            self.timesprite_avion = 0
        

    def animer(self):
        '''
        Cette méthode gère les sprites de la voiture et l'avion, en fonction de la variable "timesprite" et "timesprite_avion". Elle permet aussi
        de faire augmenter de 1 la valeur de ces variables. Cette valeur est réinitialisée si nécessaire par "compteur_sprite()" et "
        compteur_sprite_avion()".
        '''
        self.timesprite += 1
        self.timesprite_avion += 1
        if self.vehicule == "voiture" :
            if self.timesprite < 0 :
                self.set_imgActu(self.img[8])
            elif self.timesprite == 0 or self.timesprite == 29 :
                self.set_imgActu(self.img[0])
            elif self.timesprite == 1 :
                self.set_imgActu(self.img[1])
            elif self.timesprite == 2 :
                self.set_imgActu(self.img[2])
            elif self.timesprite == 3 :
                self.set_imgActu(self.img[3])
            elif self.timesprite == 4 :
                self.set_imgActu(self.img[4])
            elif self.timesprite == 5 :
                self.set_imgActu(self.img[5])
            elif self.timesprite == 6 :
                self.set_imgActu(self.img[6])
            elif self.timesprite == 7 :
                self.set_imgActu(self.img[7])
        elif self.vehicule == "avion" :
            if self.timesprite_avion == 0 :
                self.set_imgActu(self.img[0])
            elif self.timesprite_avion == 2 :
                self.set_imgActu(self.img[1])
            elif self.timesprite_avion == 4 :
                self.set_imgActu(self.img[2])
            elif self.timesprite_avion == 6 :
                self.set_imgActu(self.img[3])
            elif self.timesprite_avion == 8 :
                self.set_imgActu(self.img[2])
            elif self.timesprite_avion == 10 :
                self.set_imgActu(self.img[1])
            
    
    def voiture_jump(self):
        '''
        Cette méthode permet de modifier la variable gérant les cycles de sprites pour "sortir" d'un cycle et ainsi commander un saut.
        '''
        if self.get_y() >= self.get_sol_voiture() or self.vehicule == "avion":
            self.timejumping = 0
            self.timesprite = -12
    
    
    def draw_car(self):
        '''
        Cette méthode permet au programme d'afficher les véhicules, autrement ils n'apparaitraient jamais ! En fonction des informations qu'elle
        reçoit des autres méthodes (saut, en l'air, descente, ou état normal) elle modifie la position du véhicule chaque seconde et met à jour
        l'écran.
        '''
        self.timejumping +=1
        if self.vehicule == "voiture" :
            if self.timejumping<=10:                        #elle saute
                self.set_y(self.get_y() - hauteur*0.02)
            elif self.timejumping<=15:                      #elle stagne en l'air
                pass
            elif self.get_y() < self.get_sol_voiture() :    #elle redescend
                self.set_y(self.get_y() + hauteur*0.02)
            else :                                          #elle roule
                self.set_y(self.get_sol_voiture())
                
        elif self.vehicule == "avion" :
            if self.timejumping<=1:                         #il saute
                self.set_y(self.get_y() - hauteur*0.011)
            elif self.get_y() < self.get_sol_voiture() +1 : #il tombe
                self.set_y(self.get_y() + hauteur*0.018)
            else :
                self.timejumping = -1
        plateau.blit(self.imgActu, (self.get_x(), self.get_y()))
        

    def collision(self, id_niv):
        '''
        Cette méthode permet de gérer les collisons entre les véhicules et leur environnement. Elle s'occupe de chaque cas et vérifie en permancence
        une liste contenant chaque obstacles du jeu pour vérifier si l'un d'eux touche le véhicule. Un pique enlève une vie, et la méthode sort aussi
        la variable "timesprite" de son cycle pour provoquer une "blessure". L'image du véhicule blessé est affiché. Pendant ce délai, la valeurs
        de la variable empêche cette fonction d'infliger de dégâts. Un carré est un obstacle sur lequel on peut rouler, mais se le prendre de
        face tue instantannément et règle les vies à zéro. Pour l'avion, toucher le sol le fait rebondir et perdre une vie, et sortir de l'image
        par en haut le tue instantannément. Chaque cas est réglé par des if, et lorsque les pv atteignent zéro, le joueur est renvoyé au menu
        principal (animation à venir).
        '''
        global running, FPS
        
        #protège le véhicule de dégats infinis (frame d'invincibilité)
        if (self.timesprite < 10 and self.vehicule == "voiture") or (self.timesprite_avion < 13 and self.vehicule == "avion") :
            
            #les piques enlèvent une vie et affichent par un print et une image la vie perdue
            for p in liste_piques[id_niv-10] :
                if self.rect.colliderect(p.rect) :
                    self.set_pv(self.get_pv() - 1)
                    print('\n','---------------', self.get_pv(), '---------------','\n')
                    self.timesprite = 10
                    self.timesprite_avion = 13
                    if self.vehicule == "avion" :
                        self.set_imgActu(pygame.image.load('BoingOuch.png'))
                    else :
                        self.set_imgActu(pygame.image.load('SauterelleOuch.png'))
            #les carrés tuent instantanément
            for c in liste_carres[id_niv-10] :
                if self.rect.colliderect(c.rect) :
                    self.set_pv(0)
                    print('mort')
            
            if self.rect.colliderect(piece1.rect) :
                temp_piece[0] = 1
                piece1.set_y(piece1.get_y() - hauteur*0.05)
            elif self.rect.colliderect(piece2.rect) :
                temp_piece[1] = 1
                piece2.set_y(piece2.get_y() - hauteur*0.05)
            elif self.rect.colliderect(piece3.rect) :
                temp_piece[2] = 1
                piece3.set_y(piece3.get_y() - hauteur*0.05)
                    
            
            #l'avion perd une vie et rebondit en touchant le sol, et meurt en touchant le toit
            if self.vehicule == "avion" :
                if self.rect.colliderect(pygame.Rect((0,self.get_sol_avion()),(largeur,2))) :
                    self.set_pv(self.get_pv() - 1)
                    print('\n','---------------', self.get_pv(), '---------------','\n')
                    self.timesprite_avion = 13
                    self.set_imgActu(pygame.image.load('BoingOuch.png'))
                elif self.rect.colliderect(pygame.Rect((0,0),(largeur,2))) :
                     self.set_pv(0)
            
            #la mort déclenche la fin du niveau (possibilité de rajouter une animation)
            if self.get_pv()<=0:
                self.mort()
                
                
    def mort(self):
        temp_piece = [0, 0, 0]
        if self.vehicule == "avion" :
            self.set_imgActu(pygame.image.load('BoingOuch.png'))
        else :
            self.set_imgActu(pygame.image.load('SauterelleOuch.png'))
            
        for i in range(FPS):
            plateau.blit(niveau_used.img, (niveau_used.get_x(), niveau_used.get_y()))
            plateau.blit(self.imgActu, (self.get_x(), self.get_y()))
            draw_life(self)
            self.set_y(self.get_y()*0.95)
            pygame.display.flip()
            clock.tick(FPS)
        for i in range(FPS//2):
            plateau.blit(niveau_used.img, (niveau_used.get_x(), niveau_used.get_y()))
            plateau.blit(self.imgActu, (self.get_x(), self.get_y()))
            draw_life(self)
            self.set_y(self.get_y()*1.2)
            pygame.display.flip()
            clock.tick(FPS)
        

        worldone()
        continuer_world_one = True
        
    def est_mort(self):
        return self.pv<=0

    def triggered(self):
        '''
        Cette fonction permet d'associer à chaque déclencheur un déplacement d'objet. Dès qu'un déclencheur est stimulé, elle
        donne de nouvelles coordonnées à l'objet en question pour donner l'illusion d'un mouvement. Les déclencheurs sont stimulés
        par une collision avec le joueur.
        '''
        #niveau parc
        if self.rect.colliderect(trigDrop1.rect) :
            drop1.set_y(drop1.get_y() + hauteur*0.04)
        elif self.rect.colliderect(trigDrop2.rect) :
            drop2.set_y(drop2.get_y() + hauteur*0.02)
        elif self.rect.colliderect(trigDrop21.rect) :
            drop2.set_y(drop2.get_y() + hauteur*0.016)
        elif self.rect.colliderect(trigDrop3.rect) :
            drop3.set_y(drop3.get_y() + hauteur*0.008)
        elif self.rect.colliderect(trigDrop31.rect) :
            drop3.set_y(drop3.get_y() + hauteur*0.016)
        elif self.rect.colliderect(trigCoast1.rect) :
            coaster1.set_x(coaster1.get_x() + largeur * 0.07)
        elif self.rect.colliderect(trigCoastEnv.rect) :
            coaster2.set_x(coaster1.get_x())
            coaster2.set_y(hauteur * 0.47)
            trigCoastEnv.set_x(largeur * largeur * -2)
            coaster1.set_x(largeur * largeur * -2)
        elif self.rect.colliderect(trigCoast2.rect) :
            coaster2.set_x(coaster2.get_x() + largeur*0.06)
        elif self.rect.colliderect(trigCoastDroit.rect) :
            coaster1.set_x(coaster2.get_x())
            coaster1.set_y(hauteur * 0.37)
            trigCoastDroit.set_x(largeur * largeur * -2)
            coaster2.set_x(largeur * largeur * -2)
        elif self.rect.colliderect(trigCoast3.rect) :
            coaster1.set_x(coaster1.get_x() + largeur*0.02)
        elif self.rect.colliderect(trigRail1.rect) :
            railtombe1.set_y(railtombe1.get_y() + hauteur*0.05)
        elif self.rect.colliderect(trigRail2.rect) :
            railtombe2.set_y(railtombe2.get_y() + hauteur*0.05)
        
        elif self.rect.colliderect(trigFeu1.rect) :
            fusee1.set_y(fusee1.get_y() + hauteur*-0.05)
        elif self.rect.colliderect(trigBoom1.rect) :
            artificeV.set_x(fusee1.get_x())
            artificeV.set_y(fusee1.get_y())
            trigBoom1.set_x(largeur * largeur * -2)
            fusee1.set_x(largeur * largeur * -2)
            
        elif self.rect.colliderect(trigFeu2.rect) :
            fusee2.set_y(fusee2.get_y() + hauteur*-0.06)
        elif self.rect.colliderect(trigBoom2.rect) :
            artificeJ.set_x(fusee2.get_x())
            artificeJ.set_y(fusee2.get_y())
            trigBoom2.set_x(largeur * largeur * -2)
            fusee2.set_x(largeur * largeur * -2)
            
        elif self.rect.colliderect(trigFeu3.rect) :
            fusee3.set_y(fusee3.get_y() + hauteur*-0.07)
        elif self.rect.colliderect(trigBoom3.rect) :
            artificeR.set_x(fusee3.get_x())
            artificeR.set_y(fusee3.get_y())
            trigBoom3.set_x(largeur * largeur * -2)
            fusee3.set_x(largeur * largeur * -2)
            
        #niveau ocean
        if self.rect.colliderect(trigcont4.rect) :
            contener4.set_y(contener4.get_y() + hauteur*0.005)
        elif self.rect.colliderect(trigcont5.rect) :
            contener5.set_y(contener5.get_y() + hauteur*0.017)
        elif self.rect.colliderect(trigcont6.rect) :
            contener6.set_y(contener6.get_y() - hauteur*0.009)
        elif self.rect.colliderect(trigball.rect) :
            balle.set_x(self.get_x() + largeur*0.07)
        elif self.rect.colliderect(trigtide.rect) :
            Mapocean.set_sol(Mapocean.get_sol() + hauteur*0.012)
        
        #niveau montagne
        if self.rect.colliderect(trigroc.rect) :
            roc10.set_y(roc10.get_y() + hauteur*0.002)
            roc11.set_y(roc11.get_y() + hauteur*0.002)
            roc12.set_y(roc12.get_y() + hauteur*0.002)
            roc20.set_y(roc20.get_y() + hauteur*0.002)
            roc21.set_y(roc21.get_y() + hauteur*0.002)
            roc22.set_y(roc22.get_y() + hauteur*0.002)
        elif self.rect.colliderect(trigarbre.rect) :
            arbre.set_y(arbre.get_y() + hauteur*0.005)
            arbre.set_x(arbre.get_x() + largeur*0.005)
            
        #niveau concert
        if self.rect.colliderect(trigbouteille1.rect) :
            bouteille1.set_y(bouteille1.get_y() - hauteur*0.04)
            bouchon1.set_y(bouchon1.get_y() - hauteur*0.08)
        elif self.rect.colliderect(trigbouteille2.rect) :
            bouteille2.set_y(bouteille2.get_y() - hauteur*0.04)
            bouchon2.set_y(bouchon2.get_y() - hauteur*0.05)
        elif self.rect.colliderect(trigbouteille3.rect) :
            bouteille3.set_y(bouteille3.get_y() - hauteur*0.03)
            bouchon3.set_y(bouchon3.get_y() - hauteur*0.09)
            
        
        
        
#les véhicules jouables
Sauteroule = Voiture(largeur/10, hauteur*0.74, hauteur*0.74, [pygame.image.load('Sauterelle1.png'), pygame.image.load('Sauterelle5.png'), pygame.image.load('Sauterelle2.png'), pygame.image.load('Sauterelle6.png'), pygame.image.load('Sauterelle3.png'), pygame.image.load('Sauterelle7.png'), pygame.image.load('Sauterelle4.png'), pygame.image.load('Sauterelle8.png'), pygame.image.load('SauterelleJump.png'), pygame.image.load('SauterelleOuch.png')], pygame.image.load('Sauterelle1.png'), "voiture", 3, 10)
BlueBlueCar= Voiture(largeur/10, hauteur*0.74, hauteur*0.74, [pygame.image.load('VoitBleue1.png'), pygame.image.load('VoitBleue5.png'), pygame.image.load('VoitBleue2.png'), pygame.image.load('VoitBleue6.png'), pygame.image.load('VoitBleue3.png'), pygame.image.load('VoitBleue7.png'), pygame.image.load('VoitBleue4.png'), pygame.image.load('VoitBleue8.png'), pygame.image.load('VoitBleueJump.png'), pygame.image.load('SauterelleOuch.png')], pygame.image.load('VoitBleue1.png'), "voiture", 3, 11)
VoitMarron= Voiture(largeur/10, hauteur*0.74, hauteur*0.74, [pygame.image.load('VoitMarron1.png'), pygame.image.load('VoitMarron5.png'), pygame.image.load('VoitMarron2.png'), pygame.image.load('VoitMarron6.png'), pygame.image.load('VoitMarron3.png'), pygame.image.load('VoitMarron7.png'), pygame.image.load('VoitMarron4.png'), pygame.image.load('VoitMarron8.png'), pygame.image.load('VoitMarronJump.png'), pygame.image.load('SauterelleOuch.png')], pygame.image.load('VoitMarron1.png'), "voiture", 3, 12)
BoingBoeing = Voiture(largeur/10, hauteur/5, hauteur*0.7, [pygame.image.load('Boing.png'), pygame.image.load('Boing2.png'), pygame.image.load('Boing3.png'), pygame.image.load('Boing4.png'), pygame.image.load('BoingOuch.png')], pygame.image.load('Boing.png'), "avion", 3, 20)
OrLine = Voiture(largeur/10, hauteur/5, hauteur*0.7, [pygame.image.load('AvOrange.png'), pygame.image.load('AvOrange2.png'), pygame.image.load('AvOrange3.png'), pygame.image.load('AvOrange4.png'), pygame.image.load('BoingOuch.png')], pygame.image.load('AvOrange.png'), "avion", 3, 21)
AvViolet = Voiture(largeur/10, hauteur/5, hauteur*0.7, [pygame.image.load('AvViolet.png'), pygame.image.load('AvViolet2.png'), pygame.image.load('AvViolet3.png'), pygame.image.load('AvViolet4.png'), pygame.image.load('BoingOuch.png')], pygame.image.load('AvViolet.png'), "avion", 3, 22)

list_voit = [Sauteroule, BlueBlueCar, VoitMarron]
list_plane = [BoingBoeing, OrLine, AvViolet]

for voiture in list_voit:
    voiture.set_sol_voiture(hauteur*0.7 - voiture.imgActu.get_height())
for avion in list_plane:
    avion.set_sol_voiture(hauteur*0.7 - voiture.imgActu.get_height())
    
    

condition_rampe = False
condition_carre = False
fin_niveau = 0
reussite = False
id_niv = 0


def deroulement_niveau(voiture_used, niveau_used, id_niv, fin_niveau):
    '''
    Cette fonction est appellée à chaque niveau lancé. C'est elle qui permet au niveau de fonctionner. Elle fais se déplacer le décor dans le
    sens inverse du joueur pour donner une illusion de déplacement. Elle parcoure toutes les listes contenant les objets du jeu pour pouvoir
    les afficher et les faire se déplacer à la même vitesse que le décor. Elle permet aussi de "monter" la hauteur du sol lorsque le joueur
    est au dessus d'un carré ou d'une rampe, pour ne pas s'enfoncer dedans. Cette fonction permet aussi de corriger un bug (ceux ci sont
    nombreux). Normalement le programme ne gérait que la hitbox du dernier objet du niveau. Cette fonction parcoure les listes pour indiquer
    le prochain obstacle que rencontrera le joueur pour lui donner une hitbox fonctionnelle. Ainsi, chaque objet a une hitbox un par un. C'est
    aussi cette fonction qui appelle toutes les méthodes gérant l'affichage et le choix du véhicule. Enfin, cette fonction gère la fin d'un
    niveau en retournant sur l'écran de choix des niveaux et en posant un marqueur de niveau validé.
    Elle retourne False si on doit arreter le niveau.
    '''
    global condition_carre, prochain_c, condition_rampe, prochain_r, continuer_world_one, liste_valide, clock, FPS, reussite, id_profil, list_voit, list_plane
    continuer_soon = False
    continuer_world_one = False
    running = True
    
    pygame.display.update() #actualise
    plateau.blit(niveau_used.img, (niveau_used.get_x(), niveau_used.get_y())) #affiche le décor
    niveau_used.set_x(niveau_used.get_x() - niveau_used.get_speed()) #le décor bouge, et non la voiture !
    avant_voiture = voiture_used.get_x() + voiture_used.imgActu.get_width() #formule pour avoir l'avant de la voiture
    
    for t in liste_trig[id_niv-10] : #les triggers avancent avec le décor
        t.set_x(t.get_x() - niveau_used.get_speed())
        t.set_rect(t.img.get_rect(topleft=(t.get_x(), t.get_y())))
        plateau.blit(t.img, (t.get_x(), t.get_y()))
        #pygame.draw.rect(plateau,(255,0,255),t.get_rect()) #affiche la colision des triggers
        
    for p in liste_piques[id_niv-10] : #les piquent avancent avec le décor
        p.set_x(p.get_x() - niveau_used.get_speed())
        p.set_rect(p.img.get_rect(topleft=(p.get_x(), p.get_y())))
        plateau.blit(p.img, (p.get_x(), p.get_y()))
        #pygame.draw.rect(plateau,(0,255,255),p.get_rect()) #affiche la colision des obstacles
        
    for pi in liste_piece: #les pieces avancent avec le décor
        pi.set_x(pi.get_x() - niveau_used.get_speed())
        pi.set_rect(pi.img.get_rect(topleft=(pi.get_x(), pi.get_y())))
        pi.animer()
        plateau.blit(pi.img, (pi.get_x(), pi.get_y()))
        #pygame.draw.rect(plateau,(0,180,100),pi.get_rect()) #affiche la colision des pieces
        
    for r in liste_rampes[id_niv-10] : #les rampent avancent avec le décor
        r.set_x(r.get_x() - niveau_used.get_speed())
        r.set_rect(r.img.get_rect(topleft=(r.get_x(), r.get_y())))
        plateau.blit(r.img, (r.get_x(), r.get_y()))
        #pygame.draw.rect(plateau,(0,255,255),r.get_rect()) #affiche la colision des rampes
        
        #détermine la rampe qui arrive
        if condition_rampe==False and avant_voiture >  r.get_x() :
            prochain_r = r
            condition_rampe = True
            #test print(prochain_r.get_x())
    if prochain_r.get_x()+prochain_r.img.get_width() < voiture_used.get_x():
        condition_rampe = False
        
    for c in liste_carres[id_niv-10] : #les carrés avancent avec le décor
        c.set_x(c.get_x() - niveau_used.get_speed())
        c.set_rect(c.img.get_rect(topleft=(c.get_x(), c.get_y() + c.img.get_height()*0.2)))
        plateau.blit(c.img, (c.get_x(), c.get_y()))
        #pygame.draw.rect(plateau,(255,255,0),c.get_rect()) #affiche la colision des obstacles cubiques
        
        #détermine le carré qui arrive
        if condition_carre==False and avant_voiture > c.get_x() and c.get_x()>0 :
            prochain_c = c
            condition_carre = True
    if avant_voiture > prochain_c.get_x()+prochain_c.img.get_width() :
        condition_carre = False
    #pygame.draw.rect(plateau,(255,200,0),prochain_c.get_rect())

    
    #change la hauteur du sol selon les rampes et carrés au même niveau que le véhicule
    hypothenuse = ((prochain_r.img.get_height()**2) + (prochain_r.img.get_width()**2))**(1/2)
    voiture_sautante = voiture_used.get_y() < prochain_c.get_y()+prochain_c.img.get_height()
    
    if avant_voiture > prochain_r.get_x() and prochain_r.get_x()+prochain_r.img.get_width() > voiture_used.get_x():
        voiture_used.set_sol_voiture(voiture_used.get_sol_voiture() - hypothenuse)
    elif avant_voiture > prochain_c.get_x() and prochain_c.get_x()+prochain_c.img.get_width() > voiture_used.get_x() and voiture_sautante :
        voiture_used.set_sol_voiture(prochain_c.get_y() - voiture_used.imgActu.get_height()*0.8)
    else :
        voiture_used.set_sol_voiture(niveau_used.get_sol())


    #appel des fonctions qui affichent la voiture
    sizev = (voiture_used.imgActu.get_width()*0.5, voiture_used.imgActu.get_height()*0.4)
    topleftv = (voiture_used.get_x()+voiture_used.imgActu.get_width()*0.3, voiture_used.get_y()+voiture_used.imgActu.get_height()*0.3)
    voiture_used.set_rect(voiture_used.imgActu.get_rect(topleft=topleftv, size=sizev))
    voiture_used.draw_car()
    
    draw_life(voiture_used)

    if voiture_used in list_voit :
        voiture_used.compteur_sprite()
    elif voiture_used in list_plane :
        voiture_used.compteur_sprite_avion()
    
    voiture_used.animer()
    voiture_used.collision(id_niv)
    voiture_used.triggered()
    
    #pygame.draw.rect(plateau,(255,0,255),voiture_used.get_rect()) #affiche la zone de colision du véhicule
    #pygame.draw.rect(plateau,(255,0,0),(0,voiture_used.get_sol_voiture()-voiture_used.imgActu.get_height(),largeur,2))
    #pygame.draw.rect(plateau,(255,0,0),(0,voiture_used.get_sol_avion()+voiture_used.imgActu.get_height(),largeur,2))
    
    
    #fin du niveau par victoire, pieces recoltees, et animation
    if niveau_used.img.get_width() + niveau_used.get_x() < largeur * fin_niveau :
        running = False
        for i in range(FPS*3):
            plateau.blit(niveau_used.img, (niveau_used.get_x(), niveau_used.get_y()))
            voiture_used.set_x(voiture_used.get_x()*1.2)
            voiture_used.set_y(voiture_used.get_y()*0.9)
            plateau.blit(voiture_used.imgActu, (voiture_used.get_x(), voiture_used.get_y()))
            pygame.display.flip()
            clock.tick(FPS) #permet de limiter le nombre d'images par seconde
            
            
        #validation du niveau
        for i in liste_valide :
            if i.get_id_niv() == id_niv :
                i.set_reussi(True)
                
                cursor.execute('SELECT * FROM reussi WHERE id_niveau=? AND id_profil=? ', (niveau_used.get_niveau(), id_profil))
                niveau_reussi(cursor.fetchone(), id_profil, temp_piece, niveau_used.get_niveau())
                pass
    
            
    #retour au menu du monde 1 ou non   
    return running


                    
                    

#création des objets "valide" pour afficher un niveau réussi
valide1 = Valide(pygame.image.load('Valided.png'), 0.29*largeur, 0.43*hauteur, 11)
valide2 = Valide(pygame.image.load('Valided.png'), 0.28*largeur, 0.606*hauteur, 12)
valide3 = Valide(pygame.image.load('Valided.png'), 0.453*largeur, 0.4*hauteur, 13)
valide4 = Valide(pygame.image.load('Valided.png'), 0.415*largeur, 0.566*hauteur, 14)
valide5 = Valide(pygame.image.load('Valided.png'), 0.576*largeur, 0.476*hauteur, 15)
valide6 = Valide(pygame.image.load('Valided.png'), 0.555*largeur, 0.666*hauteur, 16)
liste_valide = [valide1, valide2, valide3, valide4, valide5, valide6]

###ecran de connexion###
def ecran_connexion():
    '''
    cet ecran s'affiche en premier. Il permet de se connecter à son compte ou d'en créer un nouveau
    '''
    global continuer
    #chargement et redimension de l'image de fond de l'écran d'accueil 
    fond_accueil = pygame.image.load("connexion.png")
    fond_accueil = pygame.transform.scale(fond_accueil, (largeur, hauteur))
    musique_active('GD.mp3')

    #définition des boutons qui serviront à lancer le jeu
    connecter = pygame.Rect(0.27*largeur, 0.05*hauteur, largeur*0.45, hauteur*0.17) #coordonnées en x, coordonnées en y, largeur, hauteur
    creercompte = pygame.Rect(0.26*largeur, 0.53*hauteur, largeur*0.45, hauteur*0.18)
    ecritconnecter = pygame.Rect(0.29*largeur, 0.25*hauteur, largeur*0.4, hauteur*0.15)
    ecritcreer = pygame.Rect(0.29*largeur, 0.75*hauteur, largeur*0.4, hauteur*0.15)
    
    musique = pygame.Rect(0.85*largeur, 0.33*hauteur, largeur/6, hauteur/8) #coordonnées en x, y, largeur, hauteur
    francais = pygame.Rect(0.75*largeur, 0.5*hauteur, largeur/6, hauteur/8)
    anglais = pygame.Rect(0.75*largeur, 0.6*hauteur, largeur/6, hauteur/8)
    allemand = pygame.Rect(0.75*largeur, 0.7*hauteur, largeur/6, hauteur/8)
    liste_boutons = [connecter, creercompte, ecritconnecter, ecritcreer, musique, francais, anglais, allemand]
    
    bouton_musique = pygame.image.load("BoutonOn.png")
    bouton_langue1 = pygame.image.load("BoutonLangues_actif.png")
    bouton_langue2 = pygame.image.load("BoutonLanguesANG.png")
    bouton_langue3 = pygame.image.load("BoutonLanguesALL.png")
    
    ecritchamp1 = False
    ecritchamp2 = False

    #boucle de l'ecran de connexion qui continue tant qu'on ne clique pas sur la croix
    continuer_connexion = True
    continuer_bonus = False
    continuer_world_one = False
    continuer = False
    continuer_soon = False
    continuer_load = False
    pygame.time.delay(1)
    pygame.display.flip()
    
    #le texte
    pseudo=""
    pygame.font.init()
    pseudoaffiche = pygame.font.Font("Wonderly.otf", hauteur//8)
    score_display = pseudoaffiche.render(pseudo, 0, (200,200,100))
    plateau.blit(score_display, (largeur*0.3, hauteur*0.25))
    retrytest = 200
    
    while continuer_connexion :
        #affichage du fond d'écran
        plateau.blit(fond_accueil, (0, 0))
        plateau.blit(bouton_musique, (0.85*largeur, 0.35*hauteur))
        plateau.blit(bouton_langue1, (0.75*largeur, 0.5*hauteur))
        plateau.blit(bouton_langue2, (0.75*largeur, 0.6*hauteur))
        plateau.blit(bouton_langue3, (0.75*largeur, 0.72*hauteur))
        retrytest += 1

        #affichage du rectangle des boutons (pour en créer)
        #for bouton in liste_boutons :
            #pygame.draw.rect(plateau, (200, 200, 200), bouton)

        #récupération de tous les évènements captés par la fenêtre
        for event in pygame.event.get():
            
            #si l'utilisateur a cliqué sur la croix
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if event.type == pygame.KEYDOWN:
                    if len(pseudo) < 13 :
                        pseudo += event.unicode
                    if event.key == pygame.K_BACKSPACE :
                        pseudo = pseudo[:-2]
                        
            #si l'utilisateur a cliqué dans la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:
                #si le clic a été fait à la position d'un bouton (tout les boutons seront définis plus tard)
                for bouton in liste_boutons :
                    if bouton.collidepoint(event.pos):
                        #print('detected', bouton)
                        if bouton == ecritconnecter :
                            ecritchamp1 = True
                            ecritchamp2 = False
                            pseudo=''
                        elif bouton == ecritcreer :
                            pseudo=''
                            ecritchamp2 = True
                            ecritchamp1 = False
                            
                        elif bouton == connecter:
                            cursor.execute('SELECT pseudo FROM profil')
                            pseudoconnexion = cursor.fetchall()
                            for i in pseudoconnexion :
                                if pseudo == i[0] :
                                    cursor.execute('SELECT id_profil FROM profil WHERE pseudo=?', (pseudo,))
                                    global id_profil
                                    id_profil = cursor.fetchone()[0]
                                    plateau_accueil(id_profil)
                            else :
                                retrytest = 0
                                
                        elif bouton == creercompte:
                            newid = randint(0,9223372036854775807)
                            cursor.execute('INSERT INTO profil VALUES  (?, ?, 0)', (newid, pseudo))
                            conn.commit()
                            cursor.execute('SELECT id_profil FROM profil WHERE pseudo=?', (pseudo,))
                            id_profil = cursor.fetchone()[0]
                            
                            cursor.execute('INSERT INTO inventaire VALUES  (?, ?, ?)', (newid, str([10]), str([20])))
                            conn.commit()
                            cursor.execute('INSERT INTO vehicule_actu VALUES  (?, ?, ?)', (newid, 10, 20))
                            conn.commit()
                            cursor.execute('INSERT INTO reussi VALUES  (10, ?, 0, 0, 0)', (newid,))
                            conn.commit()
                                                   
                            plateau_accueil(id_profil)
                            
                        if bouton == musique :
                            if langue.get_musique() == True:
                                langue.set_musique(False)
                                bouton_musique = pygame.image.load("BoutonOff.png")
                            else:
                                langue.set_musique(True)
                                bouton_musique = pygame.image.load("BoutonOn.png")
                            musique_active('GD.mp3')
                        
                        elif bouton == francais :
                            langue.set_langue_active('francais')
                            bouton_langue1 = pygame.image.load("BoutonLangues_actif.png")
                            bouton_langue2 = pygame.image.load("BoutonLanguesANG.png")
                            bouton_langue3 = pygame.image.load("BoutonLanguesALL.png")
                            fond_accueil = langue_img("Connexion.png", "ConnexionANG.png", "ConnexionALL.png")
                            fond_accueil = pygame.transform.scale(fond_accueil, (largeur, hauteur))
                        elif bouton == anglais :
                            langue.set_langue_active('anglais')
                            bouton_langue1 = pygame.image.load("BoutonLangues.png")
                            bouton_langue2 = pygame.image.load("BoutonLanguesANG_actif.png")
                            bouton_langue3 = pygame.image.load("BoutonLanguesALL.png")
                            fond_accueil = langue_img("Connexion.png", "ConnexionANG.png", "ConnexionALL.png")
                            fond_accueil = pygame.transform.scale(fond_accueil, (largeur, hauteur))
                        elif bouton == allemand :
                            langue.set_langue_active('allemand')
                            bouton_langue1 = pygame.image.load("BoutonLangues.png")
                            bouton_langue2 = pygame.image.load("BoutonLanguesANG.png")
                            bouton_langue3 = pygame.image.load("BoutonLanguesALL_actif.png")
                            fond_accueil = langue_img("Connexion.png", "ConnexionANG.png", "ConnexionALL.png")
                            fond_accueil = pygame.transform.scale(fond_accueil, (largeur, hauteur))
        
        if ecritchamp1 :
            plateau.blit(score_display, (largeur*0.3, hauteur*0.25))
        if ecritchamp2 :
            plateau.blit(score_display, (largeur*0.3, hauteur*0.75))
        
        if retrytest < 200 :
            retry = pseudoaffiche.render('try again', 0, (255,100,100))
            plateau.blit(retry, (largeur*0.3, hauteur*0.85))
        
        if (retrytest//100)%2==0:
            score_display = pseudoaffiche.render(pseudo + 'l', 0, (200,250,200))
        else :
            score_display = pseudoaffiche.render(pseudo, 0, (200,250,200))
        pygame.display.flip() #actualise

 


### fonction qui gère la page d'accueil ###
def plateau_accueil(id_profil):
    '''
    Cette fonction gère l'affichage du menu principal. Elle actualise constamment l'écran pour qu'il s'affiche, lance une musique de fond et
    définie les boutons, qui sont juste des zones de hitbox par dessus les dessins. Pour chaque bouton elle appelle une autre fonction affichant
    un autre écran, et se désactivera d'elle même, grâce à des variables. C'est aussi cette fonction qui appelle la fonction de saut
    lorsque le joueur veut sauter. Aussi, la première fois que le jeu est lancé, cette fonction déclenche le temps de chargement principal
    (flex XD). Une variable permet d'empêcher ce temps de s'afficher à nouveau.
    '''
    global running, premier, continuer_connexion
    if premier == 1:
        for _ in range(150):
            #affichage du fond d'écran
            plateau.blit(loading, (0, 0))
            pygame.display.flip()
    premier = 0
    #chargement et redimension de l'image de fond de l'écran d'accueil
    fond_accueil = langue_img("MainMenu.png", "MainMenuANG.png", "MainMenuALL.png")
    fond_accueil = pygame.transform.scale(fond_accueil, (largeur, hauteur))
    musique_active('GD.mp3')

    #définition des boutons qui serviront à lancer le jeu
    mode_hist = pygame.Rect(0.39*largeur, 0.4*hauteur, largeur/6, hauteur/7) #coordonnées en x, coordonnées en y, largeur, hauteur
    bonusS = pygame.Rect(0.038*largeur, 0.38*hauteur, largeur/6, hauteur/5)
    garage = pygame.Rect(0.74*largeur, 0.4*hauteur, largeur/6, hauteur/6)
    parametre = pygame.Rect(0.95*largeur, 0.17*hauteur, largeur/22, hauteur/13)
    quitter = pygame.Rect(0.03*largeur, 0.04*hauteur, largeur/20, hauteur/11)
    liste_boutons = [mode_hist, bonusS, garage, parametre, quitter]

    #boucle de la page d'accueil qui continue tant qu'on ne clique pas sur la croix
    continuer_connexion = False
    continuer_bonus = False
    continuer_world_one = False
    continuer = True
    continuer_soon = False
    continuer_load = False
    continuer_parametre = False
    pygame.time.delay(1)
    pygame.display.flip()
                
                
    while continuer:
        #affichage du fond d'écran
        plateau.blit(fond_accueil, (0, 0))

        #affichage du rectangle des boutons (pour en créer)
        #for bouton in liste_boutons :
            #pygame.draw.rect(plateau, (200, 200, 200), bouton)

        #récupération de tous les évènements captés par la fenêtre
        for event in pygame.event.get():
            
            #si l'utilisateur a cliqué sur la croix
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #si l'utilisateur a cliqué dans la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:
                #si le clic a été fait à la position d'un bouton (tout les boutons seront définis plus tard)
                for bouton in liste_boutons :
                    if bouton.collidepoint(event.pos):
                        #print('detected', bouton)
                        if bouton == mode_hist :
                            worldone()
                            global running
                        elif bouton == bonusS :
                            bonus(id_profil)
                            global running
                        elif bouton == garage :
                            profilMenu(id_profil)
                            global running
                        elif bouton == parametre :
                            EcranParametre(id_profil)
                            global running
                        elif bouton == quitter :
                            pygame.quit()
                            exit()
        
                            
        pygame.display.flip() #actualise



def EcranParametre(id_profil):
    global running, continuer_parametre
    #chargement et redimension de l'image de fond de l'écran d'accueil
    fond_accueil = langue_img("ParametreEcran.png", "ParametreEcranANG.png", "ParametreEcranALL.png")
    fond_accueil = pygame.transform.scale(fond_accueil, (largeur, hauteur))
    
    musique_active('GD.mp3')

    #définition des boutons qui serviront à lancer le jeu
    musique = pygame.Rect(0.45*largeur, 0.23*hauteur, largeur/6, hauteur/8) #coordonnées en x, y, largeur, hauteur
    francais = pygame.Rect(0.45*largeur, 0.4*hauteur, largeur/6, hauteur/8)
    anglais = pygame.Rect(0.45*largeur, 0.5*hauteur, largeur/6, hauteur/8)
    allemand = pygame.Rect(0.45*largeur, 0.6*hauteur, largeur/6, hauteur/8)
    retour = pygame.Rect(0.02*largeur, 0.03*hauteur, largeur/9, hauteur/10)
    liste_boutons = [musique, francais, anglais, allemand, retour]
    
    #affichage des images des boutons
    if langue.get_musique() == True:
        bouton_musique = pygame.image.load("BoutonOn.png")
    else:
        bouton_musique = pygame.image.load("BoutonOff.png")
        
    if langue.get_langue_active() == 'francais':
        bouton_langue1 = pygame.image.load("BoutonLangues_actif.png")
        bouton_langue2 = pygame.image.load("BoutonLanguesANG.png")
        bouton_langue3 = pygame.image.load("BoutonLanguesALL.png")
        fond_accueil = langue_img("ParametreEcran.png", "ParametreEcranANG.png", "ParametreEcranALL.png")
        fond_accueil = pygame.transform.scale(fond_accueil, (largeur, hauteur))
    if langue.get_langue_active() == 'anglais':
        bouton_langue1 = pygame.image.load("BoutonLangues.png")
        bouton_langue2 = pygame.image.load("BoutonLanguesANG_actif.png")
        bouton_langue3 = pygame.image.load("BoutonLanguesALL.png")
        fond_accueil = langue_img("ParametreEcran.png", "ParametreEcranANG.png", "ParametreEcranALL.png")
        fond_accueil = pygame.transform.scale(fond_accueil, (largeur, hauteur))
    if langue.get_langue_active() == 'allemand':
        bouton_langue1 = pygame.image.load("BoutonLangues.png")
        bouton_langue2 = pygame.image.load("BoutonLanguesANG.png")
        bouton_langue3 = pygame.image.load("BoutonLanguesALL_actif.png")
        fond_accueil = langue_img("ParametreEcran.png", "ParametreEcranANG.png", "ParametreEcranALL.png")
        fond_accueil = pygame.transform.scale(fond_accueil, (largeur, hauteur))

    continuer = False
    continuer_parametre = True
    pygame.time.delay(1)
    pygame.display.flip()
                
    #boucle de la page d'accueil qui continue tant qu'on ne clique pas sur la croix
    while continuer_parametre:
        #affichage du fond d'écran
        plateau.blit(fond_accueil, (0, 0))

        plateau.blit(bouton_musique, (0.48*largeur, 0.25*hauteur))
        plateau.blit(bouton_langue1, (0.48*largeur, 0.4*hauteur))
        plateau.blit(bouton_langue2, (0.48*largeur, 0.5*hauteur))
        plateau.blit(bouton_langue3, (0.48*largeur, 0.62*hauteur))

        #affichage du rectangle des boutons (pour en créer)
        #for bouton in liste_boutons :
            #pygame.draw.rect(plateau, (200, 200, 200), bouton)

        #récupération de tous les évènements captés par la fenêtre
        for event in pygame.event.get():
            
            #si l'utilisateur a cliqué sur la croix
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #si l'utilisateur a cliqué dans la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:
                #si le clic a été fait à la position d'un bouton (tout les boutons seront définis plus tard)
                for bouton in liste_boutons :
                    if bouton.collidepoint(event.pos):
                        #print('detected', bouton)
                        if bouton == musique :
                            if langue.get_musique() == True:
                                langue.set_musique(False)
                                bouton_musique = pygame.image.load("BoutonOff.png")
                            else :
                                langue.set_musique(True)
                                bouton_musique = pygame.image.load("BoutonOn.png")
                            musique_active('GD.mp3')
                            
                        elif bouton == francais :
                            langue.set_langue_active('francais')
                            bouton_langue1 = pygame.image.load("BoutonLangues_actif.png")
                            bouton_langue2 = pygame.image.load("BoutonLanguesANG.png")
                            bouton_langue3 = pygame.image.load("BoutonLanguesALL.png")
                        elif bouton == anglais :
                            langue.set_langue_active('anglais')
                            bouton_langue1 = pygame.image.load("BoutonLangues.png")
                            bouton_langue2 = pygame.image.load("BoutonLanguesANG_actif.png")
                            bouton_langue3 = pygame.image.load("BoutonLanguesALL.png")
                        elif bouton == allemand :
                            langue.set_langue_active('allemand')
                            bouton_langue1 = pygame.image.load("BoutonLangues.png")
                            bouton_langue2 = pygame.image.load("BoutonLanguesANG.png")
                            bouton_langue3 = pygame.image.load("BoutonLanguesALL_actif.png")
                        elif bouton == retour :
                            plateau_accueil(id_profil)
        
                            
        pygame.display.flip() #actualise



def profilMenu(id_profil):
    '''
    Cette fonction fonctionne (on le répètera jamais assez) comme les précédentes, et permet d'afficher l'écran Comming Soon, que l'on
    appelle pour toutes les sections du jeu prévues mais non commencées ou qui sont encore en phase de "ressemble à rien".
    '''
    global running, continuer, continuer_world_one, continuer_soon, continuer_profil, continuer_shop
    #chargement et redimension de l'image de fond de l'écran d'accueil
    Profile = langue_img("ProfilMenu.png", "ProfilMenuANG.png", "ProfilMenuALL.png")
    Profile = pygame.transform.scale(Profile, (largeur, hauteur))
    
    #mise en place de la musique
    musique_active('BonusOST.mp3')

    #définition des boutons
    retour = pygame.Rect(0.03*largeur, 0.03*hauteur, 0.08*largeur, 0.09*hauteur) #coordonnées en x, coordonnées en y, largeur, hauteur
    shop = mode_hist = pygame.Rect(0.456*largeur, 0.64*hauteur, 0.08*largeur, 0.09*hauteur)
    
    liste_bout = [retour, shop]
    

    #boucle qui arrête la précédente et continue tant qu'on ne clique pas sur la croix
    continuer = False
    continuer_world_one = False
    running = False
    continuer_soon = False
    continuer_profil = True
    continuer_shop = False
    pygame.time.delay(1)
    pygame.display.flip()

    cursor.execute("SELECT nb_pieces FROM profil WHERE id_profil = ?", (id_profil,))
    nb_piece = cursor.fetchone()[0]
    cursor.execute("SELECT high_score FROM record WHERE id_profil = ? and id_mini = ?", (id_profil,2))
    score = cursor.fetchone()
    if score == None:
        score = 0
    else :
        score = score[0]
    voiture_actu, avion_actu = get_vehicules_actu(id_profil)

    
    while continuer_profil:
        #affichage du fond d'écran
        plateau.blit(Profile, (0, 0))
        plateau.blit(taille_img(list_voit[voiture_actu-10].get_img()[0]), (largeur*0.32, hauteur*0.45))
        plateau.blit(taille_img(list_plane[avion_actu-20].get_img()[0]), (largeur*0.53, hauteur*0.45))
        
        pygame.font.init()
        score_display = pygame.font.Font("Wonderly.otf", hauteur//11).render(str(nb_piece), 0, (255, 255, 0))
        plateau.blit(score_display, (largeur*0.86, hauteur*0.05))
        
        afficher_record_flappy(score, 'profilMenu')

        #affichage du rectangle des boutons (utile pour créer les pochains mondes)
        #for bouton in liste_bout :
            #pygame.draw.rect(plateau, (200, 200, 200), bouton)

        #récupération de tous les évènements captés par la fenêtre
        for event in pygame.event.get():

            #si l'utilisateur a cliqué sur la croix
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #si l'utilisateur a cliqué dans la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bouton1 in liste_bout :
                    if bouton1.collidepoint(event.pos):
                        #print('detected', bouton1)
                        if bouton1 == retour : #retour en arrière
                            plateau_accueil(id_profil)
                        if bouton1 == shop:
                            shopMenu(id_profil)
        pygame.display.flip()
        
        
def shopMenu(id_profil):
    '''
    Cette fonction fonctionne (on le répètera jamais assez) comme les deux précédentes, et permet d'afficher l'écran Comming Soon, que l'on
    appelle pour toutes les sections du jeu prévues mais non commencées ou qui sont encore en phase de "ressemble à rien".
    '''
    global running, continuer, continuer_world_one, continuer_soon
    #chargement et redimension de l'image de fond de l'écran d'accueil
    Shopping = pygame.image.load("ShopMenu.png")
    Shopping = pygame.transform.scale(Shopping, (largeur, hauteur))
    
    #mise en place de la musique
    musique_active('ComingOST.mp3')

    #définition des boutons du monde 1
    retour = pygame.Rect(0.03*largeur, 0.03*hauteur, 0.08*largeur, 0.09*hauteur)
    liste_bout = [retour]
    

    #boucle du monde 1 qui arrête la précédente et continue tant qu'on ne clique pas sur la croix
    continuer = False
    continuer_world_one = False
    running = False
    continuer_soon = False
    continuer_profil = False
    continuer_shop = True
    pygame.time.delay(1)
    pygame.display.flip()
    
    #affichage des vehicules achetés
    voiture_actu, avion_actu = get_vehicules_actu(id_profil)
    for slot in liste_slots[0]:
        if slot.get_cible() == voiture_actu:
            slot.set_img(pygame.image.load("BslotEquipe.png"))
            pass
    for slot in liste_slots[1]:
        if slot.get_cible() == avion_actu:
            slot.set_img(pygame.image.load("BslotEquipe.png"))
            pass
    
    cursor.execute("SELECT id_voiture FROM inventaire WHERE id_profil = ?", (id_profil,))
    voitures_achetes = cursor.fetchone()[0]
    voitures_achetes = json.loads(voitures_achetes)
    for voit in voitures_achetes :
        for slots in liste_slots[0] :
            if voit == slots.get_cible() :
                slots.set_img(pygame.image.load("BslotBuy.png"))
    cursor.execute("SELECT id_avion FROM inventaire WHERE id_profil = ?", (id_profil,))
    avions_achetes = cursor.fetchone()[0]
    avions_achetes = json.loads(avions_achetes)
    for avion in avions_achetes :
        for slots in liste_slots[1] :
            if avion == slots.get_cible() :
                slots.set_img(pygame.image.load("BslotBuy.png"))
    
    while continuer_shop:
        #affichage du fond d'écran
        plateau.blit(Shopping, (0, 0))
        
        
        for bouton in liste_boutons[3] : #bouton retour
            plateau.blit(bouton.img, (bouton.get_x(), bouton.get_y()))
        for slot in liste_slots[0] : #boutons cadenas voitures
            plateau.blit(slot.img, (slot.get_x(), slot.get_y()))
        for slotA in liste_slots[1] : #boutons cadenas avions
            plateau.blit(slotA.img, (slotA.get_x(), slotA.get_y()))
            
            
        #affichage du rectangle des boutons (utile pour créer les pochains mondes)
        #for bouton in liste_bout :
            #pygame.draw.rect(plateau, (200, 200, 200), bouton)

        #récupération de tous les évènements captés par la fenêtre
        for event in pygame.event.get():

            #si l'utilisateur a cliqué sur la croix
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #si l'utilisateur a cliqué dans la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Bretour.get_rect().collidepoint(event.pos): #retour en arrière 
                    profilMenu(id_profil)
                for ligne in liste_slots:
                    for slot in ligne :
                        if slot.get_rect().collidepoint(event.pos):
                            if slot.get_cible() < 20:
                                vehicule, id_vehicule = "voiture", "id_voiture"
                            else :
                                vehicule, id_vehicule = "avion", "id_avion"
                            acheter(vehicule, id_vehicule, slot, id_profil)
                                
        pygame.display.flip()



def running_niveau(voiture_used, niveau_used, id_niv, fin_niveau):
    clock = pygame.time.Clock() #permet de définir un système d'horloge.
    #boucle faisant tourner un niveau
    while True :
        resultat = deroulement_niveau(voiture_used, niveau_used, id_niv, fin_niveau)
        clock.tick(20) #permet de limiter le nombre d'images par seconde
        
        if resultat == False or voiture_used.est_mort():
            worldone()
            continuer_world_one = True
            break
            
        for event in pygame.event.get():
            
            #si l'utilisateur a cliqué sur la croix
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            #si l'utilisateur a pressé la touche du saut (flèche du haut)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_ESCAPE:
                    pygame.key.set_repeat(1,20)
                    voiture_used.voiture_jump()
        
        pygame.display.flip()
                    


def worldone():
    '''
    Cette fonction fonctionne (xD) de la même manière que la précédente mais gère le monde 1 du jeu et appelle les fonctions gérant les
    niveaux. Elle lance aussi la musique de chaque niveau et leur temps de chargement. Une variable empêche chaque temps de chargement de
    rejouer à chaque fois, sauf si le joueur retourne au menu principal. Cette fonction permet aussi d'afficher les tokens de validation
    d'un niveau, et les auvegarde tant que le jeu n'est pas fermé où que le niveau n'est pas retenté puis perdu.
    '''
    global running, continuer, continuer_world_one, continuer_soon, niveau_used, replay, id_profil
    #chargement et redimension de l'image de fond de l'écran d'accueil
    WorldOne = langue_img("AtollTuto.png", "AtollTutoANG.png", "AtollTutoALL.png")
    WorldOne = pygame.transform.scale(WorldOne, (largeur, hauteur))
    
    #mise en place de la musique
    musique_active('DKislandOST.mp3')

    #définition des boutons du monde 1
    get_back = pygame.Rect(0.002*largeur, 0.48*hauteur, 0.17*largeur, 0.1*hauteur) #coordonnées en x, coordonnées en y, largeur, hauteur
    level1 = pygame.Rect(valide1.get_x(), valide1.get_y(), 0.03*largeur, 0.039*hauteur)
    level2 = pygame.Rect(valide2.get_x(), valide2.get_y(), 0.03*largeur, 0.039*hauteur)
    level3 = pygame.Rect(valide3.get_x(), valide3.get_y(), 0.03*largeur, 0.039*hauteur)
    level4 = pygame.Rect(valide4.get_x(), valide4.get_y(), 0.03*largeur, 0.039*hauteur)
    level5 = pygame.Rect(valide5.get_x(), valide5.get_y(), 0.03*largeur, 0.039*hauteur)
    level6 = pygame.Rect(valide6.get_x(), valide6.get_y(), 0.03*largeur, 0.039*hauteur)
    levelboss1 = pygame.Rect(0.43*largeur, 0.48*hauteur, 0.03*largeur, 0.039*hauteur)
    world2 = pygame.Rect(0.82*largeur, 0.48*hauteur, 0.17*largeur, 0.1*hauteur)
    liste_niv = [get_back, level1, level2, level3, level4, level5, level6, levelboss1, world2]
    
    #boucle du monde 1 qui arrête la précédente et continue tant qu'on ne clique pas sur la croix
    continuer = False
    continuer_world_one = True
    continuer_soon = False
    pygame.time.delay(1)
    pygame.display.flip()
    
    
    #validation du niveau
    cursor.execute('SELECT id_niveau FROM reussi WHERE id_profil=?', (id_profil,))
    niveau_reussi = cursor.fetchall()
    for valide in liste_valide :
        for niv in niveau_reussi :
            if valide.get_id_niv() == niv[0] :
                valide.set_reussi(True)
                
    
    while continuer_world_one:
        #affichage du fond d'écran et des symboles "valide"
        plateau.blit(WorldOne, (0, 0))
        for i in liste_valide :
            if i.get_reussi() == True :
                valide_img = pygame.transform.scale(i.get_img(), (0.035*largeur, 0.05*hauteur))
                plateau.blit(valide_img, (i.get_x(), i.get_y()))

        #affichage du rectangle des boutons (utile pour créer les pochains mondes)
        #for bouton in liste_niv :
            #pygame.draw.rect(plateau, (200, 200, 200), bouton)

        #récupération de tous les évènements captés par la fenêtre
        for event in pygame.event.get():

            #si l'utilisateur a cliqué sur la croix
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #si l'utilisateur a cliqué dans la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bouton in liste_niv :
                    if bouton.collidepoint(event.pos):
                        #print('detected', bouton)
                        
                        if bouton == get_back : #retour en arrière
                            replay = 1
                            plateau_accueil(id_profil)
                        elif bouton == world2 : #monde 2 (à venir)
                            commingsoon()
                
                        #les différents niveaux sont lancés
                        if bouton == level1 :
                            #pygame.mixer.music.load('IntrusionIndustrielle.mp3')
                            commingsoon()
                            voiture_used, niveau_used, id_niv, fin_niveau = Usine(list_voit, id_profil)
                            running_niveau(voiture_used, niveau_used, id_niv, fin_niveau)
                            valide1.set_reussi('en cours')
                        elif bouton == level2 :
                            musique_active('AssautSonore.mp3')
                            voiture_used, niveau_used, id_niv, fin_niveau = Concert(list_plane, id_profil)
                            running_niveau(voiture_used, niveau_used, id_niv, fin_niveau)
                            valide2.set_reussi('en cours')
                        elif bouton == level3 :
                            #pygame.mixer.music.load('EmbuchesBucheronnes.mp3')
                            commingsoon()
                            voiture_used, niveau_used, id_niv, fin_niveau = Scierie(list_voit, id_profil)
                            running_niveau(voiture_used, niveau_used, id_niv, fin_niveau)
                            valide3.set_reussi('en cours')
                        elif bouton == level4 :
                            if replay == 1:
                                for _ in range(50):
                                    plateau.blit(loadingpark, (0, 0)) #faux ecran de chargement pour flex
                                    pygame.display.flip()
                            replay = 0
                            musique_active('GrandeFuite.mp3')
                            voiture_used, niveau_used, id_niv, fin_niveau = Parc(list_plane, id_profil)
                            running_niveau(voiture_used, niveau_used, id_niv, fin_niveau)
                            valide4.set_reussi('en cours')
                        elif bouton == level5 :
                            #pygame.mixer.music.load('EcueillsCaillouteux.mp3')
                            voiture_used, niveau_used, id_niv, fin_niveau = Montagne(list_plane, id_profil)
                            running_niveau(voiture_used, niveau_used, id_niv, fin_niveau)
                            valide5.set_reussi('en cours')
                        elif bouton == level6 :
                            #pygame.mixer.music.load('AlguesAuRythme.mp3')
                            #pygame.mixer.music.play(-1)
                            voiture_used, niveau_used, id_niv, fin_niveau = Ocean(list_voit, id_profil)
                            running_niveau(voiture_used, niveau_used, id_niv, fin_niveau)
                            valide6.set_reussi('en cours')
                                                  
        pygame.display.flip() #actualise



def bonus(id_profil):
    '''
    Cette fonction gère l'affichage du menu des minis jeux qui arriveront prochainement, tels le lavage auto en cours de développement.
    Elle actualise constamment l'écran pour qu'il s'affiche, lance une musique de fond et définie des boutons, qui sont juste des zones
    de hitbox par dessus les dessins. Pour chaque bouton elle appelle une autre fonction affichant un autre écran, et se désactivera
    d'elle même, grâce à des variables.
    '''
    global running
    #chargement et redimension de l'image de fond de l'écran d'accueil 
    fond_bonus = pygame.image.load("Challenge.png")
    fond_bonus = pygame.transform.scale(fond_bonus, (largeur, hauteur))
    musique_active('BonusOST.mp3')

    #définition des boutons qui serviront à lancer le jeu
    retour = pygame.Rect(0.04*largeur, 0.35*hauteur, largeur/18, hauteur/9) #coordonnées en x, coordonnées en y, largeur, hauteur
    lavage = pygame.Rect(0.24*largeur, 0.56*hauteur, largeur/11, hauteur/9)
    flappy = pygame.Rect(0.31*largeur, 0.34*hauteur, largeur/11, hauteur/9)
    liste_boutons = [retour, lavage, flappy]

    #boucle de la page d'accueil qui continue tant qu'on ne clique pas sur la croix
    continuer_bonus = True
    continuer_world_one = False
    continuer = False
    continuer_soon = False
    continuer_load = False
    pygame.time.delay(1)
    pygame.display.flip()
    
    cursor.execute("SELECT high_score FROM record WHERE id_profil = ? and id_mini = ?", (id_profil,2))
    score = cursor.fetchone()
    if score == None:
        score = 0
    else :
        score = score[0]
    
    while continuer_bonus:
        #affichage du fond d'écran
        plateau.blit(fond_bonus, (0, 0))
        afficher_record_flappy(score, 'bonus')

        #affichage du rectangle des boutons (pour en créer)
        #for bouton in liste_boutons :
            #pygame.draw.rect(plateau, (200, 200, 200), bouton)

        #récupération de tous les évènements captés par la fenêtre
        for event in pygame.event.get():
            
            #si l'utilisateur a cliqué sur la croix
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #si l'utilisateur a cliqué dans la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:
                #si le clic a été fait à la position d'un bouton (tout les boutons seront définis plus tard)
                for bouton in liste_boutons :
                    if bouton.collidepoint(event.pos):
                        #print('detected', bouton)
                        if bouton == retour :
                            plateau_accueil(id_profil)
                        elif bouton == lavage :
                            commingsoon()
                            #LavageEcran()
                        elif bouton == flappy :
                            continuer_bonus = False
                            minijeu2 = True
                            running_flappy(id_profil)
        pygame.display.flip() #actualise
        
    
def commingsoon():
    '''
    Cette fonction fonctionne (on le répètera jamais assez) comme les deux précédentes, et permet d'afficher l'écran Comming Soon, que l'on
    appelle pour toutes les sections du jeu prévues mais non commencées ou qui sont encore en phase de "ressemble à rien".
    '''
    global running, continuer, continuer_world_one, continuer_soon
    #chargement et redimension de l'image de fond de l'écran d'accueil
    CommSoon = pygame.image.load("ComingSoon.png")
    CommSoon = pygame.transform.scale(CommSoon, (largeur, hauteur))
    
    #mise en place de la musique
    musique_active('ComingOST.mp3')

    #définition des boutons du monde 1
    retour = pygame.Rect(0.002*largeur, 0.002*hauteur, 0.08*largeur, 0.08*hauteur) #coordonnées en x, coordonnées en y, largeur, hauteur
    liste_bout = [retour]
    

    #boucle du monde 1 qui arrête la précédente et continue tant qu'on ne clique pas sur la croix
    continuer = False
    continuer_world_one = False
    running = False
    continuer_soon = True
    pygame.time.delay(1)
    pygame.display.flip()
    
    while continuer_soon:
        #affichage du fond d'écran
        plateau.blit(CommSoon, (0, 0))

        #affichage du rectangle des boutons (utile pour créer les pochains mondes)
        #for bouton in liste_bout :
            #pygame.draw.rect(plateau, (200, 200, 200), bouton)

        #récupération de tous les évènements captés par la fenêtre
        for event in pygame.event.get():

            #si l'utilisateur a cliqué sur la croix
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #si l'utilisateur a cliqué dans la fenêtre
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bouton1 in liste_bout :
                    if bouton1.collidepoint(event.pos):
                        print('detected', bouton1)
                        if bouton1 == retour : #retour en arrière
                            plateau_accueil(id_profil)
        pygame.display.flip()
        

loading = pygame.image.load("LoadingScreen.png")
loading = pygame.transform.scale(loading, (largeur, hauteur))
loadingpark = pygame.image.load("LoadingPark.png")
loadingpark = pygame.transform.scale(loadingpark, (largeur, hauteur))

#mise en place de la musique
musique_active('Trunk.mp3')

#ces variables vont servir à gérer l'affichage de chaque écran du jeu ainsi que des temps de chargement pour flex.
continuer = False
continuer_world_one = False
running = False
continuer_soon = False
premier = 0
replay = 1
print("Pour plus de rensignements, ou si vous souhaitez nous aider, jetez donc un œil à https://raakipedia.miraheze.org/wiki/Accueil, le wiki de notre jeu, hébergé sur Miraheze !") 
ecran_connexion()
