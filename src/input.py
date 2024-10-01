import pygame
from pygame.sprite import Group
import conf as conf
import player as player


def getInput(mplayer: player.Player, projectileGroup: Group, deltaTime: float):
    # Movement controls (WASD)
    keys = pygame.key.get_pressed()

    # Update velocity based on input and deltaTime
    if keys[pygame.K_a]:  # Move left (A)
        mplayer.velocity.x -= conf.PLAYER_ACELERATION * deltaTime
    if keys[pygame.K_d]:  # Move right (D)
        mplayer.velocity.x += conf.PLAYER_ACELERATION * deltaTime
    if keys[pygame.K_w]:  # Move up (W)
        mplayer.velocity.y -= conf.PLAYER_ACELERATION * deltaTime
    if keys[pygame.K_s]:  # Move down (S)
        mplayer.velocity.y += conf.PLAYER_ACELERATION * deltaTime
    if keys[pygame.K_SPACE]:
        mplayer.shoot(projectileGroup)
    if keys[pygame.K_RIGHT]:
        # Rotate right
        mplayer.rotatingAngle += int(conf.ROTATION_SPEED * deltaTime)
    if keys[pygame.K_LEFT]:
        # Rotate left
        mplayer.rotatingAngle -= int(conf.ROTATION_SPEED * deltaTime)
    if keys[pygame.K_UP]:
        # Rotate left
        mplayer.newWeapon()

    # Normalize the rotating angle
    if (mplayer.rotatingAngle >= 360):
        mplayer.rotatingAngle = 0

    # Limit velocity to conf.PLAYER_SPEED
    if mplayer.velocity.x > conf.PLAYER_SPEED:
        mplayer.velocity.x = conf.PLAYER_SPEED
    elif mplayer.velocity.x < -conf.PLAYER_SPEED:
        mplayer.velocity.x = -conf.PLAYER_SPEED

    if mplayer.velocity.y > conf.PLAYER_SPEED:
        mplayer.velocity.y = conf.PLAYER_SPEED
    elif mplayer.velocity.y < -conf.PLAYER_SPEED:
        mplayer.velocity.y = -conf.PLAYER_SPEED
