import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Awesome Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Fonts
font_large = pygame.font.SysFont("Arial", 64)
font_small = pygame.font.SysFont("Arial", 32)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    rect = img.get_rect(center=(x, y))
    screen.blit(img, rect)

def start_screen():
    waiting = True
    while waiting:
        screen.fill(BLACK)
        
        # Display Title and Instructions
        draw_text("GALACTIC QUEST", font_large, WHITE, WIDTH // 2, HEIGHT // 3)
        draw_text("Press SPACE to Start", font_small, GRAY, WIDTH // 2, HEIGHT // 2)
        draw_text("Press Q to Quit", font_small, GRAY, WIDTH // 2, HEIGHT // 2 + 50)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False  # Exit the start screen loop
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def main_game():
    # This is where your actual game logic would go
    run = True
    while run:
        screen.fill((0, 50, 100)) # Change background to show we've started
        draw_text("THE GAME IS RUNNING!", font_small, WHITE, WIDTH // 2, HEIGHT // 2)
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

# --- Execution Flow ---
start_screen()
main_game()
pygame.quit()