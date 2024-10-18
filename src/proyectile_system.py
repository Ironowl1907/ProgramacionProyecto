import random as rand
import pygame
from pygame.math import Vector2
import conf as conf


class ProjectileType():
    BASIC = 0
    SAW = 1
    # LASER = 2
    NET = 2
    BASICENEMY = 3


direction = pygame.Vector2(0, -1)


class Projectile(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, direction, rotation: int, projType: int):
        super().__init__()
        self.spritePath = ""
        self.scaleVector = (1, 1)
        match projType:
            case ProjectileType.BASIC:
                self.spritePath = "../res/Player/Player_Items/Player_Bullet.png"
                self.scaleVector = (20, 30)
            case ProjectileType.BASICENEMY:
                self.spritePath = "../res/Enemy/Enemy_Bullet.png"
                self.scaleVector = (20, 30)
            case ProjectileType.SAW:
                self.spritePath = "../res/Player/Player_Items/Player_Saw.png"
                self.scaleVector = (80, 80)
            # case ProjectileType.LASER:
            #     self.spritePath = "../res/Player/Player_Items/Player_Laser.png"
            case ProjectileType.NET:
                self.spritePath = "../res/Player/Player_Items/Player_Web.png"
                self.scaleVector = (80, 80)

        self.rotation = rotation
        self.original_image = pygame.image.load(self.spritePath)
        self.original_image = pygame.transform.scale(
            self.original_image, self.scaleVector)
        self.image = pygame.transform.rotate(
            self.original_image, -self.rotation)
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

    def randDir(self):
        ranf = rand.random()
        self.direction = Vector2(ranf, 1 - ranf)

    def draw(self, surface):
        if conf.SHOWHITBOX:
            pygame.draw.rect(surface, conf.GREEN, self.rect)

        if self.projType == ProjectileType.SAW:
            self.rotation += conf.SAWSPEED
            self.image = pygame.transform.rotate(
                self.original_image, -self.rotation)
        surface.blit(self.image, self.rect)
