import pygame
import pygame_menu
import sys
import src.main

# Constants
WIDTH, HEIGHT = 800, 600
TIP_DISPLAY_TIME = 3000  # Time in milliseconds to display each tip

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Astroscraps")

# Load Minecraft Font
font_path = r"../../res/Fonts/Minecraftia-Regular.ttf"

# Main font for menu and upgrades
minecraft_font = pygame.font.Font(font_path, 36)
tip_font = pygame.font.Font(font_path, 16)  # Smaller font for tips


# Function to display credits
def display_credits():
    # Title and sample credits text
    title_text = "Credits"
    credits_text = [
        "Game Developed by: Facundo Guiñazú, Bautista Prieto",
        "Graphics by: Nicolas Manescau",
        "Music by: Nicolas Manescau",
        "Press ESC to return to the main menu"
    ]

    # Clear screen with black background
    screen.fill((0, 0, 0))

    # Render title
    title_surface = minecraft_font.render(title_text, True, (255, 215, 0))  # Gold color for title
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))  # Centered at the top
    screen.blit(title_surface, title_rect)

    # Render each line of credits
    for i, line in enumerate(credits_text):
        text_surface = tip_font.render(line, True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 30))  # Adjust vertical position
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

def start_menu():
    my_theme = pygame_menu.themes.Theme(
        widget_font=font_path,
        title_font=font_path,
        widget_font_size=24,
        title_font_size=30,
        widget_font_color=(255, 255, 255),
        title_font_color=(255, 215, 0),  # Gold color for title
        background_color=(0, 0, 0)  # Black background
    )

    menu = pygame_menu.Menu(title='/////', width=WIDTH, height=HEIGHT, theme=my_theme)

    menu.add.label(title="Bienvenido a Recycled Space!", font_size=36, font_color=(255, 215, 0), margin=(20, 20))

    menu.add.button('Empezar juego', src.main.mainGame)  # Start the main game loop

    menu.add.button('Creditos', display_credits)

    menu.add.button('Salir', pygame_menu.events.EXIT)

    menu.mainloop(screen)


if __name__ == "__main__":
    start_menu()
