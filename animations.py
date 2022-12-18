import pygame
from load_image import load_image

pygame.init()


heroStands = [load_image("adventurer-idle-00.png"), load_image("adventurer-idle-01.png"),
                  load_image("adventurer-idle-02.png")]

heroStands2 = [load_image("adventurer-idle-2-00.png"), load_image("adventurer-idle-2-01.png"),
               load_image("adventurer-idle-2-02.png"), load_image("adventurer-idle-2-03.png")]

heroStandProcess = [load_image("adventurer-stand-00.png"), load_image("adventurer-stand-01.png"),
                    load_image("adventurer-stand-02.png")]

heroSlide = [load_image("adventurer-slide-00.png"), load_image("adventurer-slide-01.png")]

heroRun = [load_image("adventurer-run-00.png"), load_image("adventurer-run-01.png"),
           load_image("adventurer-run-02.png"), load_image("adventurer-run-03.png"),
           load_image("adventurer-run-04.png"), load_image("adventurer-run-05.png")]

heroAttack = [[load_image("adventurer-attack1-00.png"), load_image("adventurer-attack1-01.png"),
               load_image("adventurer-attack1-02.png"), load_image("adventurer-attack1-03.png"),
               load_image("adventurer-attack2-00.png"), load_image("adventurer-attack2-01.png"),
               load_image("adventurer-attack2-02.png"), load_image("adventurer-attack2-03.png"),
               load_image("adventurer-attack2-04.png"), load_image("adventurer-attack2-05.png")],
              [load_image("adventurer-attack3-00.png"), load_image("adventurer-attack3-01.png"),
               load_image("adventurer-attack3-02.png"), load_image("adventurer-attack3-03.png"),
               load_image("adventurer-attack3-04.png"), load_image("adventurer-attack3-05.png")]]

for i in range(len(heroStands)):
    heroStands[i] = pygame.transform.scale(heroStands[i], (265, 220))
for i in range(len(heroStands2)):
    heroStands2[i] = pygame.transform.scale(heroStands2[i], (265, 220))
for i in range(len(heroRun)):
    heroRun[i] = pygame.transform.scale(heroRun[i], (265, 220))
for i in range(len(heroSlide)):
    heroSlide[i] = pygame.transform.scale(heroSlide[i], (265, 220))
for i in range(len(heroAttack)):
    for j in range(len(heroAttack[i])):
        heroAttack[i][j] = pygame.transform.scale(heroAttack[i][j], (265, 220))