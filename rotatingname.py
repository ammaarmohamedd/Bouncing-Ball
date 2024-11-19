import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enhanced Ball Game with Stars")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Clock for controlling the frame rate
clock = pygame.time.Clock()
FPS = 60

# Ball properties
ball_radius = 15
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 5

# Paddle properties
paddle_width = 120
paddle_height = 15
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - 40
paddle_speed = 8

# Star properties
star_radius = 10
star_x = random.randint(50, WIDTH - 50)
star_y = random.randint(50, HEIGHT // 2)
star_active = True

# Game variables
score = 0
running = True

# Font for displaying the score
font = pygame.font.Font(None, 36)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddle with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddle
    if (
        paddle_y <= ball_y + ball_radius <= paddle_y + paddle_height
        and paddle_x <= ball_x <= paddle_x + paddle_width
    ):
        ball_speed_y = -ball_speed_y
        score += 1

    # Ball falls below the screen
    if ball_y - ball_radius > HEIGHT:
        print("Game Over! Your score:", score)
        running = False

    # Check for star collection
    if star_active and ((ball_x - star_x) ** 2 + (ball_y - star_y) ** 2) ** 0.5 < ball_radius + star_radius:
        score += 5
        star_active = False  # Star disappears once collected

    # Respawn the star
    if not star_active:
        star_x = random.randint(50, WIDTH - 50)
        star_y = random.randint(50, HEIGHT // 2)
        star_active = True

    # Clear the screen and draw the background
    screen.fill(BLACK)

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Draw the paddle
    pygame.draw.rect(screen, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw the star
    if star_active:
        pygame.draw.circle(screen, YELLOW, (star_x, star_y), star_radius)

    # Draw the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
