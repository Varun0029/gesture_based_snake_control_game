import pygame
import random
import serial
import time

# --- Setup Serial (change COM port if needed) ---
ser = serial.Serial("COM5", 115200, timeout=1)  # Replace COM5 with your port
time.sleep(2)

# --- Pygame Setup ---
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - MPU6050 Gesture Control")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake setup
snake = [(100, 50), (90, 50), (80, 50)]
snake_dir = "RIGHT"
change_to = snake_dir
last_command = None   # To reduce sensitivity (ignore repeats)

# Food setup
food_pos = [random.randrange(1, WIDTH//CELL) * CELL,
            random.randrange(1, HEIGHT//CELL) * CELL]
FOOD_TIMEOUT = 10   # seconds to eat food
food_timer_start = time.time()
food_respawn_time = None

# Score
score = 0
font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()

def show_score():
    score_surface = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_surface, (10, 10))

# --- Main Game Loop ---
running = True
while running:
    # --- Read from Serial ---
    if ser.in_waiting > 0:
        line = ser.readline().decode("utf-8").strip()

        # Fix: invert LEFT/RIGHT if needed
        if line == "LEFT":
            line = "RIGHT"
        elif line == "RIGHT":
            line = "LEFT"

        if line in ["UP", "DOWN", "LEFT", "RIGHT"]:
            if line != last_command:  # ignore repeats
                change_to = line
                last_command = line

    # --- Keyboard fallback (optional) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Change direction (no 180° turns allowed)
    if change_to == "UP" and snake_dir != "DOWN":
        snake_dir = "UP"
    if change_to == "DOWN" and snake_dir != "UP":
        snake_dir = "DOWN"
    if change_to == "LEFT" and snake_dir != "RIGHT":
        snake_dir = "LEFT"
    if change_to == "RIGHT" and snake_dir != "LEFT":
        snake_dir = "RIGHT"

    # Move snake
    x, y = snake[0]
    if snake_dir == "UP":
        y -= CELL
    if snake_dir == "DOWN":
        y += CELL
    if snake_dir == "LEFT":
        x -= CELL
    if snake_dir == "RIGHT":
        x += CELL

    # Wrap around screen
    x = x % WIDTH
    y = y % HEIGHT

    new_head = (x, y)
    snake.insert(0, new_head)

    # --- Food timer handling ---
    if food_timer_start is not None:
        if time.time() - food_timer_start >= FOOD_TIMEOUT:
            food_pos = None       # food disappears
            food_timer_start = None
            food_respawn_time = time.time() + 2  # respawn after 2s

    # Respawn food after delay
    if food_pos is None and food_respawn_time is not None and time.time() >= food_respawn_time:
        food_pos = [random.randrange(1, WIDTH//CELL) * CELL,
                    random.randrange(1, HEIGHT//CELL) * CELL]
        food_timer_start = time.time()
        food_respawn_time = None

    # --- Eating food ---
    if food_pos is not None:
        head_rect = pygame.Rect(x, y, CELL, CELL)
        food_rect = pygame.Rect(food_pos[0], food_pos[1], CELL, CELL)
        if head_rect.colliderect(food_rect):
            score += 1
            food_pos = None
            food_timer_start = None
            food_respawn_time = time.time() + 2
        else:
            snake.pop()  # only remove tail if no food eaten
    else:
        snake.pop()  # keep snake moving

    # --- Game Over: snake touches itself ---
    if new_head in snake[1:]:
        running = False

    # --- Draw everything ---
    screen.fill(BLACK)

    # Draw snake
    for i, pos in enumerate(snake):
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], CELL, CELL))

    # Draw snake eyes on head
    head_x, head_y = snake[0]
    eye_radius = 3
    if snake_dir == "UP":
        eye1 = (head_x + 5, head_y + 5)
        eye2 = (head_x + 15, head_y + 5)
    elif snake_dir == "DOWN":
        eye1 = (head_x + 5, head_y + 15)
        eye2 = (head_x + 15, head_y + 15)
    elif snake_dir == "LEFT":
        eye1 = (head_x + 5, head_y + 5)
        eye2 = (head_x + 5, head_y + 15)
    elif snake_dir == "RIGHT":
        eye1 = (head_x + 15, head_y + 5)
        eye2 = (head_x + 15, head_y + 15)
    pygame.draw.circle(screen, WHITE, eye1, eye_radius)
    pygame.draw.circle(screen, WHITE, eye2, eye_radius)

    # Draw food as a circle
    if food_pos is not None:
        pygame.draw.circle(screen, RED, (food_pos[0] + CELL//2, food_pos[1] + CELL//2), CELL//2)

    show_score()
    pygame.display.update()
    clock.tick(10)  # Game speed

pygame.quit()
