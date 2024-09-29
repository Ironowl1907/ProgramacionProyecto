import pygame
import sys

pygame.init()

# Constants
SCREEN_SIZE = (1200, 710)
CENTER_WIDTH = 600
FPS = 60
SIDE_WIDTH = (SCREEN_SIZE[0] - CENTER_WIDTH) // 2
ITEM_SCALE, SHIP_SIZE, TRASH_START_POS = (50, 50), (75, 75), (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] - 100)
TRASH_MOVE_AMOUNT, ENEMY_SPEED, WAVE_COOLDOWN, LIFE_COOLDOWN = 10, 2, 5000, 2000

# Colors
COLORS = {"white": (255, 255, 255), "green": (0, 100, 0), "blue": (0, 0, 100)}

# Load and scale images
def load_and_scale_image(path, size):
    """Load an image from a given path and scale it to the specified size."""
    return pygame.transform.scale(pygame.image.load(path), size)

# Initialize game elements
ship_image = load_and_scale_image("Player.png", SHIP_SIZE)
ship_rect = ship_image.get_rect(center=TRASH_START_POS)
enemy_image = load_and_scale_image("Enemy.png", ITEM_SCALE)

# Scale trash to match the white screen area
trash_image = load_and_scale_image("Trash.png", (CENTER_WIDTH, SCREEN_SIZE[1] * 2))
trash_rect = trash_image.get_rect(midtop=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1]))  # Initial position below the screen

# Trash state variables
trash_active = False
trash_steps_remaining = 0

# Load weapon images and items
weapon_names = ["beam", "saw", "laser"]
weapon_images = {name: load_and_scale_image(f"Player_{name}.png", SHIP_SIZE if name != "laser" else (50, 1000)) for name in weapon_names}

def load_weapon_items(name):
    """Load weapon item images based on name and scale them."""
    suffixes = ["", "_II", "_III"]
    return [load_and_scale_image(f"Player_{name}_item{suffix}.png", ITEM_SCALE) for suffix in suffixes]

weapon_items = {name: load_weapon_items(name) for name in weapon_names}
weapon_cooldowns = [250, 500, 2000]
weapons = [{"name": name, "image": weapon_images[name], "cooldown": cd, "items": weapon_items[name]} for name, cd in zip(weapon_names, weapon_cooldowns)]

# Game state variables
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Integrative Game")
clock = pygame.time.Clock()
current_weapon, bullet_list, enemy_list = 0, [], []
last_shot_time = last_weapon_change_time = last_wave_time = pygame.time.get_ticks()
item_display_start_time, current_item_image, laser_active = None, None, False
lives, last_life_loss_time = 3, 0

