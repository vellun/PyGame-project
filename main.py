from hero import Hero
import pygame

pygame.init()
size = width, height = 700, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

anim_sprites = pygame.sprite.Group()
hero = Hero(anim_sprites)

running = True

while running:
    screen.fill('white')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    anim_sprites.update(event)
    anim_sprites.draw(screen)

    clock.tick(60)
    pygame.display.flip()
pygame.quit()
