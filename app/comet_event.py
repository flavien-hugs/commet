# app/comet_event.py

import pygame

from app.comet import Comet

class CometFallEvent:
    def __init__(self, game):
        super(CometFallEvent, self).__init__()
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False
        self.comets = pygame.sprite.Group()
    
    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        for i in range(1, 10):
            self.comets.add(Comet(self))

    def attempt_fail(self):
        if self.is_full_loaded() and len(self.game.monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True

    def update_bar(self, surface):
        self.add_percent()
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])
        pygame.draw.rect(surface, (225, 225, 225), [0, surface.get_height() - 20, (surface.get_width() / 100) * self.percent, 10])
