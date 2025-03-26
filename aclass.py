import pygame
from aimages import*

pygame.init()
info = pygame.display.Info()
largeur, hauteur = info.current_w,info.current_h

def taille_img(img):
    return pygame.transform.scale(img, (img.get_width()*largeur//1600, img.get_height()*hauteur//1000))
def largeur_img(img):
    return img.get_width()*largeur//1600
def hauteur_img(img):
    return img.get_height()*hauteur//1000

class Decor :
    #cette classe défini le décor
    def __init__(self, img = pygame.image.load('Ocean.png'), niveau = 10, x=0, y=0, speed=largeur/100, sol=hauteur*0.74):
        self.speed = speed
        self.img = img
        self.img = pygame.transform.scale(img, (img.get_width()*largeur//1970, hauteur))
        self.x = x
        self.y = y
        self.sol = sol 
        self.niveau = niveau
        
    def get_speed(self):
        return self.speed
    def get_img(self):
        return self.img
    def get_niveau(self):
        return self.niveau
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_sol(self):
        return self.sol
    
    def set_speed(self, newspeed):
        self.speed = newspeed
    def set_img(self, newimg):
        self.img = pygame.transform.scale(newimg, (newimg.get_width()*1300//largeur, hauteur))
    def set_niveau(self, newniveau):
        self.niveau = newniveau        
    def set_x(self, newx):
        self.x = newx
    def set_y(self, newy):
        self.y = newy
    def set_sol(self, newsol):
        self.sol = newsol
        

class Obstacle :
    #cette classe défini les obstacles de type 'pique'
    #les piques enlèvent une vie
    def __init__(self, img, x, y):
        self.img = img
        self.img = taille_img(self.img)
        self.x = x
        self.y = y
        self.rect = self.img.get_rect(topleft=(self.get_x(), self.get_y()))
        
    def get_img(self):
        return self.img
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_rect(self):
        return self.rect
    
    def set_img(self, newimg):
        self.img = taille_img(newimg)
    def set_x(self, newx):
        self.x = newx
    def set_y(self, newy):
        self.y = newy
    def set_rect(self, newrect):
        self.rect = newrect
        
class Carre(Obstacle) :
    #cette classe défini les obstacles de type 'carré'
    #les carrés tuent instantanément mais on peut rouler par-dessus
    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        
        
class Rampe(Obstacle) :
    #cette classe défini les rampes, permettant de monter une pente (version descente à venir)
    def __init__(self, img, x, y):
        super().__init__(img, x, y)

class Piece(Obstacle) :
    #cette classe défini les rampes, permettant de monter une pente (version descente à venir)
    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        self.timesprite_piece = 0
        
    def animer(self):
        self.timesprite_piece += 1
        if self.timesprite_piece == 0 :
            self.set_img(pygame.image.load('piece.png'))
        elif self.timesprite_piece == 1 :
            self.set_img(pygame.image.load('piece1.png'))
        elif self.timesprite_piece == 2 :
            self.set_img(pygame.image.load('piece2.png'))
            self.timesprite_piece = -1

        
class Valide :
    #cette classe défini les symboles valide, permettant de montrer qu'un niveau est complété
    def __init__(self, img, x, y, id_niv, reussi = False):
        self.img = img
        self.img = taille_img(self.img)
        self.id_niv = id_niv
        self.x = x
        self.y = y
        self.reussi = reussi
        
    def get_img(self):
        return self.img
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_reussi(self):
        return self.reussi
    def get_id_niv(self):
        return self.id_niv
    
    def set_img(self, newimg):
        self.img = taille_img(newimg)
    def set_x(self, newx):
        self.x = newx
    def set_y(self, newy):
        self.y = newy
    def set_reussi(self, newreussi):
        self.reussi = newreussi
    def set_id_niv(self, newid_niv):
        self.id_niv = newid_niv


class Slot :
    #cette classe défini les slots du shop
    def __init__(self, img, x, y, cible, etat):
        self.img = img
        self.img = taille_img(self.img)
        self.x = x
        self.y = y
        self.cible = cible
        self.rect = self.img.get_rect(topleft=(self.get_x(), self.get_y()))
        self.etat = etat
        
    def get_img(self):
        return self.img
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_cible(self):
        return self.cible
    def get_rect(self):
        return self.rect
    def get_etat(self):
        return self.etat
    
    def set_img(self, newimg):
        self.img = taille_img(newimg)
    def set_x(self, newx):
        self.x = newx
    def set_y(self, newy):
        self.y = newy
    def set_cible(self, newcible):
        self.rect = newcible
    def set_rect(self, newrect):
        self.rect = newrect
    def set_etat(self, newetat):
        self.etat = newetat
        
        
class Trigger(Obstacle) :
    #cette classe va définir des déclencheurs d'animations lors des niveaux
    def __init__(self, img, x, y):
        super().__init__(img, x, y)


class Placeholder(Obstacle) :
    #cette classe va définir des déclencheurs d'animations lors des niveaux
    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        
        
class Langue_musique():
    def __init__(self, langue, musique):
        self.langue_active = langue
        self.musique = musique

    def get_langue_active(self):
        return self.langue_active
    def get_musique(self):
        return self.musique
    
    def set_langue_active(self, newlangue_active):
        self.langue_active = newlangue_active
    def set_musique(self, newmusique):
        self.musique = newmusique

langue = Langue_musique('francais', True)