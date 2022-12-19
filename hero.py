import pygame.math
import random

from animations import *

pygame.init()
size = width, height = 700, 500


class Hero(pygame.sprite.Sprite):
    def __init__(self, hero_num, *group):
        super().__init__(*group)
        self.image = heroesStands[hero_num][0 // (60 // len(heroesStands[hero_num]))]
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, height - self.rect.height - 40

        self.speed = 3
        self.direction = pygame.math.Vector2(0, 0)

        # event_type определяет какая клавиша была нажата
        self.event_type, self.stand = None, 0  # Переменная stand определяет одну из двух анимаций персонажа когда он стоит
        self.attack, self.flip = 0, 1  # номер анимации атаки в списке и поворот персонажа
        self.press = False  # флаг чтобы определить зажата ли клавиша
        self.anim_num = 0
        self.hero_num = hero_num

    def get_input(self, evnt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and self.hero_num != 1:
            self.event_type = pygame.K_DOWN
            self.press = True

        elif evnt.type == pygame.KEYDOWN and keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
            self.stand = 0
            self.event_type = pygame.K_RIGHT if keys[pygame.K_RIGHT] else pygame.K_LEFT
            self.flip = 1 if keys[pygame.K_RIGHT] else 0
            self.press = True

        elif keys[pygame.K_f]:  # атака
            self.press = False
            self.event_type, self.anim_num, self.attack = pygame.K_f, 0, random.randrange(2)
            if self.hero_num == 0:
                self.stand = 1

        if evnt.type == pygame.KEYUP and self.press:
            self.event_type = None
            self.press = False

        self.anim_num += 1
        if self.anim_num >= 60:
            self.anim_num = 0
            if self.event_type and self.event_type == pygame.K_f:
                if self.hero_num == 0:
                    self.stand = 1
                self.event_type, run = None, False

    def update(self, *args):
        # В зависимости от нажатой клавиши показываются кадры анимации из списка
        self.get_input(args[0])
        if not self.event_type:
            self.image = heroesStands[self.hero_num][
                self.anim_num // (60 // (len(heroesStands[self.hero_num])))] if not self.stand else hero1Stands2[
                self.anim_num // 15]
            self.direction.x = 0

        elif self.event_type == pygame.K_DOWN:
            self.image = heroesSlide[self.hero_num][self.anim_num // (60 // len(heroesSlide[self.hero_num]))]
            self.direction.x = 1 if self.flip == 1 else -1

        elif self.event_type == pygame.K_RIGHT:
            self.image = heroesRun[self.hero_num][self.anim_num // (60 // len(heroesRun[self.hero_num])) - 1]
            self.direction.x = 1

        elif self.event_type == pygame.K_LEFT:
            self.image = heroesRun[self.hero_num][self.anim_num // (60 // len(heroesRun[self.hero_num])) - 1]
            self.direction.x = -1

        elif self.event_type == pygame.K_f:
            self.image = heroesAttack[self.hero_num][self.attack][
                self.anim_num // (60 // len(heroesAttack[self.hero_num][self.attack])) - 1]

        # Разворот персонажа по горизонтали
        sides = [True, False]
        self.image = pygame.transform.flip(self.image, sides[self.flip], False)

        self.rect.x += self.direction.x * self.speed
