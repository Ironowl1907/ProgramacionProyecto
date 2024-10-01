import pygame
import pygame_menu
import sys

# Constants
WIDTH, HEIGHT = 800, 600
TIP_DISPLAY_TIME = 3000  # Time in milliseconds to display each tip

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Tips")

# Load Minecraft Font
font_path = r"..\res\Minecraftia-Regular.ttf"
minecraft_font = pygame.font.Font(font_path, 36)  # Main font for menu and upgrades
tip_font = pygame.font.Font(font_path, 16)  # Smaller font for tips

# Sample list of tips (replace these with your own)
tips = [
    "1. Separa tus residuos en casa: plásticos, papel, vidrio y orgánicos.",
    "2. Limpia los envases antes de reciclarlos para evitar contaminaciones.",
    "3. Infórmate sobre las normas de reciclaje en tu localidad.",
    "4. Reutiliza envases y bolsas siempre que sea posible.",
    "5. Compra productos con menos embalaje y opta por envases reciclables.",
    "6. Participa en programas de reciclaje comunitarios.",
    "7. Recicla correctamente las baterías y productos electrónicos.",
    "8. Usa papel reciclado para tus impresiones y manualidades.",
    "9. Dona ropa y objetos que ya no uses en lugar de tirarlos.",
    "10. Compostar residuos orgánicos para reducir la basura."
]

# Sample list of upgrades (replace these with your own)
upgrades = [
    {"name": "Eco-friendly packaging options", "cost": 10},
    {"name": "Improved recycling bins", "cost": 15},
    {"name": "Community workshops", "cost": 20},
]

# Game variables
points = 0
selected_upgrade_index = 0


# Function to display a tip
def display_tip(selected_tip):
    screen.fill((0, 0, 0))  # Clear screen with black background
    text_surface = tip_font.render(selected_tip, True, (255, 255, 255))  # White text using smaller font
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()


def show_tips_with_timer():
    for tip in tips:
        display_tip(tip)

        # Start a timer for displaying the tip
        start_time = pygame.time.get_ticks()

        # Wait for specified time or until Escape is pressed
        while True:
            current_time = pygame.time.get_ticks()
            if current_time - start_time >= TIP_DISPLAY_TIME:  # Time elapsed
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Allow back navigation with Escape key
                        return  # Exit to main menu


# Function to purchase an upgrade
def purchase_upgrade(upgrade):
    global points
    if points >= upgrade["cost"]:
        points -= upgrade["cost"]
        print(f"Purchased: {upgrade['name']}")
        return True
    else:
        print("Not enough points!")
        return False


# Menu function for upgrades
def upgrade_menu():
    global selected_upgrade_index

    my_theme = pygame_menu.themes.Theme(
        widget_font=font_path,
        title_font=font_path,
        widget_font_size=24,
        title_font_size=30,
        widget_font_color=(255, 255, 255),
        title_font_color=(255, 215, 0),  # Gold color for title
        background_color=(0, 0, 0)  # Black background
    )

    upgrades_menu = pygame_menu.Menu('Upgrades', WIDTH, HEIGHT,
                                     theme=my_theme)

    # Add buttons for upgrades
    for i, upgrade in enumerate(upgrades):
        upgrades_menu.add.button(f"{upgrade['name']} - Cost: {upgrade['cost']} points",
                                 lambda u=upgrade: purchase_upgrade(u))

    upgrades_menu.add.button('Back', start_menu)

    while True:
        # Handle events for the upgrades menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:  # Use Tab to navigate through upgrades
                    selected_upgrade_index = (selected_upgrade_index + 1) % len(upgrades)
                    print(f"Selected Upgrade: {upgrades[selected_upgrade_index]['name']}")
                if event.key == pygame.K_RETURN:  # Use Enter to confirm selection
                    purchase_upgrade(upgrades[selected_upgrade_index])
                if event.key == pygame.K_ESCAPE:  # Use Escape to go back (optional)
                    return  # Exit the upgrade menu

        # Update the menu display
        upgrades_menu.mainloop(screen)


# Main game loop function
def main_game_loop():
    global points

    # Simulate gaining points (for demonstration purposes)
    points += 5  # This would typically happen through gameplay events

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:  # Press Tab to open the upgrade menu
                    upgrade_menu()

        # Update screen with current points (optional)
        screen.fill((0, 0, 0))  # Clear screen with black background
        point_surface = minecraft_font.render(f"Puntos: {points}", True, (255, 255, 255))
        screen.blit(point_surface, (10, 10))
        pygame.display.flip()


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

    menu = pygame_menu.Menu('Recycled Space', WIDTH, HEIGHT,
                            theme=my_theme)

    menu.add.button('Tips de reciclaje!', show_tips_with_timer)

    menu.add.button('Empezar juego', main_game_loop)  # Start the main game loop

    menu.add.button('Mejoras', upgrade_menu)

    menu.add.button('Salir', pygame_menu.events.EXIT)

    menu.mainloop(screen)


if __name__ == "__main__":
    start_menu()