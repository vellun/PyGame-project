import sys

from hero import Hero
from level import Level
import pygame
from functions import load_image, width, height
from game_interface import game_intrf

pygame.init()

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 30
background = pygame.transform.scale(load_image('Back.jpg'), (width, height))
background2 = pygame.transform.scale(load_image('Background3 (2).jpg'), (width, height))


def draw_text(text):
    font = pygame.font.Font(None, 60)
    text = font.render(text, True, 'blue')
    screen.blit(text, (300, 300))


def main_menu():
    while True:
        screen.blit(background2, (0, 0))
        draw_text('Run, hero, run!')
        menu_back = Level(screen)
        menu_back.level_shift = -3

        button1 = pygame.Rect(0, 0, 200, 50)
        button2 = pygame.Rect(50, 200, 200, 50)
        pygame.draw.rect(screen, 'pink', button1)
        pygame.draw.rect(screen, 'pink', button2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    game()

        clock.tick(FPS)
        pygame.display.flip()


def game():
    pygame.mixer.music.load("sounds/soundtrack.mp3")  # Фоновая музыка
    pygame.mixer.music.play(-1)

    anim_sprites = pygame.sprite.Group()
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
