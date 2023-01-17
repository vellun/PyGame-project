import sys

from hero import Hero
from level import Level
import pygame
from functions import *
from game_interface import game_intrf
from main_menu import *

pygame.init()

clock = pygame.time.Clock()
FPS = 30
background = pygame.transform.scale(load_image('Back.jpg'), (width, height))
background2 = pygame.transform.scale(load_image('blur_background.jpg'), (width, height))


def main_menu():
    pygame.mixer.music.load("sounds/menu_snt.mp3")  # Фоновая музыка
    pygame.mixer.music.play(-1)
    while True:
        screen.blit(background2, (0, 0))
        btns = create_menu()
        for btn in btns:
            if btn.rect.collidepoint(pygame.mouse.get_pos()):
                btn.draw('#1E90FF')
            else:
                btn.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btns[0].rect.collidepoint(event.pos):
                    game()
                elif btns[1].rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        clock.tick(FPS)
        pygame.display.flip()


def game():
    pygame.mixer.music.load("sounds/soundtrack.mp3")  # Фоновая музыка
    pygame.mixer.music.play(-1)

    anim_sprites = pygame.sprite.GroupSingle()
    hero = Hero(0, screen, anim_sprites)
    level = Level(screen, hero)
    running = True
    event = False
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level.coins_kolvo(None, True)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        level.update()
        anim_sprites.update(event)
        anim_sprites.draw(screen)
        game_intrf(screen)

        clock.tick(FPS)
        pygame.display.flip()


main_menu()
