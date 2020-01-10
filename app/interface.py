import pygame
import math
import random
from pygame.locals import *

# IMPORTATION DES CLASS JEU ET JOUEUR
from app.jeu import Jeu
from app.player import Joueur

# PARAMETRES DE L'INTERFACE
LARGEUR, HAUTEUR = 1080, 700  # LARGEUR = 1080 ET HAUTEUR = 700
TITRE = "DESTROY COMMET"  # TITRE DU JEU
BG_POS_X, BG_POS_Y = 0, -200  # COORDONNEE X, Y
RESTART_BY_SCD = 100  # NOMBRE DE FOIS OÙ LE JEU REDESSINE LES IMAGES
BG_IMAGE = "src/bg.jpg"  # IMAGE ARRIERE PLAN

FONT = "src/fonts/PositiveSystem.otf"  # POLICE DE TEXTE
TEXTE = "start"
COLOR_TEXTE = "#FFFF00"


def interface():
    # INITIALISATION DU JEU
    pygame.init()
    screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption(TITRE.upper())

    # REMPLISSAGE DE L'ARRIERE PLAN
    background = pygame.image.load(BG_IMAGE).convert()
    background_pos = background.get_rect()
    background_pos.x = BG_POS_X
    background_pos.y = BG_POS_Y

    # TEXTE START
    police = pygame.font.Font(FONT, 50)
    texte = police.render(TEXTE.upper(), True, pygame.Color(COLOR_TEXTE))
    rectTexte = texte.get_rect()
    rectTexte.topleft = (0, 0)

    # INSTANCE DE LA CLASS JEU
    jeu = Jeu()

    # BOUCLE DU JEU
    temps = pygame.time.Clock()
    run = True
    while run:
        _temps = temps.tick(RESTART_BY_SCD)

        # GESTION DES EVENEMENTS
        for event in pygame.event.get():
            # CONDITION SI LE JEU EST FERMEÉ
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                print("Fermeture du jeu")
                run = False
                break
            # CLICK SUR LES TOUCHES DIRECTIONNELLES DOWN & UP
            elif event.type == KEYDOWN:
                jeu.deplacement[event.key] = True
            elif event.type == KEYUP:
                jeu.deplacement[event.key] = False

        # ECRAN PRINCIPALE DU JEU
        screen.blit(background, background_pos)

        # AJOUT TEXTE START
        screen.blit(texte, rectTexte)

        # AJOUT IMAGE DU JOUEUR
        screen.blit(jeu.joueur.image, jeu.joueur.imgDimensionRect)

        # DEPLACEMENT DU JOUEUR
        if jeu.deplacement.get(K_RIGHT) and jeu.joueur.imgDimensionRect.x < 910:
            jeu.joueur.allerAdroite()
        elif jeu.deplacement.get(K_LEFT) and jeu.joueur.imgDimensionRect.x > -35:
            jeu.joueur.allerAgauche()

        # MISE A JOUR DE L'AFFICHAGE - ECRAN
        pygame.display.update()
