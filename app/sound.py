# app/sound.py

import pygame


class SoundManager:
    def __init__(self):
        super(SoundManager, self).__init__()
        self.sounds = {
            'tir': pygame.mixer.Sound("src/sounds/tir.ogg"),
            'click': pygame.mixer.Sound("src/sounds/click.ogg"),
            'game_over': pygame.mixer.Sound("src/sounds/game_over.ogg"),
            'meteorite': pygame.mixer.Sound("src/sounds/meteorite.ogg")
        }

    def play(self, sound_name):
        self.sounds[sound_name].play()
