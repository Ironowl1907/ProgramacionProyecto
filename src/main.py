import pygame
import constraints as constr
import enemy as enemy
import conf as conf
from enemy import Enemy
import input as input
import player as player
import ui as ui

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((conf.WIDTH, conf.HEIGHT))
pygame.display.set_caption("Avion de basura (que se yo)")
background = pygame.image.load("../res/Background.png")


def mainGame():

    # Initialize pygame
    pygame.init()

    # Create a window
    screen = pygame.display.set_mode((conf.WIDTH, conf.HEIGHT))
    pygame.display.set_caption("Avion de basura (que se yo)")
    background = pygame.image.load("../res/Background.png")

    pygame.mixer.init()
    pygame.mixer.music.load("../res/music.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play()

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
    spawnTimeCounter = 0
    waveNumber = 0
    baseEnemyCount = 2
    spawnInterval = 10

    # Main game loop
    clock = pygame.time.Clock()
    running = True

    print("Entered while")

    while running:
        deltaTime = clock.tick(conf.FPS) / 1000
        if len(enemiesGroup) == 0:
            if mainUi.showingTip == False:
                mainUi.newTip()
            spawnTimeCounter += deltaTime
            mainUi.showingTip = True
        else:
            mainUi.showingTip = False

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # Handle Input
        input.getInput(mainPlayer, projectilesGroup, deltaTime)

        # Check if it's time to spawn a new wave of enemies
        if spawnTimeCounter >= spawnInterval * waveNumber:
            waveNumber += 1

            # Calculate number of enemies for this wave
            additionalEnemies = int(
                (spawnTimeCounter / 60) + (mainPlayer.killedEnemies / 5))
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


# if __name__ == "__main__":
#     mainGame()
