import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Indic Script Guessing Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define fonts
font = pygame.font.Font(None, 48)

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
    return text_surface, transliteration

# Main game loop
def main():
    running = True
    score = 0
    while running:
        screen.fill(WHITE)

        # Display a random Devanagari character
        character_surface, transliteration = display_character()
        screen.blit(character_surface, (WIDTH // 2 - character_surface.get_width() // 2, HEIGHT // 3))

        # Display the player's score
        score_surface = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_surface, (20, 20))

        # Update the display
        pygame.display.flip()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_RETURN:
                    # Player's guess
                    player_input = input("Enter your guess (in English): ").strip().lower()
                    # Check if the guess is correct
                    if player_input == transliteration:
                        score += 1
                        print("Correct!")
                    else:
                        print(f"Incorrect! The correct answer is '{transliteration}'")

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()
