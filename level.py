import pygame

class Level:
    def __init__(self, number):
        self.number = number
        self.platforms, self.exit_door = self.load_level(number)

    def load_level(self, number):
        levels = {
            1: ([pygame.Rect(0, 400, 800, 50), pygame.Rect(200, 300, 150, 20)], pygame.Rect(500, 350, 50, 50)),
            2: ([pygame.Rect(0, 450, 800, 50), pygame.Rect(300, 370, 100, 20), pygame.Rect(500, 290, 120, 20)], pygame.Rect(750, 400, 50, 50)),
            3: ([pygame.Rect(0, 500, 800, 50), pygame.Rect(200, 420, 100, 20), pygame.Rect(400, 360, 100, 20), pygame.Rect(600, 300, 100, 20)], pygame.Rect(750, 450, 50, 50)),
            
        }
        if number in levels:
            return levels[number]
        else:
            return ([pygame.Rect(0, 400, 800, 50)], pygame.Rect(750, 350, 50, 50))  # nivel por defecto

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (100, 100, 100), platform)
        pygame.draw.rect(screen, (0, 255, 0), self.exit_door)  # puerta en verde