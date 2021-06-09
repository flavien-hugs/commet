# app/game.py

import pygame

from app.player import Player
from app.sound import SoundManager
from app.monster import Mummy, Alien
from app.comet_event import CometFallEvent


class Game:
    def __init__(self):
        self.is_playing = False

        self.players = pygame.sprite.Group()
        self.player = Player(self)
        self.players.add(self.player)

        self.sound_manager = SoundManager()

        self.comet_event = CometFallEvent(self)

        self.monsters = pygame.sprite.Group()
        self.score_font = pygame.font.Font("src/fonts/permanent_marker_regular.ttf", 30)
        self.score = 0

        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        self.monsters = pygame.sprite.Group()
        self.comet_event.comets = pygame.sprite.Group()
        self.player.player_health = self.player.player_max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')

    def start_game(self, screen):
        score_text = self.score_font.render(f"Score : {self.score}", 1, (225, 225, 225))
        screen.blit(score_text, (20, 20))

        screen.blit(self.player.image, self.player.rect)
        self.player.update_player_health_bar(screen)
        self.player.animate_player()

        self.comet_event.update_bar(screen)

        for weapon in self.player.weapon:
            weapon.move()
        self.player.weapon.draw(screen)

        for monster in self.monsters:
            monster.forward()
            monster.monster_update_health_bar(screen)
            monster.animate_monster()
        self.monsters.draw(screen)

        for comet in self.comet_event.comets:
            comet.fall()
        self.comet_event.comets.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 910:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -35:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.monsters.add(monster_class_name.__call__(self))
