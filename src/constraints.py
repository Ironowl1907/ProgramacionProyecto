import pygame
import random as rand
from pygame.sprite import Group
import player
import conf
import enemy
from proyectile_system import ProjectileType


def checkCollisions(main_player: player.Player, enemy_group: Group, projectile_group: Group):
    # Player-enemy collisions
    for current_enemy in enemy_group:
        if main_player.invencibleTime > 0 or main_player.inmortal:
            continue
        if main_player.rect.colliderect(current_enemy.rect):
            print("Game Over: Player crashed with enemy")
            exit()

    # Projectile collisions
    for projectile in projectile_group:
        if projectile.projType == ProjectileType.BASICENEMY and not main_player.inmortal:
            if projectile.rect.colliderect(main_player.rect):
                print(f"Game Over: Player hit by projectile: {
                      int(projectile.projType)}")
                exit()

        for current_enemy in enemy_group:
            if projectile.projType == ProjectileType.BASICENEMY:
                continue
            if not projectile.rect.colliderect(current_enemy.rect):
                continue

            if projectile.projType == ProjectileType.SAW:
                current_enemy.kill()
                projectile.randDir()
            elif projectile.projType == ProjectileType.NET and current_enemy.killed:
                main_player.killedEnemies += 1
                projectile_group.remove(projectile)
                enemy_group.remove(current_enemy)

            else:
                projectile_group.remove(projectile)
                current_enemy.kill()


def spawnEnemy(enemy_group: Group, projectile_group: Group):
    new_enemy = enemy.Enemy(projectile_group, int(
        rand.random() * conf.WIDTH), -100)
    enemy_group.add(new_enemy)
