import pygame
from functions import *


class Coins(pygame.sprite.Sprite):
    def __init__(self, x, y, coin, *group):
        super().__init__(*group)

        self.frames = cut_sheet(self, load_image(coin), 5, 1, x, y)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

    def update(self, shift):
        self.image = self.frames[self.cur_frame]
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)

        self.rect.x += shift  # Монеты двигаются вместе с уровнем


