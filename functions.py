import pygame
import sys
import os

''' Функции для загрузки картинки(load image) и для получения кадров анимации(cut_sheet) '''

size = width, height = 1600, 900


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
            if type == 'run':
                frames.append(sheet.subsurface(pygame.Rect(frame_location, (obj.rect.w - 80, obj.rect.h))))
            else:
                frames.append(sheet.subsurface(pygame.Rect(frame_location, (obj.rect.w, obj.rect.h))))
    return frames
