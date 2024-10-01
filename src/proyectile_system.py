import pygame
from pygame.math import Vector2
import conf as conf


class ProjectileType():
    BASIC = 0
    BASICENEMY = 1
    SAW = 2
    LASER = 2


direction = pygame.Vector2(0, -1)


class Projectile(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, direction, rotation: int, projType: int):
        super().__init__()
        self.spritePath = ""
        match projType:
            case ProjectileType.BASIC:
                self.spritePath = "../res/Player_beam.png"
            case ProjectileType.BASICENEMY:
                self.spritePath = "../res/Enemy_beam.png"
            case ProjectileType.SAW:
                self.spritePath = "../res/Player_saw.png"
            case ProjectileType.LASER:
                self.spritePath = "../res/Player_beam.png"

        self.original_image = pygame.image.load(self.spritePath)
        self.original_image = pygame.transform.scale(
            self.original_image, (20, 30))
        self.image = pygame.transform.rotate(self.original_image, -rotation)
        self.rect = self.image.get_rect(center=position)

        self.projType = projType
        self.direction = direction.normalize()  # Already rotated by the player
        self.speed = conf.PROJECTILE_SPEED

    def update(self):
        self.rect.x += int(self.direction.x * self.speed)
        self.rect.y += int(self.direction.y * self.speed)

        if (self.rect.right < 0 or self.rect.left > conf.WIDTH or
                self.rect.bottom < 0 or self.rect.top > conf.HEIGHT):
            self.kill()

    def draw(self, surface):
        if conf.SHOWHITBOX:
            pygame.draw.rect(surface, conf.GREEN, self.rect)
        surface.blit(self.image, self.rect)
