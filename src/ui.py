import pygame
from pygame.math import Vector2
from pygame.surface import Surface

from player import Player
from proyectile_system import ProjectileType


class Ui:
    def __init__(self, position: pygame.Vector2, mainPlayer: Player) -> None:
        self.position = position
        self.player = mainPlayer

        # self.sawIcon = pygame.image.load("../res/Player_saw_item.png")
        self.basicIcon = pygame.image.load(
            "../res/Player/Player_Items/Player_Bullet.png")
        self.laserIcon = pygame.image.load(
            "../res/Player/Player_Items/Player_Laser.png")

    def _drawSelectedWeapon(self, position: Vector2, type: int, surface: Surface):
        surface.blit(self.basicIcon, (position.x, position.y))

    def _drawRemainingLive(self, position: Vector2, surface: Surface):
        pass

    def _drawKilledEnemies(self, position: Vector2, surface: Surface):
        pass

    def draw(self, surface: pygame.Surface):
        self._drawSelectedWeapon(self.position, ProjectileType.BASIC, surface)
