import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.vel_y = 0  # Cambiado de velocity_y a vel_y para mantener consistencia
        self.jumping = False
        self.on_ground = True  # Añadido inicialización de on_ground

    def handle_input(self, event):
        # Manejo de eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and self.on_ground:
                self.vel_y = -15
                self.on_ground = False

    def update(self, platforms):
        # Gravedad
        self.vel_y += 1
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
        if keys[pygame.K_a]:  # Cambiado de K_LEFT a K_a
            self.rect.x -= 5
        if keys[pygame.K_d]:  # Cambiado de K_RIGHT a K_d
            self.rect.x += 5

    def reset_position(self):
        self.rect.topleft = (100, SCREEN_HEIGHT - 150)
        self.vel_y = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 255), self.rect)