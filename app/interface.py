import pygame
from pygame.locals import *

# importation des class Jeu et Joueur
from app.jeu import Jeu
from app.player import Joueur

# Declaration des variables

TAILLE_ECRAN = [1080, 700]  # largeur = 1080 et hauteur = 700
TITRE = "DESTROY COMMET"
BG_IMAGE = "src/bg.jpg"
BG_POS_X, BG_POS_Y = 0, -200


def main():
    # Initialisation de la fenêtre d'affichage
    pygame.init()
    screen = pygame.display.set_mode(TAILLE_ECRAN)
    pygame.display.set_caption(TITRE.upper())

    # Remplissage de l'arrière-plan
    background = pygame.image.load(BG_IMAGE).convert()
    background_pos = background.get_rect()
    background_pos.x = BG_POS_X
    background_pos.y = BG_POS_Y

    # initialisation du jeu
    jeu = Jeu()

    run = True
    while run:
        # creation de l'ecran principal du jeu
        screen.blit(background, background_pos)

        # Ajout de l'image du joueur
        screen.blit(jeu.joueur.image, jeu.joueur.positionnement_image)

        # deplacement du joueur
        if jeu.deplacement.get(K_RIGHT) and jeu.joueur.positionnement_image.x < 910:
            jeu.joueur.deplacementAdroite()
        elif jeu.deplacement.get(K_LEFT) and jeu.joueur.positionnement_image.x > -35:
            jeu.joueur.deplacementAgauche()

        # mise à jour de l'ecran
        pygame.display.flip()

        # Boucle d'évènements
        for event in pygame.event.get():
            # condition de fermeture de la fenetre du jeu
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                print("Fermeture du jeu")
                run = False
                break
            # si click sur une touche du clavier
            elif event.type == KEYDOWN:
                jeu.deplacement[event.key] = True
            elif event.type == KEYUP:
                jeu.deplacement[event.key] = False
