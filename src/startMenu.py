import pygame
import pygame_menu
import sys
from main import mainGame

# Constants
WIDTH, HEIGHT = 800, 600
TIP_DISPLAY_TIME = 3000  # Time in milliseconds to display each tip

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AstroScraps")

# Load Minecraft Font
font_path = r"../res/Fonts/Minecraftia-Regular.ttf"

# Load the background image
background_image = pygame.image.load("../res/Background.png").convert()

# Main font for menu and upgrades
minecraft_font = pygame.font.Font(font_path, 50)
tip_font = pygame.font.Font(font_path, 20)  # Smaller font for tips


# Function to display credits
def display_credits():
    # Title and sample credits text
    title_text = "Credits"
    credits_text = [
        "Game Developed by: Facundo Guiñazú, Bautista Prieto",
        "Graphics by: Nicolas Manescau",
        "Music by: Felipe Verri",
        "Project Manager: Cristobal Gonzalez", "",
        "Press ESC to return to the main menu"
    ]

    # Clear screen with background image
    screen.blit(background_image, (0, 0))

    # Render title
    title_surface = minecraft_font.render(
        title_text, True, (255, 215, 0))  # Gold color for title
    title_rect = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 4))  # Centered at the top
    screen.blit(title_surface, title_rect)

    # Render each line of credits
    for i, line in enumerate(credits_text):
        text_surface = tip_font.render(
            line, True, (153, 229, 80))
        text_rect = text_surface.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + i * 30))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()  # Update the display

    # Wait for player input to return
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Allow back navigation with Escape key
                    return  # Exit to main menu


# Function to display Player_tutorial sprite with "How to Play" title and background
def display_how_to_play():
    # Load the Player_tutorial sprite
    player_sprite = pygame.image.load("../res/Player/Player_tutorial.png")

    # Set the new size (for example, 127x87 scaled by 4)
    new_width, new_height = 127 * 4, 87 * 4
    player_sprite = pygame.transform.scale(player_sprite, (new_width, new_height))

    # Get the rect for the resized sprite and center it
    player_rect = player_sprite.get_rect(center=(WIDTH // 2, (HEIGHT // 2) + 50))  # Centered on screen

    # Clear screen with the background image
    screen.blit(background_image, (0, 0))  # Background fills the screen

    # Render "How to Play" title
    title_surface = minecraft_font.render("How to Play", True, (255, 215, 0))  # Gold color
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 7))  # Position near the top
    screen.blit(title_surface, title_rect)

    # Render the Player_tutorial sprite
    screen.blit(player_sprite, player_rect)

    pygame.display.flip()  # Update the display

    # Wait for player input to return
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Allow back navigation with Escape key
                    return  # Exit to main menu


def start_menu():
    # Clear the screen with the background image
    screen.blit(background_image, (0, 0))  # Fill with the background image

    my_theme = pygame_menu.themes.Theme(
        widget_font=font_path,
        title_font=font_path,
        widget_font_size=20,
        title_font_size=50,
        widget_font_color=(153, 229, 80),
        title_font_color=(255, 215, 0),  # Gold color for title
        background_color=(0, 0, 0, 0)  # Set to transparent background to allow bgfun to work
    )

    menu = pygame_menu.Menu(title='/////', width=WIDTH,
                            height=HEIGHT, theme=my_theme)

    # Position the title label correctly
    menu.add.label(title="AstroScraps!",
                   font_size=50, font_color=(255, 215, 0), margin=(20, 20))

    menu.add.button('Start Game', mainGame)  # Start the main game loop

    menu.add.button('How to Play?', display_how_to_play)

    menu.add.button('Credits', display_credits)

    menu.add.button('Exit', pygame_menu.events.EXIT)

    # Use bgfun to continuously display the background image during the menu loop
    menu.mainloop(screen, bgfun=lambda: screen.blit(background_image, (0, 0)))


if __name__ == "__main__":
    start_menu()