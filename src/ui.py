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

        self.sawIcon = self._load_and_scale_image(
            "../res/Player/Player_Items/Player_Saw_Item.png", (50, 50))
        self.basicIcon = self._load_and_scale_image(
            "../res/Player/Player_Items/Player_Bullet_Item.png", (50, 50))
        self.laserIcon = self._load_and_scale_image(
            "../res/Player/Player_Items/Player_Laser_Item.png", (50, 50))
        self.noImg = self._load_and_scale_image(
            "../res/ui/no_weapon.png", (50, 50))

    def _load_and_scale_image(self, path: str, size: tuple[int, int]) -> pygame.Surface:
        try:
            img = pygame.image.load(path)
            return scale(img, size)
        except pygame.error as e:
            print(f"Error loading image at {path}: {e}")
            return pygame.Surface(size)  # Return empty surface on failure

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
        font = pygame.font.SysFont(None, 40)
        score_text = font.render(
            f"Score: {self.player.killedEnemies}", True, (255, 255, 255))
        surface.blit(score_text, (position.x, position.y))

    def draw(self, surface: pygame.Surface):
        selected_weapon_type = self.player.actualWeapon
        self._drawSelectedWeapon(
            Vector2(self.position.x / 8, self.position.y), selected_weapon_type, surface)
        self._drawKilledEnemies(
            Vector2(self.position.x + self.position.x/8, self.position.y), surface)
