from app.player import Joueur


class Jeu:
    # CREATION DU CONSTRUCTEUR DU JEU
    def __init__(self):
        # INSTANCE JOUEUR
        self.joueur = Joueur()
        self.deplacement = {}
