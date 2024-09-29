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
        if mainPlayer.rect.colliderect(uenemy.rect):
            print("Game Over")
            exit()

    for projectile in projectileGroup:
        for uenemy in enemyGroup:
            if projectile.rect.colliderect(uenemy.rect):
                print("Enemy killed")
                enemyGroup.remove(uenemy)


def spawnEnemy(enemyGroup: Group, projectileGroup: Group, mainPlayer: player.Player):
    newEnemy = enemy.Enemy(projectileGroup, 0, 0)
    position = pygame.Vector2(0)
    overlappping = True
    while overlappping:
        overlappping = False
        position.x = randint(0, conf.WIDTH)
        position.y = randint(0, conf.HEIGHT)
        newEnemy.position = position
        for uememy in enemyGroup:
            if newEnemy.rect.colliderect(uememy) or newEnemy.rect.colliderect(mainPlayer.rect):
                overlappping = True
                break
        enemyGroup.add(newEnemy)
