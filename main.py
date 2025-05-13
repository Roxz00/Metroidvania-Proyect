import pygame
from settings import *
from player import Player
from level import Level

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Metroidvania")
clock = pygame.time.Clock()

current_level = 1
player = Player()
level = Level(current_level)

running = True
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(level.platforms)

    # Revisar si el jugador toca la puerta
    if player.rect.colliderect(level.exit_door):
        current_level += 1
        if current_level > 10:
            current_level = 1  # reiniciar si pasa el nivel 10
        level = Level(current_level)
        player.reset_position()

    screen.fill(BG_COLOR)
    level.draw(screen)
    player.draw(screen)
    pygame.display.flip()

pygame.quit()