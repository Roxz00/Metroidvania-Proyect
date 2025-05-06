import pygame
from settings import *

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 100, 32, 48)
        self.color = (255, 255, 255)
        self.vel_y = 0
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()
        dx = dy = 0

        if keys[pygame.K_LEFT]:
            dx = -PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            dx = PLAYER_SPEED

        self.vel_y += GRAVITY
        dy += self.vel_y

        self.rect.x += dx
        self.check_collisions(dx, 0, platforms)
        self.rect.y += dy
        self.check_collisions(0, dy, platforms)

        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -JUMP_FORCE
            self.on_ground = False

    def check_collisions(self, dx, dy, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform):
                if dy > 0:
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True
                elif dy < 0:
                    self.rect.top = platform.bottom
                    self.vel_y = 0
                elif dx > 0:
                    self.rect.right = platform.left
                elif dx < 0:
                    self.rect.left = platform.right

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)