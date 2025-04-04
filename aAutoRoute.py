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
def taille_img_cursed(img):
    return pygame.transform.scale(img, (img.get_width()*largeur//1510, img.get_height()*hauteur//1000))


class Voiture_haut :
    #cette classe permet de définir comment fonctionne les personnages jouables du jeu
    def __init__(self, x, y, img, imgActu):
        #le constructeur
        self.x = x
        self.y = y
        self.img = img
        self.imgActu = taille_img(imgActu)
        self.rect = self.imgActu.get_rect(topleft=(0, 0), size=(largeur_img(self.imgActu), hauteur_img(self.imgActu)))
        self.timejumping = 6
        self.timesprite = 0
    
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
    

    def a_droite(self):
        '''
        Cette méthode gère les sprites de la voiture, en fonction de la variable "timesprite" et "timesprite_avion". Elle permet aussi
        de faire augmenter de 1 la valeur de ces variables. Cette valeur est réinitialisée si nécessaire par "compteur_sprite()".
        '''
        if self.get_x() < largeur*0.68 :
            self.timesprite += 1
            if 0 <= self.timesprite < 15 :
                self.set_imgActu(self.img[1])
                self.set_x(self.get_x() + largeur*0.01)
            else :
                self.timesprite = -1
            
    
    def a_gauche(self):
        '''
        Cette méthode gère les sprites de la voiture, en fonction de la variable "timesprite" et "timesprite_avion". Elle permet aussi
        de faire augmenter de 1 la valeur de ces variables. Cette valeur est réinitialisée si nécessaire par "compteur_sprite()".
        '''
        if self.get_x() > largeur*0.28 :
            self.timesprite += 1
            if 0 <= self.timesprite < 15 :
                self.set_imgActu(self.img[2])
                self.set_x(self.get_x() - largeur*0.01)
            else :
                self.timesprite = -1
    
    
    def draw_car(self):
        '''
        Cette méthode permet au programme d'afficher les véhicules, autrement ils n'apparaitraient jamais ! En fonction des informations qu'elle
        reçoit des autres méthodes (saut, en l'air, descente, ou état normal) elle modifie la position du véhicule chaque seconde et met à jour
        l'écran.
        '''
        if self.get_x() <= largeur*0.35 :
            self.set_imgActu(self.img[1])
        elif self.get_x() >= largeur*0.65 :
            self.set_imgActu(self.img[2])
        else: 
            self.set_imgActu(self.img[0])
        plateau.blit(self.imgActu, (self.get_x(), self.get_y()))
        

    def collision(self, liste_ennemi):
        '''
        Cette méthode permet de gérer les collisons entre les véhicules et leur environnement. Elle s'occupe de chaque cas et vérifie en permancence
        une liste contenant chaque obstacles du jeu pour vérifier si l'un d'eux touche le véhicule. Un pique enlève une vie, et la méthode sort aussi
        la variable "timesprite" de son cycle pour provoquer une "blessure". L'image du véhicule blessé est affiché. Pendant ce délai, la valeurs
        de la variable empêche cette fonction d'infliger de dégâts. Un carré est un obstacle sur lequel on peut rouler, mais se le prendre de
        face tue instantannément et règle les vies à zéro. Pour l'avion, toucher le sol le fait rebondir et perdre une vie, et sortir de l'image
        par en haut le tue instantannément. Chaque cas est réglé par des if, et lorsque les pv atteignent zéro, le joueur est renvoyé au menu
        principal (animation à venir).
        '''        
        for e in liste_ennemi :
            if self.rect.colliderect(e.rect) :
                self.vie = False
                self.mort()
                
                
    def mort(self):
        self.set_imgActu(pygame.image.load('SauterelleOuch.png'))
        for i in range(FPS):
            pygame.display.flip()
            plateau.blit(Maproute.img, (Maproute.get_x(), Maproute.get_y()))
            plateau.blit(self.imgActu, (self.get_x(), self.get_y()))
            clock.tick(FPS)


class Ennemi:
    def __init__(self, img, x, y = -hauteur*0.2):
        self.img = taille_img(img)
        self.x = x
        self.y = y
        self.compteur = 0
        self.compteur_distance = 0
        self.difficulte = 0
        
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
    

    def creer(self, score, liste_ennemi):
        self.compteur_distance += 1
        self.compteur += 1
        self.x1 = largeur*0.3 + largeur*0.12*randint(0, 3)
        
        if self.compteur_distance == 101 - self.difficulte :
            self.compteur_distance = 0
            if self.difficulte < 50 :
                self.difficulte += 1
            Maproute.set_speed(Maproute.get_speed()*1.1)
            
        elif self.compteur_distance == 100 - self.difficulte :
            if self.get_x() <= largeur*0.3 :
                img = pygame.image.load("Camion1d.png")
            elif self.get_x() >= largeur*0.7 :
                img = pygame.image.load("Camion1g.png")
            else: 
                img = pygame.image.load("Camion1m.png")
            liste_ennemi.append(Ennemi(img, self.x1))
            score += 1
            
        if self.compteur == 100 - self.difficulte :
            self.compteur = 0
            del self
            
        return score
        
    def detruction_ultime(self):
        del self


Sauteroule = Voiture_haut(largeur*0.55, hauteur*0.8, [pygame.image.load('SauterelleHautm.png'), pygame.image.load('SauterelleHautd.png'), pygame.image.load('SauterelleHautg.png')], pygame.image.load('SauterelleHautm.png'))
enn = Ennemi(pygame.image.load("Camion1m.png"), largeur*0.5)

liste_ennemi = [enn]

def deroulement_route(Sauteroule, liste_ennemi):
    '''
    '''
    pygame.display.update() #actualise
    if Maproute.get_y() >= 0:
        Maproute.set_y(-hauteur)
    plateau.blit(Maproute.get_img(), (Maproute.get_x(), Maproute.get_y())) #affiche le décor puis anime le décor
    Maproute.set_y(Maproute.get_y() + Maproute.get_speed()) #le décor bouge, et non la voiture !


    for e in liste_ennemi : #les ennemis avancent avec le décor
        e.set_y(e.get_y() + Maproute.get_speed())
        e.set_rect(e.img.get_rect(topleft=(e.get_x(), e.get_y())))
        plateau.blit(e.img, (e.get_x(), e.get_y()))
        #pygame.draw.rect(plateau,(255,255,0),e.get_rect()) #affiche la colision des obstacles ennemi



    #appel des fonctions qui affichent la voiture
    sizev = (Sauteroule.imgActu.get_width()*0.5, Sauteroule.imgActu.get_height()*0.4)
    topleftv = (Sauteroule.get_x()+Sauteroule.imgActu.get_width()*0.3, Sauteroule.get_y()+Sauteroule.imgActu.get_height()*0.3)
    Sauteroule.set_rect(Sauteroule.imgActu.get_rect(topleft=topleftv, size=sizev))
    
    Sauteroule.draw_car()
    Sauteroule.collision(liste_ennemi)

    
    
minijeu2 = True

def running_route(id_profil):
    liste_ennemi = []
    Sauteroule.set_vie(True)
    Sauteroule.set_x(largeur*0.55)
    enn.set_difficulte(0)
    Maproute.set_speed(5)
    score = -2
    clock = pygame.time.Clock() #permet de définir un système d'horloge.
    animer_tourne_d = 0
    animer_tourne_g = 0
    Maproute.set_y(hauteur)
    #boucle faisant tourner un niveau
    while True :
        clock.tick(200) #permet de limiter le nombre d'images par seconde
        score = Ennemi.creer(enn, score, liste_ennemi)
        deroulement_route(Sauteroule, liste_ennemi)
        
        animer_tourne_d -= 1
        if animer_tourne_d > 0:
            Sauteroule.a_droite()
        animer_tourne_g -= 1
        if animer_tourne_g > 0:
            Sauteroule.a_gauche()
        
        if not Sauteroule.get_vie():
            for e in liste_ennemi:
                e.detruction_ultime()
            record_enregistre(id_profil, score)
            break
            
        for event in pygame.event.get():
            #si l'utilisateur a cliqué sur la croix
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            #si l'utilisateur a pressé la touche du saut (flèche du haut)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    animer_tourne_g = 17
                elif event.key == pygame.K_RIGHT :
                    animer_tourne_d = 17
        
        pygame.display.flip()

    
        

def record_enregistre(id_profil, score):
    if score < 0 :
        score = 0
    cursor.execute('SELECT id_mini FROM record WHERE id_profil=?', (id_profil,))
    if (3,) in cursor.fetchall(): #si tu as deja joué au jeu
        cursor.execute('SELECT high_score FROM record WHERE id_profil=?', (id_profil,))
        high_score = cursor.fetchone()[0]
        if score > high_score :
            cursor.execute('UPDATE record SET high_score=? WHERE id_profil=? AND id_mini=?', (score, id_profil, 3))
    else :
        cursor.execute('INSERT INTO record VALUES  (?, ?, ?)', (3, id_profil, score))
    conn.commit()
