# app/interface.py

import math, sys, pygame

from app.game import Game


def main():
    FPSCLOCK = 60
    pygame.init()
    fps_clock = pygame.time.Clock()

    screen = pygame.display.set_mode((1080, 700))
    pygame.display.set_caption("COMMET FALL GAME".upper())

    background = pygame.image.load("src/bg.jpg").convert()
    background_position = background.get_rect()
    background_position.x = 0
    background_position.y = -200

    banner = pygame.image.load("src/banner.png")
    banner = pygame.transform.scale(banner, (500, 500))
    banner_rect = banner.get_rect()
    banner_rect.x = math.ceil(screen.get_width() / 4)

    play_button = pygame.image.load("src/button.png")
    play_button = pygame.transform.scale(play_button, (400, 150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width() / 3.33)
    play_button_rect.y = math.ceil(screen.get_height() / 2)

    game = Game()

    while True:
        screen.blit(background, background_position)

        if game.is_playing:
            game.start_game(screen)
        else:
            screen.blit(play_button, play_button_rect)
            screen.blit(banner, banner_rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    if game.is_playing:
                        game.player.launch_weapon()
                    else:
                        game.start()
                        game.sound_manager.play('click')
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    game.start()
                    game.sound_manager.play('click')

        fps_clock.tick(FPSCLOCK)
        pygame.display.update()
