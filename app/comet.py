# app/comet.py

import random

import pygame


class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super(Comet, self).__init__()
        self.image = pygame.image.load("src/comet.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.velocity = random.randint(1, 3)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.comets.remove(self)
        self.comet_event.game.sound_manager.play('meteorite')
        if len(self.comet_event.comets) == 0:
            self.comet_event.reset_percent()
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 550:
            self.remove()
            if len(self.comet_event.comets) == 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(self, self.comet_event.game.players):
            self.remove()
            self.comet_event.game.player.player_dommage_attack(20)
