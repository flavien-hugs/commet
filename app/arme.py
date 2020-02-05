import pygame


# GESTION DE L'ARME
class Arme(pygame.sprite.Sprite):

    # CONSTRUCTEUR DE LA CLASSE ARME
    def __init__(self, player):
        super(Arme, self).__init__()

        self.velocity = 5  # VITESSE DE DEPLACEMENT DE L'ARME
        self.player = player
        self.image = pygame.image.load('src/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80

        self.origin_image = self.image
        self.angle = 0

    # ANIMATION DE L'ARME
    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        print("Animation activée !")

    def remove(self):
        self.player.armes.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
                                      
        # SI ARME HORS CADRE
        if self.rect.x > 1080:
            print("arme detruite !")
            self.remove()
