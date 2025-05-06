import pygame
from settings import *
from player import Player
from level import Level

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Metroidvania")
clock = pygame.time.Clock()

player = Player()
level = Level()

running = True
while running:
    dt = clock.tick(60) / 1000  # segundos por frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update(level.platforms)
    screen.fill(BG_COLOR)
    level.draw(screen)
    player.draw(screen)

    pygame.display.flip()

pygame.quit()