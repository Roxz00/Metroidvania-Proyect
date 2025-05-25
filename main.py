import pygame
import math
from player import Player
from level import Level
from menu import MainMenu, PauseMenu, CustomLevelMenu  # Update import
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BASE_WIDTH, BASE_HEIGHT  # Agregamos BASE_WIDTH y BASE_HEIGHT
from editor_visual import LevelEditor
import os

class Game:
    def __init__(self):
        pygame.init()
        
        # Actualizar la resolución de la pantalla
        info = pygame.display.Info()
        global SCREEN_WIDTH, SCREEN_HEIGHT
        SCREEN_WIDTH = info.current_w
        SCREEN_HEIGHT = info.current_h
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
        self.game_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
        self.scale_factor_x = SCREEN_WIDTH / BASE_WIDTH
        self.scale_factor_y = SCREEN_HEIGHT / BASE_HEIGHT
        
        # Inicializar variables de la cámara
        self.camera_x = 0
        self.camera_y = 0
        self.level_width = 3000  # Ancho máximo del nivel
        self.level_height = 2000  # Alto máximo del nivel
        
        pygame.display.set_caption("Metroidvania")
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = "MENU"
        self.speedrun_time = 0
        self.speedrun_active = False
        self.font = pygame.font.Font(None, 36)
        self.rankings = self.load_rankings()
        self.player_name = ""  # Añadir esta línea
        
        # Inicializar menús
        self.main_menu = MainMenu(self.screen)
        self.pause_menu = PauseMenu(self.screen)
        
        # Inicializar juego
        self.current_level = 1
        self.level = Level(self.current_level)
        self.player = Player(100, BASE_HEIGHT - 150)
        self.custom_levels = []
        self.load_custom_levels()
        self.custom_level_menu = None
        self.editor = None

    def load_custom_levels(self):
        if os.path.exists('custom_levels'):
            self.custom_levels = [f[:-5] for f in os.listdir('custom_levels') if f.endswith('.json')]

    def load_rankings(self):
        try:
            with open('rankings.txt', 'r') as f:
                rankings = []
                for line in f:
                    name, time = line.strip().split(',')
                    rankings.append((name, float(time)))
                return sorted(rankings, key=lambda x: x[1])
        except:
            return []
    
    def save_rankings(self):
        with open('rankings.txt', 'w') as f:
            for name, time in self.rankings:
                f.write(f"{name},{time}\n")
    
    def update(self):
        if self.game_state == "PLAYING" and self.speedrun_active:
            self.speedrun_time += self.clock.get_time() / 1000.0
            
            if self.current_level > 30:
                self.game_state = "ENTER_NAME"
                return
                
        visible_platforms = self.level.get_visible_platforms(self.player.rect.centerx)
        self.player.update(visible_platforms)
        
        # Detectar si el jugador ha caído del mapa
        if self.player.rect.top > BASE_HEIGHT:
            if hasattr(self.level, 'custom_level_name') and self.level.custom_level_name:
                # Reiniciar el mismo nivel personalizado
                self.level = Level(number=None, custom_level_name=self.level.custom_level_name)
            else:
                # Reiniciar el nivel principal actual
                self.level = Level(self.current_level)
            self.player = Player(100, BASE_HEIGHT - 150)
            self.camera_x = 0
            self.camera_y = 0
            return
        
        # Cámara dinámica que muestra más del nivel
        target_x = self.player.rect.centerx - BASE_WIDTH // 3  # Muestra más espacio por delante del jugador
        target_y = self.player.rect.centery - BASE_HEIGHT // 2
        
        # Suavizado de la cámara
        self.camera_x += (target_x - self.camera_x) * 0.1
        self.camera_y += (target_y - self.camera_y) * 0.1
        
        if self.player.rect.colliderect(self.level.exit_door):
            self.current_level += 1
            self.level = Level(self.current_level)
            self.player = Player(100, BASE_HEIGHT - 150)
            self.camera_x = 0
            self.camera_y = 0
        self.level_width = 3000  # Ancho máximo del nivel
        self.level_height = 2000  # Alto máximo del nivel
    
    def format_time(self, seconds):
        minutes = int(seconds // 60)
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:05.2f}"
    
    def draw(self):
        self.screen.fill((0, 0, 0))  # Limpiar la pantalla al inicio de cada frame
        
        if self.game_state == "PLAYING":
            # Dibujamos primero en la superficie del juego
            self.game_surface.fill((0, 0, 0))
            
            # Obtener las plataformas visibles basadas en la posición del jugador
            visible_platforms = self.level.get_visible_platforms(self.player.rect.centerx)
            
            # Aplicar el offset de la cámara al dibujar
            for platform in visible_platforms:
                pygame.draw.rect(self.game_surface, (100, 100, 100),
                               pygame.Rect(platform.x - self.camera_x,
                                          platform.y - self.camera_y,
                                          platform.width, platform.height))
            
            # Dibujar la puerta de salida con offset de cámara
            exit_rect = pygame.Rect(self.level.exit_door.x - self.camera_x,
                                   self.level.exit_door.y - self.camera_y,
                                   self.level.exit_door.width,
                                   self.level.exit_door.height)
            pygame.draw.rect(self.game_surface, (0, 255, 0), exit_rect)
            
            # Dibujar el jugador con offset de cámara
            player_rect = pygame.Rect(self.player.rect.x - self.camera_x,
                                     self.player.rect.y - self.camera_y,
                                     self.player.rect.width,
                                     self.player.rect.height)
            pygame.draw.rect(self.game_surface, (255, 0, 0), player_rect)
            
            # Dibujar la flecha y el número de nivel
            dx = self.level.exit_door.centerx - self.player.rect.centerx
            dy = self.level.exit_door.centery - self.player.rect.centery
            angle = math.degrees(math.atan2(dy, dx)) - 90
            
            rotated_arrow = pygame.transform.rotate(self.level.arrow_image, -angle)
            arrow_rect = rotated_arrow.get_rect()
            arrow_rect.centerx = player_rect.centerx
            arrow_rect.bottom = player_rect.top - 5
            self.game_surface.blit(rotated_arrow, arrow_rect)
            
            level_text = self.level.font.render(f"Nivel {self.level.number}", True, (255, 255, 255))
            self.game_surface.blit(level_text, (10, 10))
            
            if self.speedrun_active:
                time_text = self.font.render(self.format_time(self.speedrun_time), True, (255, 255, 255))
                time_rect = time_text.get_rect(center=(BASE_WIDTH // 2, 30))
                self.game_surface.blit(time_text, time_rect)
            
            # Escalamos y dibujamos en la pantalla completa
            scaled_surface = pygame.transform.scale(self.game_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.screen.blit(scaled_surface, (0, 0))
            
        elif self.game_state == "MENU":
            self.main_menu.draw()
        elif self.game_state == "PAUSED":
            self.pause_menu.draw()
        elif self.game_state == "CUSTOM_LEVELS":
            if self.custom_level_menu:
                self.custom_level_menu.draw()
        elif self.game_state == "RANKINGS":
            if not self.rankings:
                no_times_text = self.font.render("Parece que nadie ha completado el juego aún :)", True, (255, 255, 255))
                text_rect = no_times_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                self.screen.blit(no_times_text, text_rect)
            else:
                for i, (name, time) in enumerate(self.rankings[:10]):
                    ranking_text = self.font.render(f"{i+1}. {name}: {self.format_time(time)}", True, (255, 255, 255))
                    text_rect = ranking_text.get_rect(center=(SCREEN_WIDTH // 2, 100 + i * 50))
                    self.screen.blit(ranking_text, text_rect)
        elif self.game_state == "ENTER_NAME":
            self.screen.fill((0, 0, 0))
            time_text = self.font.render(f"¡Completado! Tiempo: {self.format_time(self.speedrun_time)}", True, (255, 255, 255))
            options_text = self.font.render("Presiona ENTER para guardar, R para reintentar, o ESC para salir", True, (255, 255, 255))
            name_text = self.font.render("Ingresa tu nombre:", True, (255, 255, 255))
            input_text = self.font.render(self.player_name + "_", True, (255, 255, 0))
            
            self.screen.blit(time_text, time_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)))
            self.screen.blit(options_text, options_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
            self.screen.blit(name_text, name_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)))
            self.screen.blit(input_text, input_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)))
        
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.game_state == "MENU":
                option = self.main_menu.update(event)
                if option is not None:
                    if option == 0:  # Jugar
                        self.game_state = "PLAYING"
                        self.current_level = 1
                        self.level = Level(self.current_level)
                        self.player = Player(100, BASE_HEIGHT - 150)
                        self.speedrun_active = True
                        self.speedrun_time = 0
                    elif option == 1:  # Ver Rankings
                        self.game_state = "RANKINGS"
                    elif option == 2:  # Niveles Personalizados
                        self.load_custom_levels()
                        self.custom_level_menu = CustomLevelMenu(self.screen, self.custom_levels)
                        self.game_state = "CUSTOM_LEVELS"
                    elif option == 3:  # Editor de Niveles
                        self.editor = LevelEditor(self.screen)
                        self.game_state = "EDITOR"
                    elif option == 4:  # Salir
                        self.running = False

            elif self.game_state == "CUSTOM_LEVELS":
                if not hasattr(self, 'custom_level_menu') or self.custom_level_menu is None:
                    self.load_custom_levels()  # Aseguramos que los niveles estén cargados
                    self.custom_level_menu = CustomLevelMenu(self.screen, self.custom_levels)
                
                self.custom_level_menu.draw()  # Añadir esta línea para dibujar el menú
                
                option = self.custom_level_menu.update(event)
                if option == -1 or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.game_state = "MENU"
                elif option is not None and self.custom_levels:
                    # Cargar el nivel personalizado seleccionado
                    self.level = Level(number=0, custom_level_name=self.custom_levels[option])
                    self.player = Player(100, BASE_HEIGHT - 150)
                    self.game_state = "PLAYING"
                    self.speedrun_active = False  # Desactivar speedrun para niveles personalizados
            elif self.game_state == "RANKINGS":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.game_state = "MENU"

            elif self.game_state == "EDITOR":
                if self.editor:
                    result = self.editor.run()
                    if result == "exit":
                        self.game_state = "MENU"
                        self.editor = None
                    
            elif self.game_state == "PLAYING":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.game_state = "PAUSED"
                else:
                    self.player.handle_input(event)
                    
            elif self.game_state == "PAUSED":
                option = self.pause_menu.update(event)
                if option == 0:  # Continuar
                    self.game_state = "PLAYING"
                elif option == 1:  # Menú Principal
                    self.game_state = "MENU"
                    self.current_level = 1
                    self.level = Level(self.current_level)
                    self.player = Player(100, SCREEN_HEIGHT - 150)

            elif self.game_state == "ENTER_NAME":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(self.player_name) > 0:
                        self.rankings.append((self.player_name, self.speedrun_time))
                        self.rankings.sort(key=lambda x: x[1])
                        self.save_rankings()
                        self.game_state = "MENU"
                    elif event.key == pygame.K_ESCAPE:
                        self.game_state = "MENU"  # Salir sin guardar
                    elif event.key == pygame.K_r:
                        # Reiniciar el juego
                        self.current_level = 1
                        self.level = Level(self.current_level)
                        self.player = Player(100, BASE_HEIGHT - 150)
                        self.speedrun_time = 0
                        self.game_state = "PLAYING"
                        self.player_name = ""
                    elif event.key == pygame.K_BACKSPACE:
                        self.player_name = self.player_name[:-1]
                    elif event.unicode.isalnum() and len(self.player_name) < 15:
                        self.player_name += event.unicode
            
            elif self.game_state == "RANKINGS":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.game_state = "MENU"
                    self.screen.fill((0, 0, 0))
                    if not self.rankings:
                        no_times_text = self.font.render("Parece que nadie ha completado el juego aún :)", True, (255, 255, 255))
                        text_rect = no_times_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                        self.screen.blit(no_times_text, text_rect)
                    else:
                        for i, (name, time) in enumerate(self.rankings[:10]):
                            ranking_text = self.font.render(f"{i+1}. {name}: {self.format_time(time)}", True, (255, 255, 255))
                            text_rect = ranking_text.get_rect(center=(SCREEN_WIDTH // 2, 100 + i * 50))
                            self.screen.blit(ranking_text, text_rect)
                    pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()