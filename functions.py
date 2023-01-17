import pygame
import sys
import os
from pygame import mixer

''' Функции для загрузки картинки(load image) и для получения кадров анимации(cut_sheet) '''

size = width, height = 1600, 900

mixer.init()
fail_sound = mixer.Sound("sounds/fail_snd.wav")  # Звук проигрыша
screen = pygame.display.set_mode((width, height)) # Основной экран


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
            # if type == 'run':
            #     frames.append(sheet.subsurface(pygame.Rect(frame_location, (obj.rect.w - 80, obj.rect.h))))
            # else:
            frames.append(sheet.subsurface(pygame.Rect(frame_location, (obj.rect.w, obj.rect.h))))
    return frames

def draw_text(text, btn_pos, btn_size):
    font = pygame.font.Font('data/retro-land-mayhem.ttf', 50)
    text2 = font.render(text, True, 'white')
    bx, by = btn_pos
    bw, bh = btn_size
    fw, fh = font.size(text)
    screen.blit(text2, (bx + ((bw - fw) // 2), by + ((bh - fh) // 2)))
