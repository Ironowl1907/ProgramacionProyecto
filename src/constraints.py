from random import randint, random
import pygame
from pygame.sprite import Group
import player as player
import conf as conf
import enemy as enemy


def checkCollisions(mainPlayer: player.Player, enemyGroup: Group, projectileGroup: Group):
    for i, enemy1 in enumerate(enemyGroup):
        for j, enemy2 in enumerate(enemyGroup):
            if i < j:  # Ensure each pair is only checked once
                if enemy1.rect.colliderect(enemy2.rect):
                    print("Collision")

    for uenemy in enemyGroup:
        if mainPlayer.rect.colliderect(uenemy.rect) and mainPlayer.invencibleTime <= 0:
            print("Game Over")
            exit()

    for projectile in projectileGroup:
        for uenemy in enemyGroup:
            if projectile.rect.colliderect(uenemy.rect):
                print("Enemy killed")
                enemyGroup.remove(uenemy)
                projectileGroup.remove(projectile)


def spawnEnemy(enemyGroup: Group, projectileGroup: Group, mainPlayer: player.Player):
    newEnemy = enemy.Enemy(projectileGroup, 0, 0)
    position = pygame.Vector2(0, 0)  # More explicit initialization
    overlapping = True

    while overlapping:
        print("Checking new coord")
        overlapping = False

        position.x = randint(0, conf.WIDTH - newEnemy.rect.width)
        position.y = randint(0, conf.HEIGHT - newEnemy.rect.height)

        newEnemy.position = position
        # Make sure the rect is updated
        newEnemy.rect.topleft = (position.x, position.y)

        for uenemy in enemyGroup:
            if newEnemy.rect.colliderect(uenemy.rect) or newEnemy.rect.colliderect(mainPlayer.rect):
                overlapping = True
                print(f"Failed {position}")
                break

    print(f"Enemy added: {newEnemy.position}")
    enemyGroup.add(newEnemy)
