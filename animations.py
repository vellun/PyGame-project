import pygame
from functions import load_image

pygame.init()

heroesStands = [[load_image("idle sheet-Sheet2.png"), (18, 1)]]

heroesJump = [[load_image("itch jump sheet-Sheet.png"), (1, 1)]]

heroesFall = [[load_image("itch fall sheet-Sheet.png"), (1, 1)]]

heroesAttack = [[load_image("itch light atk sheet-Sheet.png"), (26, 1)]]

heroesRun = [[load_image("itch run-Sheet sheet.png"), (24, 1)]]


