import pygame
import conf as conf

direction = pygame.Vector2(0, -1)


class Projectile(pygame.sprite.Sprite):
    def __init__(self, position, direction, rotation: int):
        super().__init__()
        # Load the sprite image
        self.original_image = pygame.image.load("../res/Player_beam.png")
        self.original_image = pygame.transform.scale(
            self.original_image, (100, 100))  # Adjust size if necessary

        # Rotate the image based on the player's rotation
        self.image = pygame.transform.rotate(self.original_image, -rotation)

        # Set rect at the front position
        self.rect = self.image.get_rect(center=position)

        # Direction and speed
        self.direction = direction.normalize()  # Already rotated by the player
        self.speed = conf.PROJECTILE_SPEED

    def update(self):
        # Move the projectile in the specified direction
        self.rect.x += int(self.direction.x * self.speed)
        self.rect.y += int(self.direction.y * self.speed)

        # Remove the projectile if it goes off-screen
        if (self.rect.right < 0 or self.rect.left > conf.WIDTH or
                self.rect.bottom < 0 or self.rect.top > conf.HEIGHT):
            self.kill()  # Remove the sprite from all sprite groups
