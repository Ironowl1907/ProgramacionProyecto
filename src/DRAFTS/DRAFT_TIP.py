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

# Function to display a tip
def display_tip(selected_tip):
    screen.fill((0, 0, 0))  # Clear screen with black background
    # White text using smaller font
    text_surface = tip_font.render(selected_tip, True, (255, 255, 255))
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

# Function to display messages
def display_message(message):
    screen.fill((0, 0, 0))  # Clear screen with black background
    text_surface = tip_font.render(message, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)  # Display message for 2 seconds
