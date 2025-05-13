import pygame

pygame.init()

# Pantalla completa
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
pygame.display.set_caption("Editor Visual de Niveles")

clock = pygame.time.Clock()

# Configuración de la cuadrícula
GRID_SIZE = 50
platforms = []

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (50, 50, 50), (0, y), (SCREEN_WIDTH, y))

def draw_platforms():
    for rect in platforms:
        pygame.draw.rect(screen, (100, 100, 100), rect)

def export_platforms():
    print("\n--- Código exportado ---\n")
    for rect in platforms:
        print(f"pygame.Rect({rect.x}, {rect.y}, {rect.width}, {rect.height}),")
    print("\n--- Fin código exportado ---\n")

def get_grid_position(pos):
    x = (pos[0] // GRID_SIZE) * GRID_SIZE
    y = (pos[1] // GRID_SIZE) * GRID_SIZE
    return x, y

running = True
while running:
    screen.fill((30, 30, 30))

    draw_grid()
    draw_platforms()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_e:
                export_platforms()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = get_grid_position(event.pos)
            rect = pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE)

            if event.button == 1:  # Click izquierdo
                # Agregar solo si no existe
                if not any(r.colliderect(rect) for r in platforms):
                    platforms.append(rect)

            elif event.button == 3:  # Click derecho
                # Borrar si existe
                for r in platforms:
                    if r.collidepoint(pos):
                        platforms.remove(r)
                        break

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
