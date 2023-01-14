import pygame
from pytmx.util_pygame import load_pygame
from tile import Tile
from functions import *
from coins import Coins
from enemy import *
from objects_coords import *
from animations import *


class Level:
    def __init__(self, screen, hero=None):
        self.map = load_pygame('data\map.tmx')
        self.screen = screen
        self.hero = hero
        self.level_shift = 0
        self.render()
        self.f = False
        self.coin_sound = pygame.mixer.Sound("sounds/coin.wav")  # Звук монеты
        self.enem = None

    def render(self):  # Рисование уровня
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemies_rects = pygame.sprite.Group()
        for y in range(self.map.height):
            for x in range(self.map.width):
                image = self.map.get_tile_image(x, y, layer=0)
                if image:
                    Tile(self.map, x, y, self.level_shift, self.tiles)
        for i in golden_coins:  # Создание золотых монет
            Coins(i[0] * self.map.tilewidth, i[1] * self.map.tilewidth, "MonedaD.png", self.coins)
        for i in silver_coins:  # Создание серебряных монет
            Coins(i[0] * self.map.tilewidth, i[1] * self.map.tilewidth, "MonedaP.png", self.coins)
        for i in enemies:  # Создание врагов
            Enemy(i[0] * self.map.tilewidth, i[1] * self.map.tilewidth, self.enemies)

    def camera(self):  # Камера
        playerx = self.hero.rect.centerx
        if playerx < width // 2 and self.hero.directionx < 0:
            self.hero.speed = 0
            self.level_shift = 5
        elif playerx > width // 2 and self.hero.directionx > 0:
            self.hero.speed = 0
            self.level_shift = -5
        else:
            self.level_shift = 0
            self.hero.speed = 8

    def collision(self):
        right_left_rect = pygame.Rect(self.hero.rect.left - 5, self.hero.rect.top, self.hero.rect.width,
                                      self.hero.rect.height - 30)
        top_bottom_rect = pygame.Rect(self.hero.rect.left + 18, self.hero.rect.top, self.hero.rect.width - 36,
                                      self.hero.rect.height)
        for sprite in self.tiles.sprites():
            #  Проверка столкновений сверху и снизу персонажа
            if sprite.rect.colliderect(top_bottom_rect):
                if self.hero.directiony < 0:
                    self.hero.rect.top = sprite.rect.bottom
                    self.hero.directiony = 0
                elif self.hero.directiony > 0:
                    self.hero.rect.bottom = sprite.rect.top + 10
                    self.hero.directiony = 0

            #  Проверка столкновений справа и слева от персонажа
            elif sprite.rect.colliderect(right_left_rect):
                if self.hero.directionx < 0:
                    self.hero.rect.left = sprite.rect.right
                    self.hero.directionx = 0
                elif self.hero.directionx > 0:
                    self.hero.rect.right = sprite.rect.left
                    self.hero.directionx = 0
                self.level_shift = 0

        #  Проверка столкновений персонажа с монетами
        for coin in self.coins.sprites():
            if coin.rect.colliderect(right_left_rect):
                coin.kill()
                self.coin_sound.play()

        #  Проверка столкновений врагов с уровнем
        for enemy in self.enemies.sprites():
            rect_sprite = EnemiesRects(enemy, self.enemies_rects)
            if not pygame.sprite.spritecollideany(rect_sprite, self.tiles):
                enemy.directionx *= -1

            if enemy.rect.colliderect(right_left_rect):
                enemy.frames = cut_sheet(self, load_image("Attack.png"), 8, 1, enemy.rect.x, enemy.rect.y)
                if self.hero.attack:
                    enemy.kill()

            else:
                enemy.frames = cut_sheet(self, load_image("Flight.png"), 8, 1, enemy.rect.x, enemy.rect.y)

        if pygame.sprite.spritecollideany(self.hero, self.enemies_rects):
            if self.hero.cur_frame == 0:
                self.hero.animation(heroesHurt)
        else:
            if self.hero.cur_frame == 0:
                if self.hero.directionx == 0:
                    self.hero.animation(heroesStands)
                else:
                    self.hero.animation(heroesRun)

    def update(self):
        if self.hero:
            self.camera()
            self.collision()
        self.tiles.draw(self.screen)
        self.tiles.update(self.level_shift)

        self.coins.draw(self.screen)
        self.coins.update(self.level_shift)

        self.enemies.draw(self.screen)
        self.enemies.update(self.level_shift)

        self.enemies_rects.update(self.level_shift)
