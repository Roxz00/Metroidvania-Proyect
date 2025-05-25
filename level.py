import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
import json
import os

class Level:
    def __init__(self, number, custom_level_name=None):
        self.number = number
        self.level_width = 3000  # Ancho máximo del nivel
        self.level_height = 2000  # Alto máximo del nivel
        self.platforms, self.exit_door = self.load_level(number, custom_level_name)
        self.font = pygame.font.Font(None, 36)  # Añadimos una fuente para el texto
        self.arrow_image = pygame.Surface((20, 20), pygame.SRCALPHA)  # Superficie más pequeña para la flecha
        # Dibujamos una flecha que apunta hacia arriba por defecto
        pygame.draw.polygon(self.arrow_image, (255, 255, 0), [(10, 20), (0, 5), (5, 5), (5, 0), (15, 0), (15, 5), (20, 5)])

    def load_level(self, number, custom_level_name=None):
        if custom_level_name:
            try:
                with open(f'custom_levels/{custom_level_name}.json', 'r') as f:
                    data = json.load(f)
                    platforms = [pygame.Rect(*p) for p in data['platforms']]
                    exit_door = pygame.Rect(*data['exit_door']) if data['exit_door'] else None
                    return platforms, exit_door
            except:
                return self.get_default_level()

        # Definimos el diccionario levels aquí dentro del método
        levels = {
            1: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),  # Plataforma inicial
                 pygame.Rect(400, SCREEN_HEIGHT - 100, 100, 20)],  # Una plataforma simple
                pygame.Rect(600, SCREEN_HEIGHT - 150, 50, 50)  # Puerta cerca
            ),
            2: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),  # Plataforma inicial
                 pygame.Rect(400, SCREEN_HEIGHT - 100, 100, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 150, 100, 20),
                 pygame.Rect(800, SCREEN_HEIGHT - 200, 100, 20)],
                pygame.Rect(1000, SCREEN_HEIGHT - 250, 50, 50)  # Puerta más lejos
            ),
            3: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(400, SCREEN_HEIGHT - 150, 80, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 200, 80, 20),
                 pygame.Rect(800, SCREEN_HEIGHT - 250, 80, 20),
                 pygame.Rect(1000, SCREEN_HEIGHT - 200, 80, 20)],
                pygame.Rect(1200, SCREEN_HEIGHT - 250, 50, 50)
            ),
            4: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),  # Suelo
                 pygame.Rect(200, SCREEN_HEIGHT - 200, 80, 20),
                 pygame.Rect(400, SCREEN_HEIGHT - 250, 80, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 300, 80, 20),
                 pygame.Rect(800, SCREEN_HEIGHT - 250, 80, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 300, 50, 50)
            ),
            5: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),  # Suelo
                 pygame.Rect(200, SCREEN_HEIGHT - 200, 70, 20),
                 pygame.Rect(400, SCREEN_HEIGHT - 250, 70, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 300, 70, 20),
                 pygame.Rect(800, SCREEN_HEIGHT - 350, 70, 20),
                 pygame.Rect(1000, SCREEN_HEIGHT - 300, 70, 20)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 350, 50, 50)
            ),
            6: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),  # Suelo
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 100, 20),  # Plataforma inicial
                 pygame.Rect(350, SCREEN_HEIGHT - 300, 100, 20),  # Segunda plataforma
                 pygame.Rect(550, SCREEN_HEIGHT - 400, 100, 20),  # Tercera plataforma
                 pygame.Rect(750, SCREEN_HEIGHT - 500, 100, 20),  # Cuarta plataforma
                 pygame.Rect(950, SCREEN_HEIGHT - 400, 100, 20),  # Plataforma de retorno
                 pygame.Rect(1150, SCREEN_HEIGHT - 300, 100, 20)],  # Plataforma final
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 350, 50, 50)  # Puerta
            ),
            7: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),  # Suelo
                 pygame.Rect(200, SCREEN_HEIGHT - 200, 80, 20),  # Plataforma 1
                 pygame.Rect(400, SCREEN_HEIGHT - 350, 80, 20),  # Plataforma 2
                 pygame.Rect(600, SCREEN_HEIGHT - 500, 80, 20),  # Plataforma 3
                 pygame.Rect(800, SCREEN_HEIGHT - 650, 80, 20),  # Plataforma alta
                 pygame.Rect(1000, SCREEN_HEIGHT - 500, 80, 20),  # Plataforma descenso
                 pygame.Rect(1200, SCREEN_HEIGHT - 350, 80, 20)],  # Plataforma final
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 400, 50, 50)  # Puerta
            ),
            8: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),  # Suelo
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 70, 20),  # Inicio
                 pygame.Rect(300, SCREEN_HEIGHT - 350, 70, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 500, 70, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 650, 70, 20),  # Punto más alto
                 pygame.Rect(750, SCREEN_HEIGHT - 500, 70, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 350, 70, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 500, 70, 20),  # Subida final
                 pygame.Rect(1200, SCREEN_HEIGHT - 650, 70, 20)],  # Plataforma meta
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 700, 50, 50)  # Puerta
            ),
            9: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),  # Suelo
                 pygame.Rect(200, SCREEN_HEIGHT - 250, 60, 20),
                 pygame.Rect(250, SCREEN_HEIGHT - 400, 60, 20),
                 pygame.Rect(400, SCREEN_HEIGHT - 550, 60, 20),
                 pygame.Rect(550, SCREEN_HEIGHT - 700, 60, 20),  # Máxima altura
                 pygame.Rect(700, SCREEN_HEIGHT - 550, 60, 20),
                 pygame.Rect(850, SCREEN_HEIGHT - 400, 60, 20),
                 pygame.Rect(1000, SCREEN_HEIGHT - 550, 60, 20),
                 pygame.Rect(1150, SCREEN_HEIGHT - 700, 60, 20)],  # Final
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 750, 50, 50)  # Puerta
            ),
            10: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),  # Suelo
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 50, 20),  # Inicio
                 pygame.Rect(300, SCREEN_HEIGHT - 350, 50, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 500, 50, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 650, 50, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 800, 50, 20),  # Punto más alto
                 pygame.Rect(900, SCREEN_HEIGHT - 650, 50, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 500, 50, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 650, 50, 20)],  # Final
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 700, 50, 50)  # Puerta
            ),
            11: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50),  # Suelo
                 pygame.Rect(100, SCREEN_HEIGHT - 250, 40, 20),  # Primera plataforma
                 pygame.Rect(300, SCREEN_HEIGHT - 350, 40, 20),  # Reducida la altura de 400 a 350
                 pygame.Rect(500, SCREEN_HEIGHT - 450, 40, 20),  # Reducida la altura de 550 a 450
                 pygame.Rect(700, SCREEN_HEIGHT - 550, 40, 20),  # Reducida la altura de 700 a 550
                 pygame.Rect(900, SCREEN_HEIGHT - 650, 40, 20),  # Reducida la altura de 850 a 650
                 pygame.Rect(1100, SCREEN_HEIGHT - 550, 40, 20)],  # Reducida la altura de 700 a 550
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 600, 50, 50)  # Ajustada la puerta a una altura alcanzable
            ),
            12: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),  # Plataforma inicial
                 pygame.Rect(200, SCREEN_HEIGHT - 200, 40, 20),  # Primera plataforma
                 pygame.Rect(400, SCREEN_HEIGHT - 300, 40, 20),  # Segunda plataforma
                 pygame.Rect(600, SCREEN_HEIGHT - 400, 40, 20),  # Tercera plataforma
                 pygame.Rect(800, SCREEN_HEIGHT - 500, 40, 20),  # Cuarta plataforma
                 pygame.Rect(1000, SCREEN_HEIGHT - 400, 40, 20),  # Plataforma de descenso
                 pygame.Rect(1200, SCREEN_HEIGHT - 300, 40, 20)],  # Plataforma final
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 350, 50, 50)  # Puerta
            ),
            13: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),  
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 35, 20),  # Primera plataforma
                 pygame.Rect(350, SCREEN_HEIGHT - 300, 35, 20),  # Segunda plataforma
                 pygame.Rect(550, SCREEN_HEIGHT - 400, 35, 20),  # Tercera plataforma
                 pygame.Rect(750, SCREEN_HEIGHT - 500, 35, 20),  # Cuarta plataforma
                 pygame.Rect(950, SCREEN_HEIGHT - 400, 35, 20),  # Plataforma de descenso
                 pygame.Rect(1150, SCREEN_HEIGHT - 300, 35, 20)],  # Plataforma final
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 350, 50, 50)  # Puerta
            ),
            14: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),  # Plataforma inicial
                 pygame.Rect(200, SCREEN_HEIGHT - 200, 35, 20),  # Primera plataforma
                 pygame.Rect(400, SCREEN_HEIGHT - 300, 35, 20),  # Segunda plataforma
                 pygame.Rect(600, SCREEN_HEIGHT - 400, 35, 20),  # Tercera plataforma
                 pygame.Rect(800, SCREEN_HEIGHT - 300, 35, 20),  # Plataforma de descenso
                 pygame.Rect(1000, SCREEN_HEIGHT - 400, 35, 20),  # Subida
                 pygame.Rect(1200, SCREEN_HEIGHT - 300, 35, 20)],  # Plataforma final
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 350, 50, 50)  # Puerta
            ),
            15: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),  # Plataforma inicial
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 100, 20),  # Primera plataforma
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 100, 20),  # Segunda plataforma más alta
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 100, 20),  # Tercera plataforma
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 100, 20),  # Cuarta plataforma más alta
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 100, 20),  # Quinta plataforma
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 100, 20)],  # Plataforma final más alta
                pygame.Rect(1050, SCREEN_HEIGHT - 450, 50, 50)  # Puerta
            ),
            # Niveles 16-20: Patrones zigzag y saltos precisos
            16: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),  # Plataforma inicial
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 100, 20),  # Primera plataforma
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 100, 20),  # Segunda plataforma
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 100, 20),  # Tercera plataforma
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 100, 20),  # Cuarta plataforma
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 100, 20),  # Quinta plataforma
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 100, 20),  # Sexta plataforma
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 100, 20)],  # Séptima plataforma
                pygame.Rect(1200, SCREEN_HEIGHT - 400, 50, 50)  # Puerta
            ),
            17: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 100, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 100, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 100, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 100, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 100, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 100, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 100, 20)],
                pygame.Rect(1200, SCREEN_HEIGHT - 400, 50, 50)
            ),
            18: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 100, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 100, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 100, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 100, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 100, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 100, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 100, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 100, 20)],
                pygame.Rect(1350, SCREEN_HEIGHT - 500, 50, 50)
            ),
            19: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 100, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 100, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 100, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 100, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 100, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 100, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 100, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 100, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 100, 20)],
                pygame.Rect(1500, SCREEN_HEIGHT - 450, 50, 50)
            ),
            20: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 100, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 100, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 100, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 100, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 100, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 100, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 100, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 100, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 100, 20),
                 pygame.Rect(1500, SCREEN_HEIGHT - 500, 100, 20)],
                pygame.Rect(1650, SCREEN_HEIGHT - 550, 50, 50)
            ),
            21: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 90, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 90, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 90, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 90, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 90, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 90, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 90, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 90, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 90, 20),
                 pygame.Rect(1500, SCREEN_HEIGHT - 500, 90, 20)],
                pygame.Rect(1650, SCREEN_HEIGHT - 550, 50, 50)
            ),
            22: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 90, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 90, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 90, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 90, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 90, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 90, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 90, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 90, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 90, 20),
                 pygame.Rect(1500, SCREEN_HEIGHT - 500, 90, 20),
                 pygame.Rect(1650, SCREEN_HEIGHT - 450, 90, 20)],
                pygame.Rect(1800, SCREEN_HEIGHT - 500, 50, 50)
            ),
            23: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 80, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 80, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 80, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 80, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 80, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 80, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 80, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 80, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 80, 20),
                 pygame.Rect(1500, SCREEN_HEIGHT - 500, 80, 20),
                 pygame.Rect(1650, SCREEN_HEIGHT - 450, 80, 20)],
                pygame.Rect(1800, SCREEN_HEIGHT - 500, 50, 50)
            ),
            24: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 80, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 80, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 80, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 80, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 80, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 80, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 80, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 80, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 80, 20),
                 pygame.Rect(1500, SCREEN_HEIGHT - 500, 80, 20),
                 pygame.Rect(1650, SCREEN_HEIGHT - 450, 80, 20),
                 pygame.Rect(1800, SCREEN_HEIGHT - 550, 80, 20)],
                pygame.Rect(1950, SCREEN_HEIGHT - 600, 50, 50)
            ),
            25: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 70, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 70, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 70, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 70, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 70, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 70, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 70, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 70, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 70, 20),
                 pygame.Rect(1500, SCREEN_HEIGHT - 500, 70, 20),
                 pygame.Rect(1650, SCREEN_HEIGHT - 450, 70, 20),
                 pygame.Rect(1800, SCREEN_HEIGHT - 550, 70, 20)],
                pygame.Rect(1950, SCREEN_HEIGHT - 600, 50, 50)
            ),
            26: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 70, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 70, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 70, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 70, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 70, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 70, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 70, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 70, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 70, 20),
                 pygame.Rect(1500, SCREEN_HEIGHT - 500, 70, 20),
                 pygame.Rect(1650, SCREEN_HEIGHT - 450, 70, 20),
                 pygame.Rect(1800, SCREEN_HEIGHT - 550, 70, 20),
                 pygame.Rect(1950, SCREEN_HEIGHT - 500, 70, 20)],
                pygame.Rect(2100, SCREEN_HEIGHT - 550, 50, 50)
            ),
            27: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 60, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 60, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 60, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 60, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 60, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 60, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 60, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 60, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 60, 20),
                 pygame.Rect(1500, SCREEN_HEIGHT - 500, 60, 20),
                 pygame.Rect(1650, SCREEN_HEIGHT - 450, 60, 20),
                 pygame.Rect(1800, SCREEN_HEIGHT - 550, 60, 20),
                 pygame.Rect(1950, SCREEN_HEIGHT - 500, 60, 20)],
                pygame.Rect(2100, SCREEN_HEIGHT - 550, 50, 50)
            ),
            28: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 60, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 60, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 60, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 60, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 60, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 60, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 60, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 60, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 60, 20),
                 pygame.Rect(1500, SCREEN_HEIGHT - 500, 60, 20),
                 pygame.Rect(1650, SCREEN_HEIGHT - 450, 60, 20),
                 pygame.Rect(1800, SCREEN_HEIGHT - 550, 60, 20),
                 pygame.Rect(1950, SCREEN_HEIGHT - 500, 60, 20),
                 pygame.Rect(2100, SCREEN_HEIGHT - 600, 60, 20)],
                pygame.Rect(2250, SCREEN_HEIGHT - 650, 50, 50)
            ),
            29: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 50, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 50, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 50, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 50, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 50, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 50, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 50, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 50, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 50, 20),
                 pygame.Rect(1500, SCREEN_HEIGHT - 500, 50, 20),
                 pygame.Rect(1650, SCREEN_HEIGHT - 450, 50, 20),
                 pygame.Rect(1800, SCREEN_HEIGHT - 550, 50, 20),
                 pygame.Rect(1950, SCREEN_HEIGHT - 500, 50, 20),
                 pygame.Rect(2100, SCREEN_HEIGHT - 600, 50, 20)],
                pygame.Rect(2250, SCREEN_HEIGHT - 650, 50, 50)
            ),
            30: (
                [pygame.Rect(0, SCREEN_HEIGHT - 100, 300, 50),
                 pygame.Rect(150, SCREEN_HEIGHT - 200, 50, 20),
                 pygame.Rect(300, SCREEN_HEIGHT - 300, 50, 20),
                 pygame.Rect(450, SCREEN_HEIGHT - 250, 50, 20),
                 pygame.Rect(600, SCREEN_HEIGHT - 350, 50, 20),
                 pygame.Rect(750, SCREEN_HEIGHT - 300, 50, 20),
                 pygame.Rect(900, SCREEN_HEIGHT - 400, 50, 20),
                 pygame.Rect(1050, SCREEN_HEIGHT - 350, 50, 20),
                 pygame.Rect(1200, SCREEN_HEIGHT - 450, 50, 20),
                 pygame.Rect(1350, SCREEN_HEIGHT - 400, 50, 20),
                 pygame.Rect(1500, SCREEN_HEIGHT - 500, 50, 20),
                 pygame.Rect(1650, SCREEN_HEIGHT - 450, 50, 20),
                 pygame.Rect(1800, SCREEN_HEIGHT - 550, 50, 20),
                 pygame.Rect(1950, SCREEN_HEIGHT - 500, 50, 20),
                 pygame.Rect(2100, SCREEN_HEIGHT - 600, 50, 20),
                 pygame.Rect(2250, SCREEN_HEIGHT - 550, 50, 20)],
                pygame.Rect(2400, SCREEN_HEIGHT - 600, 50, 50)
            )
        }

        # Asegurar que las plataformas y la puerta estén dentro de los límites del nivel
        level_data = levels.get(number, self.get_default_level())
        platforms, exit_door = level_data

        # Ajustar las coordenadas para que estén dentro del nivel visible
        for platform in platforms:
            if platform.x > self.level_width - platform.width:
                platform.x = self.level_width - platform.width
            if platform.y > self.level_height - platform.height:
                platform.y = self.level_height - platform.height
        
        if exit_door.x > self.level_width - exit_door.width:
            exit_door.x = self.level_width - exit_door.width
        if exit_door.y > self.level_height - exit_door.height:
            exit_door.y = self.level_height - exit_door.height

        return platforms, exit_door

    def get_default_level(self):
        return ([pygame.Rect(0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 50)],
                pygame.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 150, 50, 50))

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (100, 100, 100), platform)
        pygame.draw.rect(screen, (0, 255, 0), self.exit_door)
        
        # Dibujamos el número de nivel en una posición fija en la pantalla
        level_text = self.font.render(f"Nivel {self.number}", True, (255, 255, 255))
        screen.blit(level_text, (10, 10))  # Siempre en la esquina superior izquierda

    def get_visible_platforms(self, player_x):
        # Return all platforms since we removed the ground
        return self.platforms