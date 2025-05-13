import pygame
from settings import *
from player import Player
from level import Level

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

pygame.display.set_caption("Metroidvania")
clock = pygame.time.Clock()

player = Player()
current_level_number = 1
level = Level(current_level_number)

running = True
while running:
    screen.fill((0, 0, 0))

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    player.update(level.platforms)

    # Cambiar nivel si toca la puerta
    if player.rect.colliderect(level.exit_door):
        current_level_number += 1
        if current_level_number > 10:
            current_level_number = 1
        level = Level(current_level_number)
        player.reset_position()

    level.draw(screen)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()