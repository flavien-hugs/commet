# Class principale du Jeu
from app.player import Joueur


class Jeu:
    # Creation du constructeur de la class Jeu
    def __init__(self):
        # instance du joueur
        self.joueur = Joueur()
        self.deplacement = {}
