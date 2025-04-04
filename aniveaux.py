import pygame
import sqlite3
from random import*
from time import*
import json
from aimages import*
from aobjets import*
from aclass import*
from afonctions import*


''' les differents niveaux : '''
#on modifie simplement la position ou les images des objets qu'on utilise
def Usine(list_voit, id_profil):
    '''
    Toutes les six fonctions suivantes suivent le même fonctionnement. Chacune gère un niveau, et une fois apellée, elle déplace les objets
    du niveau correspondant à leur place, ceux ci étant définis initialemments à gauche de l'écran, à l'extérieur.
    '''
    id_niv = 11
    niveau_used = Mapusine
    fin_niveau = 2
    niveau_used.set_x(0)
    niveau_used.set_sol(hauteur*0.74)
    voiture_used.set_x(largeur/10)
    voiture_used = list_voit[get_vehicules_actu(id_profil)[1]-10]
    voiture_used.set_pv(3)
    
    pique.set_x(largeur + 4500)
    pique1.set_x(largeur + 3000)
        
    rampe.set_x(largeur + 1000)
    rampe.set_y(0.7*hauteur)
        
    carre.set_x(largeur + 2500)
    carre1.set_x(largeur + 5000)
    carre2.set_x(largeur + 5500)
    
    return voiture_used, niveau_used, id_niv, fin_niveau
    
    
def Concert(list_plane, id_profil):
    '''
    Voir "Usine()"
    '''
    id_niv = 12
    niveau_used = Mapconcert
    niveau_used.set_x(0)
    niveau_used.set_sol(hauteur*0.75)
    fin_niveau = 2.8
    voiture_used = list_plane[get_vehicules_actu(id_profil)[1]-20]
    voiture_used.set_sol_avion(niveau_used.get_sol())
    voiture_used.set_x(largeur/10)
    voiture_used.set_y(hauteur*0.2)
    voiture_used.set_pv(3)
    
    
    fumee.set_x(largeur*0.6)
    fumee.set_y(hauteur*0.6)

    trigbouteille1.set_x(largeur*0.7)
    trigbouteille1.set_y(0)
    trigbouteille2.set_x(largeur*1)
    trigbouteille2.set_y(0)
    trigbouteille3.set_x(largeur*1.3)
    trigbouteille3.set_y(0)
    
    bouchon1.set_x(largeur*1.05)
    bouchon1.set_y(hauteur*1.5)
    bouchon2.set_x(largeur*1.3)
    bouchon2.set_y(hauteur*1.2)
    bouchon3.set_x(largeur*1.65)
    bouchon3.set_y(hauteur*1.5)
    
    piece1.set_x(largeur*1.1)
    piece1.set_y(hauteur*0.07)
    
    bouteille1.set_x(largeur*0.9)
    bouteille1.set_y(hauteur*1.2)
    bouteille2.set_x(largeur*1.2)
    bouteille2.set_y(hauteur*1.2)
    bouteille3.set_x(largeur*1.5)
    bouteille3.set_y(hauteur*1.2)
    
    barre1.set_x(largeur*1.9)
    barre1.set_y(0)
    piece2.set_x(largeur*2.1)
    piece2.set_y(hauteur*0.6)
    barre2.set_x(largeur*1.9)
    barre2.set_y(hauteur*0.55)
    barre3.set_x(largeur*2.2)
    barre3.set_y(0)
    barre4.set_x(largeur*2.2)
    barre4.set_y(hauteur*0.65)
    barre5.set_x(largeur*2.5)
    barre5.set_y(0)
    
    barre6.set_x(largeur*2.5)
    barre6.set_y(hauteur*0.65)
    barre7.set_x(largeur*2.8)
    barre7.set_y(0)
    barre8.set_x(largeur*2.8)
    barre8.set_y(hauteur*0.45)
    barre9.set_x(largeur*3.1)
    barre9.set_y(0)
    barre10.set_x(largeur*3.1)
    barre10.set_y(hauteur*0.65)
    
    musik10.set_x(largeur*3.5)
    musik10.set_y(hauteur*0)
    musik11.set_x(largeur*3.5)
    musik11.set_y(hauteur*0.63)
    piece3.set_x(largeur*3.7)
    piece3.set_y(hauteur*0.1)
    
    musik20.set_x(largeur*4.1)
    musik20.set_y(hauteur*0)
    musik21.set_x(largeur*4.1)
    musik21.set_y(hauteur*0.21)
    musik22.set_x(largeur*4.1)
    musik22.set_y(hauteur*0.63)
    
    musik30.set_x(largeur*4.7)
    musik30.set_y(hauteur*0.21)
    musik31.set_x(largeur*4.7)
    musik31.set_y(hauteur*0.42)
    musik32.set_x(largeur*4.7)
    musik32.set_y(hauteur*0.63)
    
    return voiture_used, niveau_used, id_niv, fin_niveau

