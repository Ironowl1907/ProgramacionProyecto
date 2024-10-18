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
            conf.RUNNING = False

    # Projectile collisions
    for projectile in projectile_group:
        if projectile.projType == ProjectileType.BASICENEMY and not main_player.inmortal:
            if projectile.rect.colliderect(main_player.rect):
                print(f"Game Over: Player hit by projectile: {
                      int(projectile.projType)}")
                conf.RUNNING = False

        for current_enemy in enemy_group:
            if projectile.projType == ProjectileType.BASICENEMY:
                continue
            if not projectile.rect.colliderect(current_enemy.rect):
                continue

            if projectile.projType == ProjectileType.SAW:
                current_enemy.kill()  # Marca al enemigo como destruido
                projectile_group.remove(projectile)  # Elimina el proyectil
            elif projectile.projType == ProjectileType.NET:
                if current_enemy.killed:  # Solo si el enemigo ya fue destruido
                    main_player.killedEnemies += 1
                    projectile_group.remove(projectile)  # Elimina la red
                    enemy_group.remove(current_enemy)  # Elimina el enemigo
                else:
                    # Si el enemigo no estaba destruido, se podría hacer otra acción o ignorar
                    continue
            else:
                projectile_group.remove(projectile)  # Elimina el proyectil
                current_enemy.kill()  # Marca al enemigo como destruido


def spawnEnemy(enemy_group: Group, projectile_group: Group):
    new_enemy = enemy.Enemy(projectile_group, int(
        rand.random() * conf.WIDTH), -100)
    enemy_group.add(new_enemy)
