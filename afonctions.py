import pygame
import sqlite3
from random import*
from time import*
import json
from aimages import*
from aobjets import*
from aclass import*

conn = sqlite3.connect('RAACbasedonnee.db')
cursor = conn.cursor()



def musique_active(song):
    if langue.get_musique() == True:
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()
        
def langue_img(img_fr, img_ang, img_all):
    if langue.get_langue_active() == 'francais':
        return pygame.image.load(img_fr)
    elif langue.get_langue_active() == 'anglais':
        return pygame.image.load(img_ang)
    elif langue.get_langue_active() == 'allemand':
        return pygame.image.load(img_all)
    

def afficher_record_flappy(score, ecran):
    pygame.font.init()
    score_display = pygame.font.Font("Wonderly.otf", hauteur//18).render(str(score), 0, (255, 100, 0))
    if ecran == 'profilMenu':
        nom_jeu = pygame.font.Font("Wonderly.otf", hauteur//20).render('FlappyTours', 0, (255, 100, 0))
        plateau.blit(nom_jeu, (largeur*0.84, hauteur*0.38))
        plateau.blit(score_display, (largeur*0.9, hauteur*0.46))
    else :
        mot_score = pygame.font.Font("Wonderly.otf", hauteur//18).render('score :', 0, (255, 100, 0))
        plateau.blit(mot_score, (largeur*0.17, hauteur*0.22))
        plateau.blit(score_display, (largeur*0.28, hauteur*0.22))
        

def niveau_reussi(est_reussi, id_profil, temp_piece, id_niv):
    if est_reussi == None :
        cursor.execute('INSERT INTO reussi VALUES  (?, ?, ?, ?, ?)', (id_niv, id_profil, temp_piece[0], temp_piece[1], temp_piece[2]))
        cursor.execute('SELECT nb_pieces FROM profil WHERE id_profil=? ', (id_profil,))
        get_pieces = cursor.fetchone()[0]
        cursor.execute('UPDATE profil SET nb_pieces=? WHERE id_profil=? ', (temp_piece[0]+temp_piece[1]+temp_piece[2]+get_pieces, id_profil))
        conn.commit()
    else :
        cursor.execute('SELECT * FROM reussi WHERE id_niveau=? AND id_profil=? ', (id_niv, id_profil))
        pieces_got = cursor.fetchmany()[0]
        
        piece1_got = pieces_got[2]
        piece2_got = pieces_got[3]
        piece3_got = pieces_got[4]
        
        if temp_piece[0]==1 and piece1_got==0:
            cursor.execute('UPDATE reussi SET piece1=? WHERE id_niveau=? AND id_profil=? ', (1, id_niv, id_profil))
            cursor.execute('SELECT nb_pieces FROM profil WHERE id_profil=? ', (id_profil,))
            get_pieces = cursor.fetchone()[0]
            cursor.execute('UPDATE profil SET nb_pieces=? WHERE id_profil=? ', (get_pieces+1, id_profil))
            
        if temp_piece[1]==1 and piece2_got==0:
            cursor.execute('UPDATE reussi SET piece2=? WHERE id_niveau=? AND id_profil=? ', (1, id_niv, id_profil))
            cursor.execute('SELECT nb_pieces FROM profil WHERE id_profil=? ', (id_profil,))
            get_pieces = cursor.fetchone()[0]
            cursor.execute('UPDATE profil SET nb_pieces=? WHERE id_profil=? ', (get_pieces+1, id_profil))
            
        if temp_piece[2]==1 and piece3_got==0:
            cursor.execute('UPDATE reussi SET piece3=? WHERE id_niveau=? AND id_profil=? ', (1, id_niv, id_profil))
            cursor.execute('SELECT nb_pieces FROM profil WHERE id_profil=? ', (id_profil,))
            get_pieces = cursor.fetchone()[0]
            cursor.execute('UPDATE profil SET nb_pieces=? WHERE id_profil=? ', (get_pieces+1, id_profil))
            
        conn.commit()
        

def draw_life(voiture_used):
        if voiture_used.get_pv() == 3:
            LifeBar.set_img(LifeBarFulli)
        elif voiture_used.get_pv() == 2:
            LifeBar.set_img(LifeBarHalfi)
        elif voiture_used.get_pv() == 1:
            LifeBar.set_img(LifeBarCritici)
        elif voiture_used.get_pv() == 0:
            LifeBar.set_img(NoMoreLifei)
        else:
            LifeBar.set_img(LifeBarNotLogici)
        plateau.blit(LifeBar.img, (LifeBar.get_x(), LifeBar.get_y()))
        
                        
def get_vehicules_actu(id_profil):
    cursor.execute("SELECT voiture FROM vehicule_actu WHERE id_profil = ?", (id_profil,))
    voiture_actu = cursor.fetchone()[0]
    cursor.execute("SELECT avion FROM vehicule_actu WHERE id_profil = ?", (id_profil,))
    avion_actu = cursor.fetchone()[0]
    return voiture_actu, avion_actu


def acheter(vehicule, id_vehicule, slot, id_profil):
    cursor.execute(f'SELECT {id_vehicule} FROM inventaire WHERE id_profil=? ', (id_profil,))
    vehicule_achetes = cursor.fetchone()
    vehicule_achetes = vehicule_achetes[0]
    vehicule_achetes = json.loads(vehicule_achetes)
    
    if slot.get_cible() not in vehicule_achetes :
        cursor.execute("SELECT nb_pieces FROM profil WHERE id_profil = ?", (id_profil,))
        nb_piece = cursor.fetchone()[0]
        if nb_piece >= 1 :
            cursor.execute('UPDATE profil SET nb_pieces=? WHERE id_profil=? ', (nb_piece-1, id_profil))
            vehicule_achetes.append(slot.get_cible())
            cursor.execute(f'UPDATE inventaire SET {id_vehicule}=? WHERE id_profil=? ', (str(vehicule_achetes), id_profil))
            conn.commit()
            slot.set_etat(1)
            slot.set_img(pygame.image.load("BslotBuy.png"))
        else :
            impossible()
    else :
        cursor.execute(f'SELECT {vehicule} FROM vehicule_actu WHERE id_profil = ?', (id_profil,))
        id_vehicule_actu = cursor.fetchone()[0]
        for ligne in liste_slots:
            for slots in ligne :
                if id_vehicule_actu == slots.get_cible() :
                    slots.set_img(pygame.image.load("BslotBuy.png"))
        cursor.execute(f'UPDATE vehicule_actu SET {vehicule} = ? WHERE id_profil = ?', (slot.get_cible(), id_profil))
        slot.set_img(pygame.image.load("BslotEquipe.png"))
        conn.commit()


def impossible():
    impossible = pygame.font.Font("Wonderly.otf", hauteur//8).render('impossible', 0, (255,100,100))
    plateau.blit(impossible, (largeur*0.4, hauteur*0.85))
    pygame.display.flip()
    pygame.time.wait(1000)
        