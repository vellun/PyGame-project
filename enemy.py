import pygame
from functions import *


# Класс врагов
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)

        self.frames = cut_sheet(self, load_image("Flight.png"), 8, 1, x, y)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.speed = 5
        self.directionx = 1

    # def change_frames(self, pic, cols, rows):
    #     self.frames = cut_sheet(self, load_image("Flight.png"), 8, 1, x, y)

    def update(self, shift):
        self.image = self.frames[self.cur_frame]
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)

        self.rect.x += shift

        self.rect.x += self.speed * self.directionx

        self.image = pygame.transform.flip(self.image, True if self.directionx < 0 else False, False)


# Класс для создания прямогольников для проверки столкновений врагов с уровнем
class EnemiesRects(pygame.sprite.Sprite):
    def __init__(self, enemy, *group):
        super().__init__(*group)
        self.enemy = enemy
        self.image = pygame.Surface((enemy.rect.width - 240, enemy.rect.height))
        self.image.fill('green')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = enemy.rect.left + 120, enemy.rect.top

    def update(self, shift):  # Прямоугольник двигается вместе с врагом и уровнем
        self.rect.x += shift
        self.rect.x += self.enemy.speed * self.enemy.directionx
