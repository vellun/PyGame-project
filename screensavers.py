from functions import *
import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 30


def screensaver(screen, text, size=130):  # Функция для отображения заставок между уровнями
        screen.fill('black')
        font = pygame.font.Font('data/retro-land-mayhem.ttf', size)
        text2 = font.render(text, True, 'white')
        fw, fh = font.size(text)
        screen.blit(text2, (500, 500))

        clock.tick(FPS)
        pygame.display.flip()
        pygame.time.delay(2500)


