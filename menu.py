import pygame


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.selected_option = 0
        
    def draw_menu(self, options, selected_color=(255, 255, 0), unselected_color=(255, 255, 255)):
        total_height = len(options) * 100  # Altura total del menú (100 píxeles por opción)
        start_y = (self.screen.get_height() - total_height) // 2  # Posición inicial para centrar verticalmente
        
        for i, option in enumerate(options):
            color = selected_color if i == self.selected_option else unselected_color
            text = self.font.render(option, True, color)
            rect = text.get_rect(center=(self.screen.get_width() // 2,
                                       start_y + i * 100))
            self.screen.blit(text, rect)
    
    def handle_input(self, event, num_options):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # Cambiado de K_UP a K_w
                self.selected_option = (self.selected_option - 1) % num_options
            elif event.key == pygame.K_s:  # Cambiado de K_DOWN a K_s
                self.selected_option = (self.selected_option + 1) % num_options
            elif event.key == pygame.K_RETURN:
                return self.selected_option
        return None

class MainMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.options = ["Jugar", "Ver Rankings", "Niveles Personalizados", "Editor de Niveles", "Salir"]
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_menu(self.options)
        pygame.display.flip()
    
    def update(self, event):
        return self.handle_input(event, len(self.options))

class PauseMenu(Menu):
    def __init__(self, screen):
        super().__init__(screen)
        self.options = ["Continuar", "Menú Principal"]
    
    def draw(self):
        s = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        s.set_alpha(128)
        s.fill((0, 0, 0))
        self.screen.blit(s, (0, 0))
        self.draw_menu(self.options)
        pygame.display.flip()
    
    def update(self, event):
        return self.handle_input(event, len(self.options))

class CustomLevelMenu(Menu):
    def __init__(self, screen, levels):
        super().__init__(screen)
        self.options = levels if levels else ["Parece que nadie ha creado niveles aún :)"]
    
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.draw_menu(self.options)
        pygame.display.flip()
    
    def update(self, event):
        if not self.options or self.options[0] == "Parece que nadie ha creado niveles aún :)":
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return -1
            return None
        return self.handle_input(event, len(self.options))