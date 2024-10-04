from pygame.math import Vector2
import progressBar as pb
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

        self.original_image = pygame.image.load("../res/Enemy/Enemy.png")
        self.image = pygame.transform.scale(
            self.original_image, (50, 50))

        self.killed_original_image = pygame.image.load(
            "../res/Enemy/Destroyed_Enemy.png")
        self.killed_image = pygame.transform.scale(
            self.killed_original_image, (50, 50))

        self.rect = self.image.get_rect(center=self.position)

        self.proyectileGoup = proyectileGroup
        self.shootCooldown = 0

        self.randMovCooldown = 0
        self.randMove = Vector2(0)

        self.killed = False
        self.despawnLeftTime = 0

    def update(self, deltaTime: float, playerPosition: Vector2, enemyGroup: Group):
        if not self.killed:
            self.direction = playerPosition - self.position
        self.randMovCooldown += deltaTime
        self.shootCooldown += deltaTime
        if self.randMovCooldown >= conf.RANDCOOLDOWN:
            self.randMovCooldown = 0
            self.randMove = Vector2(
                rand.random(), rand.random()) * conf.RANDMULTILIER

        if not self.killed:
            self.rotatingAngle = math.degrees(
                math.atan2(self.direction.y, self.direction.x))

            self.rotatingAngle -= 90

        else:
            self.rotatingAngle += conf.KILLEDROTATIONSPEED
            self.despawnLeftTime -= deltaTime
            if self.despawnLeftTime <= 0:
                enemyGroup.remove(self)

        if self.randMovCooldown >= conf.ENEMYSHOOTCOOLDOWN and \
                rand.randint(1, conf.ENEMYSHOOTRAND) == 1 and not \
                self.killed:
            self.shootCooldown = 0
            self.shoot(self.proyectileGoup)

        self._update_position()
        self._check_boundaries()

    def _update_position(self):
        if not self.killed:
            self.direction = self.direction.normalize() * self.speed + self.randMove
            self.position += self.direction
        else:
            self.position += self.direction * conf.RUBBISHSPEEDMUL

        self.rect.center = (int(self.position.x), int(self.position.y))

    def _check_boundaries(self):
        self.position.x = max(
            0, min(self.position.x, conf.WIDTH - self.rect.width))
        self.position.y = max(
            -100, min(self.position.y, conf.HEIGHT - self.rect.height))

    def draw(self, surface):
        if conf.SHOWHITBOX:
            pygame.draw.rect(surface, conf.RED, self.rect)

        if not self.killed:
            rotated_image = pygame.transform.rotate(
                self.image, -self.rotatingAngle)
            rotated_rect = rotated_image.get_rect(
                center=self.rect.center)

        else:
            pb.draw_progress_bar(Vector2(self.position.x, self.position.y+30),
                                 self.despawnLeftTime/conf.AFTERKILLTIME, surface)
            rotated_image = pygame.transform.rotate(
                self.killed_image, -self.rotatingAngle)
            rotated_rect = rotated_image.get_rect(
                center=self.rect.center)

        surface.blit(rotated_image, rotated_rect)

    def kill(self):
        if not self.killed:
            self.killed = True
            self.despawnLeftTime = conf.AFTERKILLTIME

    def shoot(self, projectileGroup: Group):
        projectile_sound = pygame.mixer.Sound(conf.BASIC_PROJECTILE_SOUND)
        projectile_sound.set_volume(conf.PROJECTILE_VOLUME)
        projectile_sound.play()
        direction = pygame.Vector2(0, 1).rotate(self.rotatingAngle)
        front_position = self.position + direction * (self.rect.height / 2)

        projectile = proy.Projectile(
            front_position, direction, int(self.rotatingAngle), proy.ProjectileType.BASICENEMY)
        projectileGroup.add(projectile)