def Scierie(list_voit, id_profil):
    '''
    Voir "Usine()"
    '''
    id_niv = 13
    niveau_used = Mapscierie
    niveau_used.set_x(0)
    niveau_used.set_sol(hauteur*0.77)
    fin_niveau = 1.75
    voiture_used = list_voit[get_vehicules_actu(id_profilid_profil)[0]-10]
    voiture_used.set_x(largeur/10)
    voiture_used.set_pv(3)
    
    pique.set_x(largeur + 4500)
    pique1.set_x(largeur + 3000)
    pique2.set_x(largeur + 3500)
    pique3.set_x(largeur + 4000)
    
    carre.set_x(largeur + 2500)
    carre1.set_x(largeur + 5000)
    carre2.set_x(largeur + 5500)
    carre3.set_x(largeur + 6500)
    
    return voiture_used, niveau_used, id_niv, fin_niveau


def Parc(list_plane, id_profil):
    '''
    Voir "Usine()"
    '''
    id_niv = 14
    niveau_used = Mappark
    niveau_used.set_x(0)
    niveau_used.set_sol(hauteur*0.77)
    fin_niveau = 0.75
    voiture_used = list_plane[get_vehicules_actu(id_profil)[1]-20]
    voiture_used.set_x(largeur/10)
    voiture_used.set_sol_avion(niveau_used.get_sol())
    voiture_used.set_y(hauteur*0.2)
    voiture_used.set_pv(3)
    
    bus.set_x(largeur*0.75)
    bus.set_y(hauteur*0.81)
    
    bienvenue.set_x(largeur*1.01)
    bienvenue.set_y(hauteur*0.35)
    pancarte.set_x(largeur*1.1)
    pancarte.set_y(hauteur*-0.03)
    
    waitline1.set_x(largeur*1.19)
    waitline1.set_y(hauteur*0.81)
    waitline2.set_x(largeur*1.21)
    waitline2.set_y(hauteur*0.81)
    waitline3.set_x(largeur*1.29)
    waitline3.set_y(hauteur*0.81)
    
    welcometower.set_x(largeur*1.33)
    welcometower.set_y(hauteur*0.61)
    blocktower.set_x(largeur*1.58)
    blocktower.set_y(hauteur*0.06)
    
    #la tour de chute 1 tombe
    trigDrop1.set_x(largeur*1.8)
    trigDrop1.set_y(0)
    
    #la tour de chute 2 tombe moins bas, puis plus bas
    trigDrop2.set_x(largeur*2.05)
    trigDrop2.set_y(hauteur /90 + 1)
    trigDrop21.set_x(largeur*2.15)
    trigDrop21.set_y(hauteur /90 + 1)
    
    #la tour de chute 3 descend et redescend pendant que le joueur est dessous
    trigDrop3.set_x(largeur*2.29)
    trigDrop3.set_y(0)
    trigDrop31.set_x(largeur*2.46)
    trigDrop31.set_y(0) 
    
    drop1.set_x(largeur*1.95)
    drop1.set_y(hauteur*0.21)
    drop2.set_x(largeur*2.23)
    drop2.set_y(hauteur*0.21)
    drop3.set_x(largeur*2.476)
    drop3.set_y(hauteur*0.21)
    
    planeR1.set_x(largeur*2.76)
    planeR1.set_y(hauteur*0.08)
    planeR2.set_x(largeur*2.93)
    planeR2.set_y(hauteur*0.21)
    planeR3.set_x(largeur*3)
    planeR3.set_y(hauteur*0.66)
    
    ferrisB.set_x(largeur*3.35)
    ferrisB.set_y(hauteur*0.77)
    granderoue.set_x(largeur*3.34)
    granderoue.set_y(hauteur*-0.3)
    
    station.set_x(largeur*4.13)
    station.set_y(hauteur*0.61)
    railsdebut.set_x(largeur*4.41)
    railsdebut.set_y(hauteur*0.78)
    trigCoast1.set_x(largeur*5.25)
    trigCoast1.set_y(0)
    trigCoastEnv.set_x(largeur*5.48)
    trigCoastEnv.set_y(0)
    trigCoastDroit.set_x(largeur*6.10)
    trigCoastDroit.set_y(0)
    coaster1.set_x(largeur*5.20)
    coaster1.set_y(hauteur*0.37)
    railmonte.set_x(largeur*5.0)
    railmonte.set_y(hauteur*0.44)
    rail1.set_x(largeur*5.21)
    rail1.set_y(hauteur*0.48)
    trigFeu1.set_x(largeur*5.10)
    trigFeu1.set_y(0)
    trigBoom1.set_x(largeur*5.15)
    trigBoom1.set_y(0)
    fusee1.set_x(largeur*5.38)
    fusee1.set_y(hauteur*0.78)
    trigRail1.set_x(largeur*5.38)
    trigRail1.set_y(0)
    railtombe1.set_x(largeur*5.54)
    railtombe1.set_y(hauteur*0.48)
    railenvers.set_x(largeur*5.90)
    railenvers.set_y(hauteur*0.001)
    trigCoast2.set_x(largeur*6.02)
    trigCoast2.set_y(0)
    canon.set_x(largeur*5.98)
    canon.set_y(hauteur*0.78)
    railtombe2.set_x(largeur*6.21)
    railtombe2.set_y(hauteur*0.48)
    trigRail2.set_x(largeur*6.14)
    trigRail2.set_y(0)
    rail2.set_x(largeur*6.51)
    rail2.set_y(hauteur*0.48)
    trigCoast3.set_x(largeur*6.53)
    trigCoast3.set_y(0)
    fusee2.set_x(largeur*6.70)
    fusee2.set_y(hauteur*0.78)
    fusee3.set_x(largeur*6.86)
    fusee3.set_y(hauteur*0.78)
    trigFeu2.set_x(largeur*6.45)
    trigFeu2.set_y(0)
    trigBoom2.set_x(largeur*6.55)
    trigBoom2.set_y(0)
    trigFeu3.set_x(largeur*6.68)
    trigFeu3.set_y(0)
    trigBoom3.set_x(largeur*6.78)
    trigBoom3.set_y(0)
    raildescend.set_x(largeur*7.05)
    raildescend.set_y(hauteur*0.43)
    railfrein.set_x(largeur*7.26)
    railfrein.set_y(hauteur*0.74)
    
    return voiture_used, niveau_used, id_niv, fin_niveau
    
