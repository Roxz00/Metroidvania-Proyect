import pygame

class Level:
    def __init__(self):
        self.platforms = [
            pygame.Rect(0, 400, 800, 50),
            pygame.Rect(200, 300, 100, 20),
            pygame.Rect(400, 250, 150, 20)
        ]

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (100, 100, 100), platform)