import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, SCREEN_HEIGHT - 150, 50, 50)
        self.vel_y = 0
        self.on_ground = False

    def update(self, platforms):
        self.vel_y += 1  # Gravedad
        self.rect.y += self.vel_y

        # Colisiones verticales
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_y > 0:
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True

        # Movimiento lateral básico
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Saltar solo si está en el suelo
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -15
            self.on_ground = False

    def reset_position(self):
        self.rect.topleft = (100, SCREEN_HEIGHT - 150)
        self.vel_y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)