def Montagne(list_plane, id_profil):
    '''
    Voir "Usine()"
    '''
    id_niv = 15
    niveau_used = Mapmontagne
    fin_niveau = 2
    niveau_used.set_x(0)
    niveau_used.set_sol(hauteur*0.77)
    voiture_used = list_plane[get_vehicules_actu(id_profil)[1]-20]
    voiture_used.set_x(largeur/10)
    voiture_used.set_sol_avion(niveau_used.get_sol())
    voiture_used.set_y(hauteur*0.2)
    voiture_used.set_pv(3)
    
    trigroc.set_x(largeur*0.8)
    trigroc.set_y(0)
    roc10.set_x(largeur*0.9)
    roc10.set_y(hauteur*0.7)
    roc11.set_x(largeur*1.4)
    roc11.set_y(hauteur*-0.05)
    roc20.set_x(largeur*1.3)
    roc20.set_y(hauteur*0.55)
    roc21.set_x(largeur*2)
    roc21.set_y(hauteur*0.5)
    roc12.set_x(largeur*2.1)
    roc12.set_y(hauteur*-0.05)
    roc22.set_x(largeur*2.4)
    roc22.set_y(hauteur*0.5)
    piece1.set_x(largeur*2.3)
    piece1.set_y(hauteur*0.05)
    
    volcan.set_x(largeur*2.8)
    volcan.set_y(hauteur*0.15)
    arbre.set_x(largeur*3.8)
    arbre.set_y(0)
    trigarbre.set_x(largeur*3.8)
    trigarbre.set_y(0)
    
    return voiture_used, niveau_used, id_niv, fin_niveau
    
def Ocean(list_voit, id_profil):
    '''
    Voir "Usine()"
    '''
    id_niv = 16
    niveau_used = Mapocean
    niveau_used.set_x(0)
    niveau_used.set_sol(hauteur*0.77)
    fin_niveau = 1.75
    voiture_used = list_voit[get_vehicules_actu(id_profil)[0]-10]
    voiture_used.set_x(largeur/10)
    voiture_used.set_pv(3)
        
    contener1.set_x(largeur*0.77)
    contener2.set_x(largeur*0.9)
    contener3.set_x(largeur*1.05)
    contener4.set_x(largeur*1.63)
    contener5.set_x(largeur*1.87)
    contener6.set_x(largeur*2.13)
    
    trigcont4.set_x(largeur*1.51)
    trigcont5.set_x(largeur*1.69)
    trigcont6.set_x(largeur*1.94)
    
    contener1.set_y(hauteur*0.75)
    contener2.set_y(hauteur*0.66)
    contener3.set_y(hauteur*0.731)
    contener4.set_y(hauteur*0.55)
    contener5.set_y(hauteur*0.55)
    contener6.set_y(hauteur*0.75)
    
    piece1.set_x(largeur*2.4)
    piece1.set_y(hauteur*0.45)
    
    balle.set_x(largeur*2.8)
    balle.set_y(hauteur*0.7)
    trigball.set_x(largeur*2.85)
    trigball.set_y(0)
    
    fougere.set_x(largeur*2.8)
    fougere.set_y(hauteur*0.74)
    para1.set_x(largeur*3.322)
    para1.set_y(hauteur*0.67)
    para2.set_x(largeur*3.973)
    para2.set_y(hauteur*0.67)
    
    piece2.set_x(largeur*3.6)
    piece2.set_y(hauteur*0.45)
    
    trigtide.set_x(largeur*4.32)
    coque.set_x(largeur*4.75)
    coque.set_y(hauteur*0.85)
    piece3.set_x(largeur*5)
    piece3.set_y(hauteur*0.6)
    
    algue1.set_x(largeur*5)
    algue1.set_y(hauteur - algue1.img.get_height())
    algue2.set_x(largeur*5.4)
    algue2.set_y(hauteur - algue2.img.get_height())
    rocher.set_x(largeur*5.7)
    rocher.set_y(hauteur - rocher.img.get_height())
    
    return voiture_used, niveau_used, id_niv, fin_niveau