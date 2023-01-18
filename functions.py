import csv

import pygame
import sys
import os
from pygame import mixer

''' Функции для загрузки картинки(load image) и для получения кадров анимации(cut_sheet) '''

size = width, height = 1600, 900

mixer.init()
fail_sound = mixer.Sound("sounds/fail_snd.wav")  # Звук проигрыша
screen = pygame.display.set_mode((width, height))  # Основной экран


def get_cur_level():  # Функция для получения текущего уровня из файла
    level_file = list(csv.DictReader(open('data/current_level.csv'), delimiter=';'))
    return level_file[0]


# Функция для изменения текущего уровня
def change_level():
    l = get_cur_level()
    l['cur_level'] = int(l['cur_level']) + 1

    file_write = csv.DictWriter(open('data/current_level.csv', 'w', newline=''), fieldnames=['cur_level'],
                                delimiter=';')
    file_write.writeheader()
    file_write.writerow(l)


def get_volume():  # Функция для получения значения громкости из файла
    volume_file = list(csv.DictReader(open('data/volume.csv'), delimiter=';'))
    return volume_file[0]


# Функция для изменения громкости музыки в игре
def change_volume(volume=1):
    v = get_volume()
    v['cur_volume'] = int(v['cur_volume']) + 5 * volume  # volume показывает, нужно уменьшать громкость или увеличивать

    file_write = csv.DictWriter(open('data/volume.csv', 'w', newline=''), fieldnames=['cur_volume'], delimiter=';')
    file_write.writeheader()
    file_write.writerow(v)


def load_image(name, colorkey=None):
    fullname = os.path.join('sprites', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image
    return image


def cut_sheet(obj, sheet, columns, rows, x, y, type='idle'):
    sheet = pygame.transform.scale(sheet, (sheet.get_width() * 2, sheet.get_height() * 2))
    frames = []
    obj.cur_frame = 0
    obj.rect = pygame.Rect(x, y, sheet.get_width() // columns, sheet.get_height() // rows)
    for j in range(rows):
        for i in range(columns):
            frame_location = (obj.rect.w * i, obj.rect.h * j)
            frames.append(sheet.subsurface(pygame.Rect(frame_location, (obj.rect.w, obj.rect.h))))
    return frames


def draw_text(text, btn_pos=None, btn_size=None, pos=None, color='white'):
    font = pygame.font.Font('data/retro-land-mayhem.ttf', 50)
    text2 = font.render(text, True, color)
    if btn_pos and btn_size:  # Если параметры переданы, нужно напечатать текст на кнопке
        bx, by = btn_pos
        bw, bh = btn_size
        fw, fh = font.size(text)
        screen.blit(text2, (bx + ((bw - fw) // 2), by + ((bh - fh) // 2)))
    if pos:  # Если переданы только координаты, нужно напечатать просто текст
        screen.blit(text2, pos)
