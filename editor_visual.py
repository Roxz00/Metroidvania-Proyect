import pygame
import json
import os

class LevelEditor:
    def __init__(self, screen):
        self.screen = screen
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = screen.get_size()
        self.GRID_SIZE = 50
        self.platforms = []
        self.exit_door = None
        self.font = pygame.font.Font(None, 36)
        self.level_name = ""
        self.naming_level = False
        self.clock = pygame.time.Clock()  # Añadimos esta línea

    def draw_grid(self):
        for x in range(0, self.SCREEN_WIDTH, self.GRID_SIZE):
            pygame.draw.line(self.screen, (50, 50, 50), (x, 0), (x, self.SCREEN_HEIGHT))
        for y in range(0, self.SCREEN_HEIGHT, self.GRID_SIZE):
            pygame.draw.line(self.screen, (50, 50, 50), (0, y), (self.SCREEN_WIDTH, y))

    def draw_platforms(self):
        for rect in self.platforms:
            pygame.draw.rect(self.screen, (100, 100, 100), rect)
        if self.exit_door:
            pygame.draw.rect(self.screen, (0, 255, 0), self.exit_door)

    def get_grid_position(self, pos):
        x = (pos[0] // self.GRID_SIZE) * self.GRID_SIZE
        y = (pos[1] // self.GRID_SIZE) * self.GRID_SIZE
        return x, y

    def save_level(self):
        if not os.path.exists('custom_levels'):
            os.makedirs('custom_levels')
        
        level_data = {
            'platforms': [(p.x, p.y, p.width, p.height) for p in self.platforms],
            'exit_door': (self.exit_door.x, self.exit_door.y, self.exit_door.width, self.exit_door.height) if self.exit_door else None
        }
        
        with open(f'custom_levels/{self.level_name}.json', 'w') as f:
            json.dump(level_data, f)

    def run(self):
        running = True
        while running:
            self.screen.fill((30, 30, 30))
            self.draw_grid()
            self.draw_platforms()

            if self.naming_level:
                text = self.font.render(f"Nombre del nivel: {self.level_name}", True, (255, 255, 255))
                self.screen.blit(text, (10, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"

                elif event.type == pygame.KEYDOWN:
                    if self.naming_level:
                        if event.key == pygame.K_RETURN and self.level_name:
                            self.save_level()
                            return "exit"
                        elif event.key == pygame.K_ESCAPE:
                            self.naming_level = False
                        elif event.key == pygame.K_BACKSPACE:
                            self.level_name = self.level_name[:-1]
                        elif event.unicode.isalnum() or event.unicode == '_':
                            self.level_name += event.unicode
                    else:
                        if event.key == pygame.K_ESCAPE:
                            return "exit"
                        elif event.key == pygame.K_s and self.platforms:
                            self.naming_level = True
                        elif event.key == pygame.K_e and not self.exit_door:
                            pos = pygame.mouse.get_pos()
                            grid_pos = self.get_grid_position(pos)
                            self.exit_door = pygame.Rect(grid_pos[0], grid_pos[1], self.GRID_SIZE, self.GRID_SIZE)

                elif event.type == pygame.MOUSEBUTTONDOWN and not self.naming_level:
                    pos = self.get_grid_position(event.pos)
                    rect = pygame.Rect(pos[0], pos[1], self.GRID_SIZE, self.GRID_SIZE)

                    if event.button == 1:  # Click izquierdo
                        if not any(r.colliderect(rect) for r in self.platforms):
                            self.platforms.append(rect)

                    elif event.button == 3:  # Click derecho
                        for r in self.platforms:
                            if r.collidepoint(pos):
                                self.platforms.remove(r)
                                break

            pygame.display.flip()
            self.clock.tick(60)  # Cambiamos clock por self.clock

pygame.quit()
