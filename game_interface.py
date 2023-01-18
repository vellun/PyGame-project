from functions import *
import csv


#  Функция для отображения монет и жизней на экране
def game_intrf(screen):
    #  Отображение монет
    gold = pygame.image.load("sprites/interface_pictures/gold.png")
    silv = pygame.image.load("sprites/interface_pictures/silv.png")

    screen.blit(pygame.transform.scale(gold, (32, 32)), (width - 100, 60))
    screen.blit(pygame.transform.scale(silv, (32, 32)), (width - 200, 60))

    file_read = csv.DictReader(open('data/coins.csv'), delimiter=';')
    coins = list(file_read)
    draw_nums(str(coins[0]['cur_golden']), (width - 138, 55), screen)
    draw_nums(str(coins[0]['cur_silver']), (width - 238, 55), screen)

    #  Отображение жизней
    full_live = pygame.image.load("sprites/interface_pictures/full_heart.png")
    empty_live = pygame.image.load("sprites/interface_pictures/empty_heart.png")
    coords = ((80, 60), (120, 60), (160, 60))
    for i in range(len(coords)):
        if get_lives(coins)[i]:
            screen.blit(pygame.transform.scale(full_live, (32, 32)), coords[i])
        else:
            screen.blit(pygame.transform.scale(empty_live, (32, 32)), coords[i])


#  Функция для пересчета жизней
def get_lives(sp):
    lives = [False, False, False]
    if int(sp[0]['lives']) > 0:
        for i in range(int(sp[0]['lives'])):
            lives[i] = True
    return lives


def hero_died():  # Функция для проверки смерти персонажа
    file_read = csv.DictReader(open('data/coins.csv'), delimiter=';')
    lives = list(file_read)[0]['lives']
    if int(lives) <= 0:
        return True
    return False


def draw_nums(num, pos, screen):  # Отображение числа монет
    font = pygame.font.Font('data/retro-land-mayhem.ttf', 35)
    text = font.render(num, True, 'black')
    screen.blit(text, pos)
