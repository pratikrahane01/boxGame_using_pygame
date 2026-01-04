import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Dodge Game")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (50, 150, 255)
RED = (255, 80, 80)
BLACK = (0, 0, 0)

# Player settings
player_width = 50
player_height = 50
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 7

# Enemy settings
enemy_width = 50
enemy_height = 50
enemy_speed = 6
enemies = []

# Font
font = pygame.font.SysFont(None, 40)

# Score
score = 0

def draw_text(text, x, y):
    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))

def game_over():
    screen.fill(WHITE)
    draw_text("GAME OVER", WIDTH // 2 - 100, HEIGHT // 2 - 40)
    draw_text(f"Final Score: {score}", WIDTH // 2 - 120, HEIGHT // 2)
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += player_speed

    # Boundaries
    player_x = max(0, min(WIDTH - player_width, player_x))

    # Spawn enemies
    if random.randint(1, 30) == 1:
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemies.append(pygame.Rect(enemy_x, 0, enemy_width, enemy_height))

    # Move enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            score += 1

        # Collision
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        if enemy.colliderect(player_rect):
            game_over()

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Draw score
    draw_text(f"Score: {score}", 10, 10)

    pygame.display.update()
