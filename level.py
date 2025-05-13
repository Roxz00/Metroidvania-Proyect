import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Level:
    def __init__(self, number):
        self.number = number
        self.platforms, self.exit_door = self.load_level(number)

    def load_level(self, number):
        levels = {
            1: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),
                 pygame.Rect(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.7, 200, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 150, 50, 50)
            ),
            2: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),
                 pygame.Rect(SCREEN_WIDTH * 0.3, SCREEN_HEIGHT * 0.6, 200, 20),
                 pygame.Rect(SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.4, 200, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT * 0.35, 50, 50)
            ),
            3: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),
                 pygame.Rect(SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.5, 200, 20),
                 pygame.Rect(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.3, 200, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT * 0.25, 50, 50)
            ),
            4: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),
                 pygame.Rect(SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.75, 200, 20),
                 pygame.Rect(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, 200, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT * 0.45, 50, 50)
            ),
            5: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),
                 pygame.Rect(SCREEN_WIDTH * 0.3, SCREEN_HEIGHT * 0.6, 150, 20),
                 pygame.Rect(SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.4, 150, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT * 0.35, 50, 50)
            ),
            6: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),
                 pygame.Rect(SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.7, 150, 20),
                 pygame.Rect(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, 150, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT * 0.45, 50, 50)
            ),
            7: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),
                 pygame.Rect(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.4, 150, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT * 0.35, 50, 50)
            ),
            8: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),
                 pygame.Rect(SCREEN_WIDTH * 0.3, SCREEN_HEIGHT * 0.6, 200, 20),
                 pygame.Rect(SCREEN_WIDTH * 0.6, SCREEN_HEIGHT * 0.4, 200, 20),
                 pygame.Rect(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.2, 200, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT * 0.15, 50, 50)
            ),
            9: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),
                 pygame.Rect(SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.7, 150, 20),
                 pygame.Rect(SCREEN_WIDTH * 0.4, SCREEN_HEIGHT * 0.5, 150, 20),
                 pygame.Rect(SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.3, 150, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT * 0.25, 50, 50)
            ),
            10: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),
                 pygame.Rect(SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.7, 150, 20),
                 pygame.Rect(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5, 150, 20),
                 pygame.Rect(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.3, 150, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT * 0.25, 50, 50)
            ),
        }

        return levels.get(number, ([pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50)], pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 150, 50, 50)))

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (100, 100, 100), platform)
        pygame.draw.rect(screen, (0, 255, 0), self.exit_door)