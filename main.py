import sys

from hero import Hero
from level import Level
import pygame
from functions import *
from game_interface import *
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
        st = settings_btn()['settings']  # Кнопка настроек
        pygame.mixer.music.set_volume(int(get_volume()['cur_volume']) / 100)  # Изменение громкости музыки
        btns = create_menu()
        for btn in btns:  # Подсветка кнопки синим цветом при наведении курсора
            if btn.rect.collidepoint(pygame.mouse.get_pos()):
                btn.draw('#1E90FF')
            else:
                btn.draw()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and st.collidepoint(
                    pygame.mouse.get_pos()):  # Если нажали на настройки
                settings()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btns[0].rect.collidepoint(event.pos):  # Если нажата кнопка start
                    game()
                elif btns[1].rect.collidepoint(event.pos):  # Если нажата кнопка exit
                    pygame.quit()
                    sys.exit()

        clock.tick(FPS)
        pygame.display.flip()


def game():
    pygame.mixer.music.load("sounds/soundtrack.mp3")  # Фоновая музыка
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(int(get_volume()['cur_volume']) / 100)  # Изменение громкости музыки

    anim_sprites = pygame.sprite.GroupSingle()
    hero = Hero(0, screen, anim_sprites)
    level = Level(screen, hero)
    running = True
    event = False
    while running:
        screen.blit(background, (0, 0))
        game_intrf(screen)

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

        clock.tick(FPS)
        pygame.display.flip()


def settings():
    running = True
    while running:
        screen.blit(background2, (0, 0))
        btns = create_settings()
        pygame.mixer.music.set_volume(int(get_volume()['cur_volume']) / 100)  # Изменение громкости музыки

        for btn in btns:  # Подсветка кнопки синим цветом при наведении курсора
            if btn.rect.collidepoint(pygame.mouse.get_pos()):
                btn.draw('#1E90FF')
            else:
                btn.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cur_volume = int(get_volume()['cur_volume'])
                if btns[0].rect.collidepoint(event.pos):  # Если нажата кнопка +
                    if cur_volume < 100:
                        change_volume(1)
                elif btns[1].rect.collidepoint(event.pos):  # Если нажата кнопка -
                    if cur_volume > 0:
                        change_volume(-1)

        clock.tick(FPS)
        pygame.display.flip()


main_menu()
