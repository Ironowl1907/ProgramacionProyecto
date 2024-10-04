import pygame
from pygame.math import Vector2

import conf


def draw_progress_bar(position: Vector2, state, surface):
    """
    Draws an inverse progress bar on the screen.

    :param position: Vector2 position of the progress bar
    :param state: A float between 0 and 1 representing the current state of the bar (1 = full, 0 = empty)
    :param surface: Where should the bar be placed
    """

    # Draw the background (empty part)
    pygame.draw.rect(surface, conf.BLACK,
                     (position.x - conf.KILLBARWIDTH/2, position.y, conf.KILLBARWIDTH, conf.KILLBARHEIGHT))

    # Draw the filled part based on the state (foreground)
    current_width = conf.KILLBARWIDTH * state
    pygame.draw.rect(surface, conf.GREY,
                     (position.x - conf.KILLBARWIDTH/2, position.y, current_width, conf.KILLBARHEIGHT))
