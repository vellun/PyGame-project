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


#  Создание кнопок в главном меню
def create_menu():
    btn_start = Button(screen, (width // 2 - 200, height // 2 - 70), (400, 100), 'Start')
    btn_exit = Button(screen, (width // 2 - 200, height // 2 + 60), (400, 100), 'Exit')
    btn_levels = Button(screen, (width // 2 - 200, height // 2 - 200), (400, 100), 'Levels')
    return [btn_start, btn_exit, btn_levels]

#  Создание кнопок в настройках
def create_settings():
    global cur_volume

    draw_text("Volume settings", None, None, (width // 2 - 260, 150), 'black')  # Печатаем текст

    draw_text(f"Current volume: {cur_volume}%", None, None, (width // 2 - 400, 300), 'black')  # Печатаем текст
    print(cur_volume)

    minus_btn = Button(screen, (width // 2 - 400, 500), (200, 100), '-')
    plus_btn = Button(screen, (width // 2 + 90, 500), (200, 100), '+')
    return [plus_btn, minus_btn]

def settings_btn():
    #  Отображение кнопки настроек в главном меню
    settings = pygame.image.load("sprites/interface_pictures/settings.png")
    settings_rect = settings.get_rect()
    settings_rect.x, settings_rect.y = 70, 60
    screen.blit(settings, (settings_rect.x, settings_rect.y))
    return {'settings': settings_rect}

