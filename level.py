import pygame
from pytmx.util_pygame import load_pygame
from tile import Tile

size = width, height = 1600, 900


class Level:
    def __init__(self, screen, hero=None):
        self.map = load_pygame('data\map.tmx')
        self.screen = screen
        self.hero = hero
        self.level_shift = 0
        self.render()

    def render(self):  # Рисование уровня
        self.tiles = pygame.sprite.Group()
        for y in range(self.map.height):
            for x in range(self.map.width):
                image = self.map.get_tile_image(x, y, 0)
                if image:
                    Tile(self.map, x, y, self.level_shift, self.tiles)

    def camera(self):  # Камера
        playerx = self.hero.rect.centerx
        if playerx < width // 2 and self.hero.direction.x < 0:
            self.hero.speed = 0
            self.level_shift = 8
        elif playerx > width // 2 and self.hero.direction.x > 0:
            self.hero.speed = 0
            self.level_shift = -8
        else:
            self.level_shift = 0
            self.hero.speed = 8

    def update(self):
        if self.hero:
            self.camera()
        self.tiles.draw(self.screen)
        self.tiles.update(self.level_shift)
