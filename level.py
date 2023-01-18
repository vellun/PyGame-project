import pygame
from pytmx.util_pygame import load_pygame
from tile import Tile
from functions import *
from coins import Coins
from enemy import *
from objects_coords import *
from animations import *
import csv

maps = ['map.tmx', 'map2.tmx', 'map3.tmx']


class Level:
    def __init__(self, screen, hero=None):
        self.map = load_pygame(f'data\{maps[cur_level]}')
        self.screen = screen
        self.hero = hero
        self.level_shift = 0
        self.render()
        self.f = True
        self.coin_sound = pygame.mixer.Sound("sounds/coin.wav")  # Звук монеты
        self.coin_sound2 = pygame.mixer.Sound("sounds/vipali_coins.mp3")  # Звук выпадения монет из монстра
        self.voice = pygame.mixer.Sound("sounds/voice.mp3")
        self.bah = pygame.mixer.Sound("sounds/bah.mp3")
        self.enem = None

    def render(self):  # Рисование уровня
        self.tiles = pygame.sprite.Group()
        self.golden_coins = pygame.sprite.Group()
        self.silver_coins = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemies_rects = pygame.sprite.Group()
        self.flag = pygame.sprite.Group()
        for y in range(self.map.height):
            for x in range(self.map.width):
                image = self.map.get_tile_image(x, y, layer=0)
                if image:
                    Tile(self.map, x, y, self.level_shift, self.tiles)
        for i in golden_coins[cur_level]:  # Создание золотых монет
            Coins(i[0] * self.map.tilewidth, i[1] * self.map.tilewidth, "MonedaD.png", self.golden_coins)
        for i in silver_coins[cur_level]:  # Создание серебряных монет
            Coins(i[0] * self.map.tilewidth, i[1] * self.map.tilewidth, "MonedaP.png", self.silver_coins)
        for i in enemies_eyes[cur_level]:  # Создание врагов-летающих глаз
            Enemy(i[0] * self.map.tilewidth, i[1] * self.map.tilewidth, 'Flight.png', 'eye', self.enemies)
        for i in enemies_mishrooms[cur_level]:  # Создание врагов-грибов
            Enemy(i[0] * self.map.tilewidth, i[1] * self.map.tilewidth, 'mishroom_run.png', 'mishroom', self.enemies)
        for i in enemies_goblins[cur_level]:  # Создание врагов-гоблинов
            Enemy(i[0] * self.map.tilewidth, i[1] * self.map.tilewidth, 'goblin_run.png', 'goblin', self.enemies)
        for i in flags[cur_level]:  # Создание флага
            Coins(i[0] * self.map.tilewidth, i[1] * self.map.tilewidth, "flag animation.png", self.flag)

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
        if playerx - width // 2 >= self.map.width * self.map.tilewidth - width:
            self.level_shift = 0

    def collision(self):
        right_left_rect = pygame.Rect(self.hero.rect.left - 5, self.hero.rect.top + 15, self.hero.rect.width,
                                      self.hero.rect.height - 30)
        top_bottom_rect = pygame.Rect(self.hero.rect.left + 18, self.hero.rect.top, self.hero.rect.width - 36,
                                      self.hero.rect.height)

        for sprite in self.tiles.sprites():
            #  Проверка столкновений справа и слева от персонажа
            if sprite.rect.colliderect(right_left_rect):
                if self.hero.directionx < 0:
                    self.hero.rect.left = sprite.rect.right
                    self.hero.directionx = 0
                elif self.hero.directionx > 0:
                    self.hero.rect.right = sprite.rect.left
                    self.hero.directionx = 0
                self.level_shift = 0
            #  Проверка столкновений сверху и снизу персонажа
            elif sprite.rect.colliderect(top_bottom_rect):
                if self.hero.directiony < 0:
                    self.hero.rect.top = sprite.rect.bottom
                    self.hero.directiony = 0
                elif self.hero.directiony > 0:
                    self.hero.rect.bottom = sprite.rect.top + 10
                    self.hero.directiony = 0

        #  Проверка столкновений персонажа с золотыми монетами
        for coin in self.golden_coins.sprites():
            if coin.rect.colliderect(right_left_rect):
                self.coins_kolvo('golden')
                coin.kill()
                self.coin_sound.play()

        #  Проверка столкновений персонажа с серебряными монетами
        for coin in self.silver_coins.sprites():
            if coin.rect.colliderect(right_left_rect):
                self.coins_kolvo('silver')
                coin.kill()
                self.coin_sound.play()

        if pygame.sprite.spritecollideany(self.hero, self.flag):
            pygame.quit()
            sys.exit()

        #  Проверка столкновений врагов с уровнем
        for enemy in self.enemies.sprites():
            rect_sprite = EnemiesRects(enemy, self.enemies_rects)
            if not pygame.sprite.spritecollideany(rect_sprite, self.tiles):
                enemy.directionx *= -1

            if enemy.rect.colliderect(right_left_rect):
                enemy.frames = cut_sheet(self, enemy.attack_pic, 8, 1, enemy.rect.x, enemy.rect.y)
                if self.hero.attack:
                    self.bah.play()
                    for i in (100, -120, -150):
                        golden_coins.append((self.hero.rect.centerx + i, self.hero.rect.centery))
                    for i in golden_coins[-3:]:
                        Coins(i[0], i[1], "MonedaD.png", self.golden_coins)
                    enemy.kill()
                    pygame.time.delay(200)
                    self.coin_sound2.play()

            else:
                enemy.frames = cut_sheet(self, enemy.pic, 8, 1, enemy.rect.x, enemy.rect.y)

        #  Проверка столкновений героя с врагами
        if pygame.sprite.spritecollideany(self.hero, self.enemies_rects):
            if self.hero.cur_frame == 0 and self.f:
                self.hero.animation(heroesHurt)
                self.voice.play()
                if not self.coins_kolvo('lives'):
                    self.f = False
        else:
            self.f = True
            if self.hero.cur_frame == 0:
                if self.hero.directionx == 0:
                    self.hero.animation(heroesStands)
                else:
                    self.hero.animation(heroesRun)
        # pygame.draw.rect(self.screen, 'red',
        #                  (self.hero.rect.x, self.hero.rect.y, self.hero.rect.width, self.hero.rect.height))

    def coins_kolvo(self, coin, zeroing=False):  # Изменение общего количества монет в файле
        file_read = csv.DictReader(open('data/coins.csv'), delimiter=';')
        coins = list(file_read)
        if coin == 'lives':
            coins[0][coin] = int(coins[0][coin]) - 1
        else:
            if not zeroing:
                coins[0][coin] = int(coins[0][coin]) + 1
                coins[0][f"cur_{coin}"] = int(coins[0][f"cur_{coin}"]) + 1
            else:
                coins[0]["cur_golden"], coins[0][
                    "cur_silver"] = 0, 0  # Вначале игры монеты обнуляются, а жизни восстанавливаются
                coins[0]["lives"] = 3

        file_write = csv.DictWriter(open('data/coins.csv', 'w', newline=''), fieldnames=list(coins[0].keys()),
                                    delimiter=';')
        file_write.writeheader()
        file_write.writerow(coins[0])

        if coin and coins[0][coin] <= 0:
            return False
        return True

    def update(self):
        if self.hero:
            self.camera()
            self.collision()
        self.tiles.draw(self.screen)
        self.tiles.update(self.level_shift)

        self.golden_coins.draw(self.screen)
        self.golden_coins.update(self.level_shift)

        self.silver_coins.draw(self.screen)
        self.silver_coins.update(self.level_shift)

        self.flag.update(self.level_shift)
        self.flag.draw(self.screen)

        self.enemies.draw(self.screen)
        self.enemies.update(self.level_shift)

        self.enemies_rects.update(self.level_shift)
