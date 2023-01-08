import pygame
from functions import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)

        self.frames = cut_sheet(self, load_image("Flight.png"), 8, 1, x, y)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.speed = 5

    def update(self, shift):
        self.image = self.frames[self.cur_frame]
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)

