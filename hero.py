import pygame.math
import random

from animations import *

pygame.init()
size = width, height = 700, 500


class Hero(pygame.sprite.Sprite):
    def __init__(self, screen, *group):
        super().__init__(*group)
        self.image = heroStands[0 // 15]
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, height - self.rect.height - 40
        self.screen = screen

        self.speed = 8
        self.direction = pygame.math.Vector2(0, 0)

        # event_type определяет какая клавиша была нажата
        self.event_type, self.stand = None, 0  # Переменная stand определяет одну из двух анимаций персонажа когда он стоит
        self.attack, self.flip = 0, 1  # номер анимации атаки в списке и поворот персонажа
        self.press = False  # флаг чтобы определить зажата ли клавиша
        self.anim_num = 0

    def get_input(self, evnt):
        keys = pygame.key.get_pressed()
        if evnt:
            if keys[pygame.K_DOWN]:
                self.event_type = pygame.K_DOWN
                self.press = True
            elif evnt.type == pygame.KEYDOWN and keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                self.stand = 0
                self.event_type = pygame.K_RIGHT if keys[pygame.K_RIGHT] else pygame.K_LEFT
                self.flip = 1 if keys[pygame.K_RIGHT] else 0
                self.press = True

            elif keys[pygame.K_f]:  # атака
                self.press = False
                self.event_type, self.anim_num, self.stand, self.attack = pygame.K_f, 0, 1, random.randrange(2)

            if evnt.type == pygame.KEYUP and self.press:
                self.event_type = None
                self.press = False

            self.anim_num += 1
            if self.anim_num >= 60:
                self.anim_num = 0
                if self.event_type and self.event_type == pygame.K_f:
                    self.event_type, run, self.stand = None, False, 1

    def update(self, *args):
        # В зависимости от нажатой клавиши показываются кадры анимации из списка
        self.get_input(args[0])
        if not self.event_type:
            self.image = heroStands[self.anim_num // 20] if not self.stand else heroStands2[self.anim_num // 15]
            self.direction.x = 0

        elif self.event_type == pygame.K_DOWN:
            self.image = heroSlide[self.anim_num // (60 // len(heroSlide))]
            self.direction.x = 1 if self.flip == 1 else -1

        elif self.event_type == pygame.K_RIGHT:
            self.image = heroRun[self.anim_num // (60 // len(heroRun))]
            self.direction.x = 1

        elif self.event_type == pygame.K_LEFT:
            self.image = heroRun[self.anim_num // (60 // len(heroRun))]
            self.direction.x = -1

        elif self.event_type == pygame.K_f:
            self.image = heroAttack[self.attack][self.anim_num // (60 // len(heroAttack[self.attack]))]

        # Разворот персонажа по горизонтали
        sides = [True, False]
        self.image = pygame.transform.flip(self.image, sides[self.flip], False)

        self.rect.x += self.direction.x * self.speed
