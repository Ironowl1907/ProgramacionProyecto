import proyectile_system as proy
from pygame.sprite import Group
import conf
import pygame

# Player class


class Player(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, proyectileGroup: Group):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0)

        self.original_image = pygame.image.load("../res/Player.png")
        self.image = pygame.transform.scale(
            self.original_image, (50, 50))  # Resize if necessary
        self.rect = self.image.get_rect(center=self.position)
        self.speed = conf.PLAYER_SPEED
        self.proyectileGoup = proyectileGroup
        self.lastShot = 0
        self.rotatingAngle = 0
        self.invencibleTime = conf.INVENCIBLETIME

    def update(self, deltaTime: float):
        self.lastShot += deltaTime
        self._apply_deceleration(deltaTime)
        self._update_position()
        self._check_boundaries()

    def _apply_deceleration(self, deltaTime: float):
        if self.velocity.length() > 0:
            self.velocity *= (1 - conf.PLAYER_DEACELERATION * deltaTime)

    def _update_position(self):
        self.position += self.velocity
        self.rect.center = (int(self.position.x), int(self.position.y))

    def _check_boundaries(self):
        self.position.x = max(
            0, min(self.position.x, conf.WIDTH - self.rect.width))
        self.position.y = max(
            0, min(self.position.y, conf.HEIGHT - self.rect.height))

    def draw(self, surface):
        if conf.SHOWHITBOX:
            pygame.draw.rect(surface, conf.BLUE, self.rect)
        rotated_image = pygame.transform.rotate(
            self.image, -self.rotatingAngle)
        rotated_rect = rotated_image.get_rect(
            center=self.rect.center)

        surface.blit(rotated_image, rotated_rect)

    def shoot(self, projectileGroup: Group):
        if self.lastShot >= conf.PROJECTILE_COOLDOWN:
            direction = pygame.Vector2(0, -1).rotate(self.rotatingAngle)

            front_position = self.position + \
                direction * ((self.rect.height / 2) + 30)

            projectile = proy.Projectile(
                front_position, direction, self.rotatingAngle, proy.ProjectileType.BASIC)
            projectileGroup.add(projectile)

            self.lastShot = 0