def generate_enemies():
    """Generate enemies in a triangle formation."""
    for offset in [0, -50, 50]:
        enemy_list.append(enemy_image.get_rect(center=(SCREEN_SIZE[0] // 2 + offset, -50)))

# Initial enemy wave
generate_enemies()

def handle_events():
    """Handle all pygame events."""
    global current_weapon, last_shot_time, last_weapon_change_time, current_item_image, item_display_start_time, laser_active
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        current_time = pygame.time.get_ticks()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in [4, 5] and current_time - last_weapon_change_time >= 1500:
                current_weapon = (current_weapon + (1 if event.button == 4 else -1)) % len(weapons)
                last_weapon_change_time, item_display_start_time = current_time, current_time
                current_item_image = weapons[current_weapon]["items"][0]

            if event.button in [1, 3] and current_time - last_shot_time >= weapons[current_weapon]["cooldown"]:
                bullet_list.append({
                    "rect": weapons[current_weapon]["image"].get_rect(centerx=ship_rect.centerx, bottom=ship_rect.top + (20 if current_weapon != 2 else 0)),
                    "weapon": current_weapon, "creation_time": current_time})
                last_shot_time = current_time
                laser_active = (current_weapon == 2 and not laser_active)

def move_ship():
    """Move the ship left or right based on key input with screen boundaries."""
    keys = pygame.key.get_pressed()
    ship_rect.move_ip((-3 if keys[pygame.K_LEFT] else 3 if keys[pygame.K_RIGHT] else 0), 0)
    ship_rect.left = max(ship_rect.left, SIDE_WIDTH)
    ship_rect.right = min(ship_rect.right, SIDE_WIDTH + CENTER_WIDTH)

def move_entities(entities, speed):
    """Move a list of entities by a given speed."""
    for entity in entities:
        entity.move_ip(0, speed)

def update_bullets():
    """Update bullet positions and handle laser fading."""
    global laser_active
    current_time = pygame.time.get_ticks()
    for bullet in bullet_list[:]:
        # Laser handling (weapon 2)
        if bullet["weapon"] == 2:
            alpha = max(255 - (current_time - bullet["creation_time"]) / 2000 * 255, 0)
            if alpha <= 0:
                bullet_list.remove(bullet)
                laser_active = False
            else:
                # Reset alpha to prevent shared image modification issues
                bullet_image = weapon_images["laser"].copy()
                bullet_image.set_alpha(int(alpha))
                bullet["image"] = bullet_image
        else:
            # Set different speeds for bullets (beam), saw, and laser
            speed = -7 if bullet["weapon"] == 0 else -3 if bullet["weapon"] == 1 else 0
            bullet["rect"].move_ip(0, speed)
            # Remove bullet if it goes off-screen
            if bullet["rect"].bottom < 0:
                bullet_list.remove(bullet)

def check_collisions():
    """Check for collisions between bullets, enemies, and the player."""
    global lives, last_life_loss_time, trash_active, trash_steps_remaining
    for bullet in bullet_list[:]:
        for enemy in enemy_list[:]:
            if bullet["rect"].colliderect(enemy):
                bullet_list.remove(bullet)
                enemy_list.remove(enemy)
                trash_active = True
                trash_steps_remaining += 5  # Set the number of steps the trash will move upward
                break

    for enemy in enemy_list[:]:
        if ship_rect.colliderect(enemy) and pygame.time.get_ticks() - last_life_loss_time >= LIFE_COOLDOWN:
            lives -= 1
            last_life_loss_time = pygame.time.get_ticks()

            # Reset player and trash to starting positions
            ship_rect.center = TRASH_START_POS
            trash_rect.midtop = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1])

            # Deactivate trash movement
            trash_active = False
            trash_steps_remaining = 0

            # Clear enemies
            enemy_list.clear()

def draw_screen():
    """Clear the screen and draw all game elements."""
    screen.fill(COLORS["white"])
    pygame.draw.rect(screen, COLORS["green"], (0, 0, SIDE_WIDTH, SCREEN_SIZE[1]))
    pygame.draw.rect(screen, COLORS["blue"], (SIDE_WIDTH + CENTER_WIDTH, 0, SIDE_WIDTH, SCREEN_SIZE[1]))
    pygame.draw.rect(screen, COLORS["white"], (SIDE_WIDTH, 0, CENTER_WIDTH, SCREEN_SIZE[1]))

    # Draw trash in the background of the white area
    screen.blit(trash_image, trash_rect)

    # Display lives
    lives_text = pygame.font.Font(None, 36).render(f"Lives: {lives}", True, (255, 0, 0))
    screen.blit(lives_text, (SIDE_WIDTH + 10, 10))

    # Draw weapon items
    item_positions = [(45, 150), (123, 150), (200, 150)]  # Update these positions if needed
    for i, (key, pos) in enumerate(zip(weapon_items, item_positions)):
        for j, item in enumerate(weapon_items[key]):
            screen.blit(item, (pos[0], pos[1] + j * 60))

    screen.blit(ship_image, ship_rect)
    for bullet in bullet_list:
        screen.blit(bullet.get("image", weapons[bullet["weapon"]]["image"]), bullet["rect"])
    for enemy in enemy_list:
        screen.blit(enemy_image, enemy)

    if current_item_image and (pygame.time.get_ticks() - item_display_start_time < 2000):
        screen.blit(current_item_image, current_item_image.get_rect(center=(ship_rect.centerx, ship_rect.top - 30)))

def handle_waves():
    """Handle the generation of new enemy waves."""
    global last_wave_time
    if not enemy_list and pygame.time.get_ticks() - last_wave_time >= WAVE_COOLDOWN:
        generate_enemies()
        last_wave_time = pygame.time.get_ticks()

def move_trash_and_objects():
    """Move trash and the player upward in discrete steps."""
    global trash_steps_remaining, trash_active
    if trash_active and trash_steps_remaining > 0:
        # Move trash upward by a fixed amount
        trash_rect.move_ip(0, -TRASH_MOVE_AMOUNT)
        trash_steps_remaining -= 1

        # Check if trash has moved above the screen
        if trash_rect.bottom <= 0:
            trash_active = False
            trash_steps_remaining = 0
            return

        # Move the player if the trash is colliding with the player
        # Check if the bottom of the trash is above the top of the player
        if ship_rect.colliderect(trash_rect):
            ship_rect.move_ip(0, -TRASH_MOVE_AMOUNT)

# Main game loop
while True:
    handle_events()
    move_ship()
    move_entities(enemy_list, ENEMY_SPEED)
    update_bullets()
    check_collisions()
    move_trash_and_objects()
    draw_screen()
    handle_waves()
    pygame.display.flip()
    clock.tick(FPS)