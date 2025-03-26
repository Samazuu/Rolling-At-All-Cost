import pygame
import sqlite3
from random import*
from time import*
from aimages import*
from aobjets import*
from aclass import*
from afonctions import*


conn = sqlite3.connect('RAACbasedonnee.db')
cursor = conn.cursor()

clock = pygame.time.Clock() #permet de définir un système d'horloge.
FPS = 20


def taille_img(img):
    return pygame.transform.scale(img, (img.get_width()*largeur//1600, img.get_height()*hauteur//1000))


class Avion :
    #cette classe permet de définir comment fonctionne les avions jouables du jeu
    def __init__(self, x, y, img, imgActu):
        #le constructeur
        self.x = x
        self.y = y
        self.img = img
        self.imgActu = taille_img(imgActu)
        self.rect = self.imgActu.get_rect(topleft=(0, 0), size=(largeur_img(self.imgActu), hauteur_img(self.imgActu)))
        self.timejumping = 6
        self.timesprite = 0
        self.vie = True
    
    #les getters
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_img(self):
        return self.img
    def get_imgActu(self):
        return self.imgActu
    def get_rect(self):
        return self.rect
    def get_vie(self):
        return self.vie
    
    #les setters
    def set_x(self, newx):
        self.x = newx
    def set_y(self, newy):
        self.y = newy
    def set_img(self, newimg):
        self.img = newimg
    def set_imgActu(self, newimgActu):
        self.imgActu = taille_img(newimgActu)
    def set_rect(self, newrect):
        self.rect = newrect
    def set_vie(self, newvie):
        self.vie = newvie

        
    def animer(self):
        '''
        Cette méthode gère les sprites de la voiture et l'avion, en fonction de la variable "timesprite". Elle permet aussi
        de faire augmenter de 1 la valeur de ces variables. Cette valeur est réinitialisée si nécessaire par "
        compteur_sprite_avion()".
        '''
        self.timesprite += 1
        if self.timesprite == 12 :
            self.timesprite = 0
            
        elif self.timesprite == 0 :
            self.set_imgActu(self.img[0])
        elif self.timesprite == 2 :
            self.set_imgActu(self.img[1])
        elif self.timesprite == 4 :
            self.set_imgActu(self.img[2])
        elif self.timesprite == 6 :
            self.set_imgActu(self.img[3])
        elif self.timesprite == 8 :
            self.set_imgActu(self.img[2])
        elif self.timesprite == 10 :
            self.set_imgActu(self.img[1])
    
    def draw_plane(self):
        '''
        Cette méthode permet au programme d'afficher les véhicules, autrement ils n'apparaitraient jamais ! En fonction des informations qu'elle
        reçoit des autres méthodes (saut, en l'air, descente, ou état normal) elle modifie la position du véhicule chaque seconde et met à jour
        l'écran.
        '''
        self.timejumping +=1
        if self.timejumping<=1:                         #il saute
            self.set_y(self.get_y() - hauteur*0.011)
        elif self.get_y() < hauteur :              #il tombe
            self.set_y(self.get_y() + hauteur*0.018)
        else :
            self.timejumping = -1
        plateau.blit(self.imgActu, (self.get_x(), self.get_y()))


    def collision(self, liste_tours):
        '''
        Cette méthode permet de gérer les collisons entre les véhicules et leur environnement. Elle s'occupe de chaque cas et vérifie en permancence
        une liste contenant chaque obstacles du jeu pour vérifier si l'un d'eux touche le véhicule. Un pique enlève une vie, et la méthode sort aussi
        la variable "timesprite" de son cycle pour provoquer une "blessure". L'image du véhicule blessé est affiché. Pendant ce délai, la valeurs
        de la variable empêche cette fonction d'infliger de dégâts. Un carré est un obstacle sur lequel on peut rouler, mais se le prendre de
        face tue instantannément et règle les vies à zéro. Pour l'avion, toucher le sol le fait rebondir et perdre une vie, et sortir de l'image
        par en haut le tue instantannément. Chaque cas est réglé par des if, et lorsque les pv atteignent zéro, le joueur est renvoyé au menu
        principal (animation à venir).
        '''
        
        #protège le véhicule de dégats infinis (frame d'invincibilité)
        if self.timesprite < 13 :
            for t in liste_tours :
                if self.rect.colliderect(t.rect) :
                    self.vie = False
                    self.mort()
                
                
    def mort(self):
        self.set_imgActu(pygame.image.load('BoingOuch.png'))
        for i in range(FPS):
            pygame.display.flip()
            plateau.blit(Mapyork.img, (Mapyork.get_x(), Mapyork.get_y()))
            plateau.blit(self.imgActu, (self.get_x(), self.get_y()))
            clock.tick(FPS)

    
class Tours :
    #cette classe va définir des tours pour le mini jeu FlappyTour
    def __init__(self, img, y, x = largeur, compteur = 0):
        self.img = taille_img(img)
        self.x = x
        self.y = y
        self.compteur = compteur
        self.compteur_distance = 0
        self.difficulte = 0.3
        
    def get_img(self):
        return self.img
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_rect(self):
        return self.rect
    def get_compteur(self):
        return self.compteur
    def get_difficulte(self):
        return self.difficulte
    
    def set_img(self, newimg):
        self.img = taille_img(newimg)
    def set_x(self, newx):
        self.x = newx
    def set_y(self, newy):
        self.y = newy
    def set_rect(self, newrect):
        self.rect = newrect
    def set_compteur(self, newcompteur):
        self.compteur = newcompteur   
    def set_difficulte(self, newdifficulte):
        self.difficulte = newdifficulte
    

    def creer(self, score, liste_tours):
        self.compteur_distance += 1
        self.compteur += 1
        self.y1 = -hauteur*uniform(0, 0.5)
        self.y2 = self.y1 + hauteur*self.difficulte + self.img.get_height()
        
        if self.compteur_distance == 51 :
            self.compteur_distance = 0
            if self.difficulte > 0.18 :
                self.difficulte = self.difficulte*0.98
            Mapyork.set_speed(Mapyork.get_speed()*1.05)
            
        elif self.compteur_distance == 50 :
            liste_tours.append(Tours(pygame.image.load("ToursRetourne.png"), self.y1))
            liste_tours.append(Tours(pygame.image.load("Tours.png"), self.y2))
            score += 1
            
        if self.compteur == 100 :
            self.compteur = 0
            del self
            
        return score
        
    def detruction_ultime(self):
        del self

BoingBoeing = Avion(largeur/10, hauteur/5, [pygame.image.load('Boing.png'), pygame.image.load('Boing2.png'), pygame.image.load('Boing3.png'), pygame.image.load('Boing4.png'), pygame.image.load('BoingOuch.png')], pygame.image.load('Boing.png'))
#OrLine = Avion(largeur/10, hauteur/5, [pygame.image.load('AvOrange.png'), pygame.image.load('AvOrange2.png'), pygame.image.load('AvOrange3.png'), pygame.image.load('AvOrange4.png'), pygame.image.load('BoingOuch.png')], pygame.image.load('AvOrange.png'))
#AvViolet = Avion(largeur/10, hauteur/5, [pygame.image.load('AvViolet.png'), pygame.image.load('AvViolet2.png'), pygame.image.load('AvViolet3.png'), pygame.image.load('AvViolet4.png'), pygame.image.load('BoingOuch.png')], pygame.image.load('AvViolet.png'))
#list_plane = [BoingBoeing, OrLine, AvViolet]

to = Tours(pygame.image.load("Tours.png"), 0)


def deroulement_flappy(BoingBoeing, liste_tours):
    '''
    '''
    pygame.display.update() #actualise
    if Mapyork.get_x() <= -Mapyork.img.get_width()//3 :
        Mapyork.set_x(-Mapyork.get_speed())
    plateau.blit(Mapyork.img, (Mapyork.get_x(), Mapyork.get_y())) #affiche le décor
    Mapyork.set_x(Mapyork.get_x() - Mapyork.get_speed()) #le décor bouge, et non la voiture !

    for t in liste_tours : #les carrés avancent avec le décor
        t.set_x(t.get_x() - Mapyork.get_speed())
        t.set_rect(t.img.get_rect(topleft=(t.get_x(), t.get_y())))
        plateau.blit(t.img, (t.get_x(), t.get_y()))
        #pygame.draw.rect(plateau,(255,255,0),t.get_rect()) #affiche la colision des obstacles cubiques



    #appel des fonctions qui affichent la voiture
    sizev = (BoingBoeing.imgActu.get_width()*0.5, BoingBoeing.imgActu.get_height()*0.4)
    topleftv = (BoingBoeing.get_x()+BoingBoeing.imgActu.get_width()*0.3, BoingBoeing.get_y()+BoingBoeing.imgActu.get_height()*0.3)
    BoingBoeing.set_rect(BoingBoeing.imgActu.get_rect(topleft=topleftv, size=sizev))
    
    BoingBoeing.draw_plane()
    BoingBoeing.animer()
    BoingBoeing.collision(liste_tours)

    
    
minijeu2 = True

def running_flappy(id_profil):
    liste_tours = []
    BoingBoeing.set_vie(True)
    to.set_difficulte(0.3)
    Mapyork.set_speed(20)
    score = -2
    clock = pygame.time.Clock() #permet de définir un système d'horloge.
    #boucle faisant tourner un niveau
    while True :
        clock.tick(20) #permet de limiter le nombre d'images par seconde
        score = Tours.creer(to, score, liste_tours)
        deroulement_flappy(BoingBoeing, liste_tours)
        
        if not BoingBoeing.get_vie():
            for i in liste_tours:
                i.detruction_ultime()
            record_enregistre(id_profil, score)
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
                    BoingBoeing.timejumping = 0
        
        pygame.display.flip()

    
        

def record_enregistre(id_profil, score):
    if score < 0 :
        score = 0
    cursor.execute('SELECT id_mini FROM record WHERE id_profil=?', (id_profil,))
    if (2,) in cursor.fetchall(): #si tu as deja joué au jeu
        cursor.execute('SELECT high_score FROM record WHERE id_profil=?', (id_profil,))
        high_score = cursor.fetchone()[0]
        if score > high_score :
            cursor.execute('UPDATE record SET high_score=? WHERE id_profil=? AND id_mini=?', (score, id_profil, 2))
    else :
        cursor.execute('INSERT INTO record VALUES  (?, ?, ?)', (2, id_profil, score))
    conn.commit()
        
