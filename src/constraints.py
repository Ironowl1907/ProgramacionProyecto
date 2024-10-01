import pygame
from random import randint
from pygame.sprite import Group
import player as player
import conf as conf
import enemy as enemy
from proyectile_system import ProjectileType


def checkCollisions(mainPlayer: player.Player, enemyGroup: Group,
                    projectileGroup: Group):
    # for i, enemy1 in enumerate(enemyGroup):
    #     for j, enemy2 in enumerate(enemyGroup):
    #         if i < j:  # Ensure each pair is only checked once
    #             if enemy1.rect.colliderect(enemy2.rect):
    pass

    for uenemy in enemyGroup:
        if mainPlayer.rect.colliderect(uenemy.rect) and \
                mainPlayer.invencibleTime <= 0 and not mainPlayer.inmortal:
            print("Game Over: Player crashed with enemy")
            exit()

    for projectile in projectileGroup:
        for uenemy in enemyGroup:
            if projectile.rect.colliderect(uenemy.rect) and \
                    projectile.projType != ProjectileType.BASICENEMY:
                if projectile.projType == ProjectileType.SAW:
                    uenemy.kill()
                    projectile.randDir()
                else:
                    uenemy.kill()
                    projectileGroup.remove(projectile)
            if projectile.rect.colliderect(mainPlayer.rect) and \
                    projectile.projType == ProjectileType.BASICENEMY and not\
                    mainPlayer.inmortal:
                print(f"Game Over: Player hit by projectile: {
                      int(projectile.projType)}")
                exit()


def spawnEnemy(enemyGroup: Group, projectileGroup: Group,
               mainPlayer: player.Player):
    newEnemy = enemy.Enemy(projectileGroup, 0, 0)
    position = pygame.Vector2(0, 0)  # More explicit initialization
    overlapping = True

    while overlapping:
        overlapping = False

        position.x = randint(0, conf.WIDTH - newEnemy.rect.width)
        position.y = randint(0, conf.HEIGHT - newEnemy.rect.height)

        newEnemy.position = position
        # Make sure the rect is updated
        newEnemy.rect.topleft = (position.x, position.y)

        for uenemy in enemyGroup:
            if newEnemy.rect.colliderect(uenemy.rect) or \
                    newEnemy.rect.colliderect(mainPlayer.rect):
                overlapping = True
                break

    enemyGroup.add(newEnemy)
