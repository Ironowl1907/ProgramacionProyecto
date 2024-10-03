import pygame
from pygame.math import Vector2
from pygame.surface import Surface
from pygame.transform import scale

from player import Player
from proyectile_system import ProjectileType
import conf as conf


class Ui:
    def __init__(self, position: pygame.Vector2, mainPlayer: Player) -> None:
        self.position = position
        self.player = mainPlayer

        self.sawIcon = pygame.image.load(
            "../res/Player/Player_Items/Player_Saw_Item.png")
        self.sawIcon = scale(self.sawIcon, (50, 50))
        self.basicIcon = pygame.image.load(
            "../res/Player/Player_Items/Player_Bullet_Item.png")
        self.basicIcon = scale(self.basicIcon, (50, 50))
        self.laserIcon = pygame.image.load(
            "../res/Player/Player_Items/Player_Laser_Item.png")
        self.laserIcon = scale(self.laserIcon, (50, 50))
        self.noImg = pygame.image.load("../res/ui/no_weapon.png")
        self.noImg = scale(self.noImg, (50, 50))

    def _drawSelectedWeapon(self, position: Vector2, type: int, surface: Surface):
        selected = self.basicIcon
        match type:
            case ProjectileType.BASIC:
                selected = self.basicIcon
            case ProjectileType.LASER:
                selected = self.laserIcon
            case ProjectileType.SAW:
                selected = self.sawIcon
            case _:
                selected = self.noImg
        surface.blit(selected, (position.x, position.y))

    def _drawRemainingLive(self, position: Vector2, surface: Surface):
        pass

    def _drawKilledEnemies(self, position: Vector2, surface: Surface):
        pass

    def draw(self, surface: pygame.Surface):
        selected_weapon_type = self.player.actualWeapon
        self._drawSelectedWeapon(
            Vector2(self.position.x / 8, self.position.y), selected_weapon_type, surface)
