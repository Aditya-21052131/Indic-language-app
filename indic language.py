import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Devanagari Script Learning Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define fonts
font = pygame.font.Font(None, 36)

# Define Devanagari characters and their corresponding English transliterations
characters = {
    "अ": "a",
    "आ": "aa",
    "इ": "i",
    "ई": "ee",
    "उ": "u",
    "ऊ": "oo",
    # Add more characters as needed
}

# Function to display a random Devanagari character
def display_character():
    character, transliteration = random.choice(list(characters.items()))
    text_surface = font.render(character, True, BLACK)
    transliteration_surface = font.render(f"({transliteration})", True, BLACK)
    return text_surface, transliteration_surface

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    # Display a random Devanagari character and its transliteration
    character_surface, transliteration_surface = display_character()
    screen.blit(character_surface, (WIDTH // 2 - character_surface.get_width() // 2, HEIGHT // 3))
    screen.blit(transliteration_surface, (WIDTH // 2 - transliteration_surface.get_width() // 2, HEIGHT // 2))

    # Update the display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
