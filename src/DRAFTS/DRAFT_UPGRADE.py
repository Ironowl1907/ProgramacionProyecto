## Maybe this can be useful for the upgrades
## have to adapt it to the current code

# Sample list of upgrades
upgrades = weapons_upgrades # import from upgrades.py

# Game variables
points = main.points
selected_upgrade_index = 0


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

    upgrades_menu = pygame_menu.Menu('Mejoras', WIDTH, HEIGHT,
                                     theme=my_theme)

    # Add buttons for upgrades
    for i, upgrade in enumerate(upgrades):
        upgrades_menu.add.button(f"{upgrade.name} - Costo: {upgrade.cost} puntos",
                                 lambda u=upgrade: purchase_upgrade(u))

    upgrades_menu.add.button('Atras', start_menu)

    while True:
        # Handle events for the upgrades menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_TAB:  # Use Tab to navigate through upgrades
                    selected_upgrade_index = (
                        selected_upgrade_index + 1) % len(upgrades)
                    print(f"Mejora Seleccionada: {
                          upgrades[selected_upgrade_index].name}")
                if event.key == pygame.K_RETURN:  # Use Enter to confirm selection
                    purchase_upgrade(upgrades[selected_upgrade_index])
                # Use Escape to go back (optional)
                if event.key == pygame.K_ESCAPE:
                    return  # Exit the upgrade menu

        # Update the menu display
        upgrades_menu.mainloop(screen)

# Function to purchase an upgrade
def purchase_upgrade(upgrade):
    global points
    if points >= upgrade.cost:
        points -= upgrade.cost
        success_message = f"Purchased: {upgrade.name}"
        print(success_message)
        display_message(success_message)  # Display success message
        return True
    else:
        error_message = f"Not enough points! You have {points} points."
        print(error_message)
        display_message(error_message)  # Display error message
        return False