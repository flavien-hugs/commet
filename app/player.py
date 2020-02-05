import pygame

from app.arme import Arme

# PARAMETRES DU PERSONNAGE PRINCIPAL
IMG_JOUEUR = "src/player.png"
POS_IMG_X, POS_IMG_Y = 450, 500  # COORDONNEE DE L'IMAGE SUR L'ECRAN PRINCIPAL
NOMBRE_DE_VIE = NOMBRE_DE_VIE_MAXIMALE = 100
POINT_ATTAQUE_JOUEUR = 10
RESTART_BY_SCD = 60  # NOMBRE DE FOIS OÙ LE JEU REDESSINE LES IMAGES
VITESSE_DEPLACEMENT_JOUEUR = int(round(POS_IMG_X/(3*RESTART_BY_SCD)))


class Joueur(pygame.sprite.Sprite):

    # CONSTRUCTEUR DE LA CLASS JOUEUR
    def __init__(self):
        super(Joueur, self).__init__()
        self.nombre_de_vie = NOMBRE_DE_VIE
        self.nombre_de_vie_maximale = NOMBRE_DE_VIE_MAXIMALE
        self.point_attaque_du_joueur = POINT_ATTAQUE_JOUEUR
        self.armes = pygame.sprite.Group()
        self.vitesse_deplacement_jouer = VITESSE_DEPLACEMENT_JOUEUR
        self.image = pygame.image.load(IMG_JOUEUR).convert_alpha()
        # L'INSTRUCTION convert_alpha() PERMET DE TRAITER LA
        # TRANSPARENCE DE L'IMAGE

        # POSITIONNEMENT DE L'IMAGE DANS UN RECTANGLE AUX
        # DIMENSIONS DE L'IMAGE
        self.rect = self.image.get_rect()
        # SUR L'AXE X
        self.rect.x = POS_IMG_X
        # SUR L'AXE Y
        self.rect.y = POS_IMG_Y

    # METHODE POUR ACTIONNER L'ARME
    def launch_arme(self):
        self.armes.add(Arme(self))

    # METHODE DE DEPLACEMENT DU JOUEUR
    def allerAdroite(self):
        self.rect.x += self.vitesse_deplacement_jouer

    def allerAgauche(self):
        self.rect.x -= self.vitesse_deplacement_jouer
