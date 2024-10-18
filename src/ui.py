import pygame
from pygame.math import Vector2
from pygame.surface import Surface
from pygame.transform import scale
from DRAFTS import DRAFT_TIP as tips
from player import Player
from proyectile_system import ProjectileType


class Ui:
    def __init__(self, position: pygame.Vector2, mainPlayer: Player) -> None:
        self.position = position
        self.player = mainPlayer

        self.sawIcon = self._load_and_scale_image(
            "../res/Player/Player_Items/Player_Saw_Item.png", (50, 50))
        self.basicIcon = self._load_and_scale_image(
            "../res/Player/Player_Items/Player_Bullet_Item.png", (50, 50))
        self.netIcon = self._load_and_scale_image(
            "../res/Player/Player_Items/Player_Web_Item.png", (50, 50))
        # self.laserIcon = self._load_and_scale_image(
        #     "../res/Player/Player_Items/Player_Laser_Item.png", (50, 50))
        self.noImg = self._load_and_scale_image(
            "../res/ui/no_weapon.png", (50, 50))

        # Trash_coin Sprite
        self.trash_coin = self._load_and_scale_image(
            "../res/ui/Trash_coin.png", (25, 25))

        self.lastTip = 0
        self.showingTip = True

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
            case ProjectileType.SAW:
                selected = self.sawIcon
            # case ProjectileType.LASER:
            #     selected = self.laserIcon
            case ProjectileType.NET:
                selected = self.netIcon
            case _:
                selected = self.noImg
        surface.blit(selected, (position.x, position.y))

    def _drawNewTip(self, position: Vector2, surface: Surface):
        font = pygame.font.Font(r"../res/Fonts/Minecraftia-Regular.ttf", 18)
        score_text = font.render(
            f"{tips.tips[self.lastTip]}", True, (153, 229, 80))
        surface.blit(score_text, (position.x -
                     score_text.get_width()//2, position.y))

    def newTip(self):
        self.lastTip = self.lastTip % (len(tips.tips)-1) + 1

    def _drawKilledEnemies(self, position: Vector2, surface: Surface):
        font = pygame.font.Font(r"../res/Fonts/Minecraftia-Regular.ttf", 20)
        score_text = font.render(
            f"Scraps: {self.player.killedEnemies}", True, (255, 215, 0))
        surface.blit(score_text, (position.x, position.y))

        coin_position_x = position.x + score_text.get_width() - 150
        surface.blit(self.trash_coin, (coin_position_x, position.y))

    def draw(self, surface: pygame.Surface):
        selected_weapon_type = self.player.actualWeapon
        if not self.showingTip:
            self._drawSelectedWeapon(
                Vector2(self.position.x / 8, self.position.y), selected_weapon_type, surface)
            self._drawKilledEnemies(
                Vector2(self.position.x + self.position.x * 2/3, self.position.y), surface)
        else:
            self._drawNewTip(
                Vector2(self.position.x, self.position.y), surface)
