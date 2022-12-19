import pygame
from load_image import load_image

pygame.init()

#  Индексы персонажей в списках: 0 - путешественница, 1 - волшебник, 2 - воительница

heroesStands = [[load_image("adventurer-idle-00.png"), load_image("adventurer-idle-01.png"),
                 load_image("adventurer-idle-02.png")],
                [load_image("WizardStand1.png"), load_image("WizardStand2.png"), load_image("WizardStand3.png"),
                 load_image("WizardStand4.png"), load_image("WizardStand5.png"),
                 load_image("WizardStand6.png")],
                [load_image("Warrior_Idle_1.png"), load_image("Warrior_Idle_2.png"), load_image("Warrior_Idle_3.png"),
                 load_image("Warrior_Idle_4.png"), load_image("Warrior_Idle_5.png"), load_image("Warrior_Idle_6.png")]]

hero1Stands2 = [load_image("adventurer-idle-2-00.png"), load_image("adventurer-idle-2-01.png"),
                load_image("adventurer-idle-2-02.png"), load_image("adventurer-idle-2-03.png")]

heroesSlide = [[load_image("adventurer-slide-00.png"), load_image("adventurer-slide-01.png")], [],
               [load_image("Warrior-Slide_1.png"), load_image("Warrior-Slide_2.png"),
                load_image("Warrior-Slide_3.png")]]

heroesRun = [[load_image("adventurer-run-00.png"), load_image("adventurer-run-01.png"),
              load_image("adventurer-run-02.png"), load_image("adventurer-run-03.png"),
              load_image("adventurer-run-04.png"), load_image("adventurer-run-05.png")],
             [load_image("WizardRun1.png"), load_image("WizardRun2.png"), load_image("WizardRun3.png"),
              load_image("WizardRun4.png"), load_image("WizardRun5.png"), load_image("WizardRun6.png"),
              load_image("WizardRun7.png"), load_image("WizardRun8.png")],
             [load_image("Warrior_Run_1.png"), load_image("Warrior_Run_2.png"), load_image("Warrior_Run_3.png"),
              load_image("Warrior_Run_4.png"), load_image("Warrior_Run_5.png"), load_image("Warrior_Run_6.png"),
              load_image("Warrior_Run_7.png"), load_image("Warrior_Run_8.png")]]

heroesAttack = [[[load_image("adventurer-attack1-00.png"), load_image("adventurer-attack1-01.png"),
                  load_image("adventurer-attack1-02.png"), load_image("adventurer-attack1-03.png"),
                  load_image("adventurer-attack2-00.png"), load_image("adventurer-attack2-01.png"),
                  load_image("adventurer-attack2-02.png"), load_image("adventurer-attack2-03.png"),
                  load_image("adventurer-attack2-04.png"), load_image("adventurer-attack2-05.png")],
                 [load_image("adventurer-attack3-00.png"), load_image("adventurer-attack3-01.png"),
                  load_image("adventurer-attack3-02.png"), load_image("adventurer-attack3-03.png"),
                  load_image("adventurer-attack3-04.png"), load_image("adventurer-attack3-05.png")]],
                [[load_image("WizardAttack1.png"), load_image("WizardAttack2.png"), load_image("WizardAttack3.png"),
                  load_image("WizardAttack4.png"), load_image("WizardAttack5.png"), load_image("WizardAttack6.png"),
                  load_image("WizardAttack7.png"), load_image("WizardAttack8.png")],
                 [load_image("Wizard2Attack1.png"), load_image("Wizard2Attack2.png"), load_image("Wizard2Attack3.png"),
                  load_image("Wizard2Attack4.png"), load_image("Wizard2Attack5.png"), load_image("Wizard2Attack6.png"),
                  load_image("Wizard2Attack7.png"), load_image("Wizard2Attack8.png")]],
                [[load_image("Warrior_Attack_1.png"), load_image("Warrior_Attack_2.png"),
                  load_image("Warrior_Attack_3.png"), load_image("Warrior_Attack_4.png"),
                  load_image("Warrior_Attack_5.png"), load_image("Warrior_Attack_6.png"),
                  load_image("Warrior_Attack_7.png"), load_image("Warrior_Attack_8.png"),
                  load_image("Warrior_Attack_9.png"), load_image("Warrior_Attack_10.png"),
                  load_image("Warrior_Attack_11.png"), load_image("Warrior_Attack_12.png")],
                 [load_image("Warrior_Dash-Attack_1.png"), load_image("Warrior_Dash-Attack_2.png"),
                  load_image("Warrior_Dash-Attack_3.png"), load_image("Warrior_Dash-Attack_4.png"),
                  load_image("Warrior_Dash-Attack_5.png"), load_image("Warrior_Dash-Attack_6.png"),
                  load_image("Warrior_Dash-Attack_7.png"), load_image("Warrior_Dash-Attack_8.png"),
                  load_image("Warrior_Dash-Attack_9.png"), load_image("Warrior_Dash-Attack_10.png")]]]

for i in range(len(heroesStands)):
    for j in range(len(heroesStands[i])):
        if i == 1:
            heroesStands[i][j] = pygame.transform.scale(heroesStands[i][j], (455, 410))
        else:
            heroesStands[i][j] = pygame.transform.scale(heroesStands[i][j], (265, 220))
for i in range(len(heroesRun)):
    for j in range(len(heroesRun[i])):
        if i != 1:
            heroesRun[i][j] = pygame.transform.scale(heroesRun[i][j], (265, 220))
        else:
            heroesRun[i][j] = pygame.transform.scale(heroesRun[i][j], (455, 410))
for i in range(len(hero1Stands2)):
    hero1Stands2[i] = pygame.transform.scale(hero1Stands2[i], (265, 220))

for i in range(len(heroesSlide)):
    for j in range(len(heroesSlide[i])):
        heroesSlide[i][j] = pygame.transform.scale(heroesSlide[i][j], (265, 220))

for i in range(len(heroesAttack)):
    for j in range(len(heroesAttack[i])):
        for k in range(len(heroesAttack[i][j])):
            if i != 1:
                heroesAttack[i][j][k] = pygame.transform.scale(heroesAttack[i][j][k], (265, 220))
            else:
                heroesAttack[i][j][k] = pygame.transform.scale(heroesAttack[i][j][k], (455, 410))
