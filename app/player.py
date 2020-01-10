# Classe de representation des joueurs
import pygame

# Declarations de variables
IMG_JOUEUR = "src/player.png"
NOMBRE_DE_VIE = NOMBRE_DE_VIE_MAXIMALE = 100
POINT_ATTAQUE_JOUEUR = 10
VITESSE_DEPLACEMENT_JOUEUR = 5
# coordonnee x et y de positionnement img player
POS_IMG_X, POS_IMG_Y = 450, 500

class Joueur(pygame.sprite.Sprite):
    # constructeur de la class Joueur
    def __init__(self):
        super(Joueur, self).__init__()
        self.nombre_de_vie = NOMBRE_DE_VIE
        self.nombre_de_vie_maximale = NOMBRE_DE_VIE_MAXIMALE
        self.point_attaque_du_joueur = POINT_ATTAQUE_JOUEUR
        self.vitesse_deplacement_jouer = VITESSE_DEPLACEMENT_JOUEUR
        self.image = pygame.image.load(IMG_JOUEUR)

        # positionnement de l'image
        self.positionnement_image = self.image.get_rect()
        # sur l'axe X
        self.positionnement_image.x = POS_IMG_X
        # sur l'axe y
        self.positionnement_image.y = POS_IMG_Y

    # methode de deplacement du joueur
    def deplacementAdroite(self):
        self.positionnement_image.x += self.vitesse_deplacement_jouer

    def deplacementAgauche(self):
        self.positionnement_image.x -= self.vitesse_deplacement_jouer
