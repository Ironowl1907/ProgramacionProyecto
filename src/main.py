import pygame
import constraints as constr
import enemy as enemy
import conf as conf
from enemy import Enemy
import input as input
import sys
import player as player

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

    constr.spawnEnemy(enemiesGroup, projectilesGroup, mainPlayer)

    # Main game loop
    clock = pygame.time.Clock()
    running = True

    while running:
        deltaTime = clock.tick(conf.FPS) / 1000
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Handle Input
        input.getInput(mainPlayer, projectilesGroup, deltaTime)

        # Update
        for projectile in projectilesGroup:
            projectile.update()
        for uenemy in enemiesGroup:
            uenemy.update(deltaTime, mainPlayer.position, enemiesGroup)
        mainPlayer.update(deltaTime)

        constr.checkCollisions(mainPlayer, enemiesGroup, projectilesGroup)

        # Render
        screen.blit(background, (0, 0))
        mainPlayer.draw(screen)
        for uenemy in enemiesGroup:
            uenemy.draw(screen)
        for projectile in projectilesGroup:
            projectile.draw(screen)

        # Update the display
        pygame.display.flip()


if __name__ == "__main__":
    mainGame()
