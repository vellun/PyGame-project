import pygame
from functions import *

pygame.init()


class Button():
    def __init__(self, screen, pos, size, text):
        self.x, self.y = pos
        self.width, self.height = size
        self.text = text
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, border_color='black'):
        pygame.draw.rect(self.screen, border_color,
                         (self.x - 5, self.y - 5, self.width + 10, self.height + 10))  # Обводка кнопки
        pygame.draw.rect(self.screen, '#808080', (self.x, self.y, self.width, self.height))  # Кнопка
        draw_text(self.text, (self.x, self.y), (self.width, self.height))


def create_menu():
    btn_start = Button(screen, (width // 2 - 200, height // 2 - 70), (400, 100), 'Start')
    btn_exit = Button(screen, (width // 2 - 200, height // 2 + 60), (400, 100), 'Exit')
    btn_levels = Button(screen, (width // 2 - 200, height // 2 - 200), (400, 100), 'Levels')
    return [btn_start, btn_exit, btn_levels]
