import pygame
import constraints as constr
import enemy as enemy
import conf as conf
from enemy import Enemy
import input as input
import sys
import player as player
import ui as ui

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((conf.WIDTH, conf.HEIGHT))
pygame.display.set_caption("Avion de basura (que se yo)")
background = pygame.image.load("../res/Background.png")


def mainGame():
    # Proyectile list instance
    projectilesGroup = pygame.sprite.Group()

    # Enemy list instance
    enemiesGroup = pygame.sprite.Group()

    # Player instance
    mainPlayer = player.Player(
        int(conf.WIDTH/2), int(conf.HEIGHT/2), projectilesGroup)

    mainUi = ui.Ui(pygame.Vector2(
        conf.WIDTH/2, conf.HEIGHT * conf.UIPOSITION), mainPlayer)

    # Game timing and difficulty variables
    timePlayed = 0
    waveNumber = 0
    baseEnemyCount = 2
    spawnInterval = 10

    # Main game loop
    clock = pygame.time.Clock()
    running = True

    while running:
        deltaTime = clock.tick(conf.FPS) / 1000
        timePlayed += deltaTime

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle Input
        input.getInput(mainPlayer, projectilesGroup, deltaTime)

        # Check if it's time to spawn a new wave of enemies
        if timePlayed >= spawnInterval * waveNumber:
            waveNumber += 1

            # Calculate number of enemies for this wave
            additionalEnemies = int(
                (timePlayed / 60) + (mainPlayer.killedEnemies / 5))
            enemiesInWave = baseEnemyCount + additionalEnemies

            # Spawn enemies for this wave
            for _ in range(enemiesInWave):
                constr.spawnEnemy(enemiesGroup, projectilesGroup)

        # Update game objects
        for projectile in projectilesGroup:
            projectile.update()
        for uenemy in enemiesGroup:
            uenemy.update(deltaTime, mainPlayer.position, enemiesGroup)
        mainPlayer.update(deltaTime)

        # Check for collisions
        constr.checkCollisions(mainPlayer, enemiesGroup, projectilesGroup)

        # Render the game
        screen.blit(background, (0, 0))
        mainPlayer.draw(screen)
        for uenemy in enemiesGroup:
            uenemy.draw(screen)
        for projectile in projectilesGroup:
            projectile.draw(screen)

        mainUi.draw(screen)

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    mainGame()
