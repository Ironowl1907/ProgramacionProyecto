import pygame
import conf as conf

direction = pygame.Vector2(0, -1)


class Projectile(pygame.sprite.Sprite):
    def __init__(self, position, direction, rotation: int):
        super().__init__()
        self.original_image = pygame.image.load("../res/Player_beam.png")
        self.original_image = pygame.transform.scale(
            self.original_image, (50, 50))  # Adjust size if necessary

        self.image = pygame.transform.rotate(self.original_image, -rotation)
        self.rect = self.image.get_rect(center=position)

        self.direction = direction.normalize()  # Already rotated by the player
        self.speed = conf.PROJECTILE_SPEED

    def update(self):
        self.rect.x += int(self.direction.x * self.speed)
        self.rect.y += int(self.direction.y * self.speed)

        if (self.rect.right < 0 or self.rect.left > conf.WIDTH or
                self.rect.bottom < 0 or self.rect.top > conf.HEIGHT):
            self.kill()  # Remove the sprite from all sprite groups

    def draw(self, surface):
        if conf.SHOWHITBOX:
            pygame.draw.rect(surface, conf.GREEN, self.rect)
        surface.blit(self.image, self.rect)
