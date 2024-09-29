from pygame.math import Vector2
import random as rand
import math
import proyectile_system as proy
from pygame.sprite import Group
import conf
import pygame

# Enemy class


class Enemy(pygame.sprite.Sprite):

    def __init__(self, proyectileGroup: Group, x: int = 0, y: int = 0):
        super().__init__()
        self.position = Vector2(x, y)

        self.speed = conf.ENEMY_SPEED
        self.rotatingAngle = 0
        self.direction = Vector2(0)

        self.original_image = pygame.image.load("../res/Enemy.png")
        self.image = pygame.transform.scale(
            self.original_image, (50, 50))
        self.rect = self.image.get_rect(center=self.position)

        self.proyectileGoup = proyectileGroup
        self.lastShot = 0

        self.randMovCooldown = 0
        self.randMove = Vector2(0)

    def update(self, deltaTime: float, playerPosition: Vector2):
        self.direction = playerPosition - self.position
        self.randMovCooldown += deltaTime
        if self.randMovCooldown >= conf.RANDCOOLDOWN:
            self.randMovCooldown = 0
            self.randMove = Vector2(
                rand.random(), rand.random()) * conf.RANDMULTILIER

        self.rotatingAngle = math.degrees(
            math.atan2(self.direction.y, self.direction.x))

        self.rotatingAngle -= 90

        self.lastShot += deltaTime
        self._update_position()
        self._check_boundaries()

    def _update_position(self):
        self.position += self.direction.normalize() * self.speed
        self.position += self.randMove
        self.rect.center = (int(self.position.x), int(self.position.y))

    def _check_boundaries(self):
        self.position.x = max(
            0, min(self.position.x, conf.WIDTH - self.rect.width))
        self.position.y = max(
            0, min(self.position.y, conf.HEIGHT - self.rect.height))

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(
            self.image, -self.rotatingAngle)
        rotated_rect = rotated_image.get_rect(
            center=self.rect.center)

        surface.blit(rotated_image, rotated_rect)

    def shoot(self, projectileGroup: Group):
        if self.lastShot >= conf.PROJECTILE_COOLDOWN:
            direction = pygame.Vector2(0, -1).rotate(self.rotatingAngle)

            front_position = self.position + direction * (self.rect.height / 2)

            projectile = proy.Projectile(
                front_position, direction, int(self.rotatingAngle))
            projectileGroup.add(projectile)

            self.lastShot = 0
