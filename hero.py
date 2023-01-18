from animations import *
from functions import *

pygame.init()
FPS = 30


class Hero(pygame.sprite.Sprite):
    def __init__(self, hero_num, screen, *group):
        super().__init__(*group)
        sheet, colums, rows = heroesStands[hero_num][0], heroesStands[hero_num][1][0], heroesStands[hero_num][1][1]
        self.frames = cut_sheet(self, sheet, colums, rows, 250, 250)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.screen = screen
        self.screen_rect = (0, 0, width, height)

        self.speed = 8
        self.directionx, self.directiony = 0, 0
        self.acceleration = 0.6
        self.v = -16

        self.attack, self.flip = False, 1  # номер анимации атаки в списке и поворот персонажа
        self.press = False  # флаг чтобы определить зажата ли клавиша
        self.anim_num = 0
        self.hero_num = hero_num
        self.jump = False
        self.run = False
        self.stand = False
        self.status = 'idle'
        self.bah = pygame.mixer.Sound("sounds/bahbah.mp3")

    def get_input(self, evnt):
        keys = pygame.key.get_pressed()
        if evnt:
            if keys[pygame.K_DOWN] and self.hero_num != 1:
                self.directionx = 1 if self.flip == 1 else -1

            if evnt.type == pygame.KEYDOWN and keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
                self.flip = 1 if keys[pygame.K_RIGHT] else 0

                if self.run:
                    self.animation(heroesRun)
                    self.status = 'run'
                    self.rect.w -= 80
                    self.run = False
                self.directionx = 1 if keys[pygame.K_RIGHT] else -1

            if evnt.type == pygame.KEYUP and not self.run:
                self.animation(heroesStands)
                self.status = 'idle'
                self.directionx = 0
                self.run = True

            if keys[pygame.K_f]:  # атака
                self.animation(heroesAttack)
                self.bah.play()
                self.attack = True

            if evnt.type == pygame.KEYDOWN and evnt.key == pygame.K_UP:
                if not self.jump and self.directiony == 0:
                    self.directiony = self.v  # прыжок
                    self.jump = True
            else:
                self.jump = False

            if self.attack and self.cur_frame == len(self.frames) - 1:
                self.animation(heroesStands)
                self.status = 'idle'
                self.attack = False

        else:
            if not self.run:
                self.directionx = 0
                self.run = True

    def animation(self, animation_sp):
        # В зависимости от нужной анимации изменяется список frames
        sheet, colums, rows = animation_sp[self.hero_num][0], animation_sp[self.hero_num][1][0], \
                              animation_sp[self.hero_num][1][1]
        self.frames = cut_sheet(self, sheet, colums, rows, self.rect.x,
                                self.rect.y) if animation_sp != heroesRun else cut_sheet(self, sheet, colums, rows,
                                                                                         self.rect.x, self.rect.y,
                                                                                         'run')

    def fly(self):
        # Персонаж все время хочет упасть вниз, но блоки уровня ему мешают
        self.directiony += self.acceleration
        self.rect.y += self.directiony

    def update(self, *args):
        self.get_input(args[0])

        self.rect.x += self.directionx * self.speed  # Изменение положения персонажа

        self.image = self.frames[self.cur_frame]
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)

        # Разворот персонажа по горизонтали
        sides = [True, False]
        self.image = pygame.transform.flip(self.image, sides[self.flip], False)

        self.fly()

        if not self.rect.colliderect(self.screen_rect):
            fail_sound.play()
            self.kill()
