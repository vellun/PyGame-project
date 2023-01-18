import pygame
from functions import *

pygame.init()


#  Класс кнопки
class Button():
    def __init__(self, screen, pos, size, text, image=None):
        self.x, self.y = pos
        self.image = image
        self.width, self.height = size
        self.text = text
        self.screen = screen
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, border_color='black'):
        pygame.draw.rect(self.screen, border_color,
                         (self.x - 5, self.y - 5, self.width + 10, self.height + 10))  # Обводка кнопки
        if self.image:  # Кнопка c картинкой на ней
            screen.blit(self.image, (self.x, self.y, self.width, self.height))
        else:
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

    draw_text("Volume settings", None, None, (width // 2 - 260, 150), 'black')  # Печатаем текст

    draw_text(f"Current volume: {get_volume()['cur_volume']}%", None, None, (width // 2 - 400, 300),
              'black')  # Печатаем текст

    minus_btn = Button(screen, (width // 2 - 400, 500), (200, 100), '-')
    plus_btn = Button(screen, (width // 2 + 90, 500), (200, 100), '+')
    back_btn = Button(screen, (50, 30), (200, 70), 'Back')
    return [plus_btn, minus_btn, back_btn]


def settings_btn():
    #  Отображение кнопки настроек в главном меню
    settings = pygame.image.load("sprites/interface_pictures/settings.png")
    settings_rect = settings.get_rect()
    settings_rect.x, settings_rect.y = 70, 60
    screen.blit(settings, (settings_rect.x, settings_rect.y))
    return {'settings': settings_rect}


#  Создание кнопок в уровнях
def change_lvl():
    lvl1 = pygame.image.load("sprites/interface_pictures/level1.jpg")
    lvl2 = pygame.image.load("sprites/interface_pictures/level2.jpg")
    lvl3 = pygame.image.load("sprites/interface_pictures/level3.jpg")

    s = [((100, 120), lvl1), ((850, 120), lvl2), ((480, 520), lvl3)]
    btns = []
    for i in range(len(s)):
        btns.append(Button(screen, s[i][0], (600, 350), f'Level {i + 1}', s[i][1]))
    back_btn = Button(screen, (50, height - 120), (200, 70), 'Back')  # Кнопка выхода в меню
    btns.append(back_btn)
    for i in btns:
        i.draw()
    return btns


#  Создание кнопок на экране проигрыша
def game_over_btns():
    grave = pygame.image.load("sprites/interface_pictures/grave.png")
    screen.blit(grave, (width - width // 2 - 130, 100))

    exit_btn = Button(screen, (width - width // 2 - 450, 600), (300, 100), "Exit")
    restart_btn = Button(screen, (width - width // 2 + 180, 600), (300, 100), "Restart")
    return [exit_btn, restart_btn]
