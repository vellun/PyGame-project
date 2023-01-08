import sys

from hero import Hero
from level import Level
import pygame
from load_image import load_image

pygame.init()

width, height = 1600, 900
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
    anim_sprites = pygame.sprite.Group()
    hero = Hero(screen, anim_sprites)
    level = Level(screen, hero)
    running = True
    event = False
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        level.update()
        anim_sprites.update(event)
        anim_sprites.draw(screen)

        clock.tick(FPS)
        pygame.display.flip()
game()
