import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, level_map, x, y, shift, *group):
        super().__init__(*group)
        self.tile_size = level_map.tilewidth
        self.image = level_map.get_tile_image(x, y, 0)
        self.shift = shift
        if self.image:
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = x * self.tile_size, y * self.tile_size

    def update(self, shift):
        self.rect.x += shift


