import pygame
import sys

from pygame.surface import Surface


class Button():
    def __init__(self, image, x_pos: int, y_pos: int, text_input: str,
                 screen: Surface):
        self.font = pygame.font.SysFont("cambria", 50)
        self.screen = screen
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("Button Press!")

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, "green")
        else:
            self.text = self.font.render(self.text_input, True, "white")


button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))

# button = Button(button_surface, 400, 300, "Button")

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             button.checkForInput(pygame.mouse.get_pos())
#
#     screen.fill("white")
#
#     button.update()
#     button.changeColor(pygame.mouse.get_pos())
#
#     pygame.display.update()
