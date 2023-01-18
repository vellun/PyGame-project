import sys

from hero import Hero
from level import Level
import pygame
from functions import *
from game_interface import *
from main_menu import *
from screensavers import *

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
                    screensaver(screen, f'Level {int(get_cur_level()["cur_level"]) + 1}')
                    game()
                elif btns[1].rect.collidepoint(event.pos):  # Если нажата кнопка exit
                    pygame.quit()
                    sys.exit()
                elif btns[2].rect.collidepoint(event.pos):  # Если нажата кнопка levels
                    levels()

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
    cur_level = int(get_cur_level()['cur_level'])
    backg = pygame.transform.scale(load_image(backgrounds[cur_level]), (width, height))
    while running:
        if level.level_end == 'end':  # Если пройдены все уровни
            main_menu()
        if level.level_end:  # Если уровень пройден
            game()
            level.level_end = False

        screen.blit(backg, (0, 0))
        game_intrf(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                level.coins_kolvo(None, True)
                pygame.quit()
                sys.exit()
        level.update()
        anim_sprites.update(event)
        anim_sprites.draw(screen)

        clock.tick(FPS)
        pygame.display.flip()


def levels():
    running = True
    while running:
        screen.fill('black')
        btns = change_lvl()

        for btn in btns:  # Подсветка кнопки синим цветом при наведении курсора
            if btn.rect.collidepoint(pygame.mouse.get_pos()):
                btn.draw('#1E90FF')
            else:
                btn.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btns[-1].rect.collidepoint(event.pos):
                    main_menu()

                elif btns[0].rect.collidepoint(event.pos):
                    change_level(False, 0)
                    print(get_cur_level())
                    game()
                elif btns[1].rect.collidepoint(event.pos):
                    change_level(False, 1)
                    game()
                elif btns[2].rect.collidepoint(event.pos):
                    change_level(False, 2)
                    game()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cur_volume = int(get_volume()['cur_volume'])
                if btns[0].rect.collidepoint(event.pos):  # Если нажата кнопка +
                    if cur_volume < 100:
                        change_volume(1)
                elif btns[1].rect.collidepoint(event.pos):  # Если нажата кнопка -
                    if cur_volume > 0:
                        change_volume(-1)
                elif btns[2].rect.collidepoint(event.pos):  # Если нажата кнопка Back
                    main_menu()

        clock.tick(FPS)
        pygame.display.flip()


main_menu()
