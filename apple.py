import pygame
from random import randint
from constants import *

APPLE_WIDTH = SNAKE_PART_WIDTH
APPLE_HEIGHT = SNAKE_PART_HEIGHT
safe_margin = 3
max_x = screen_max_x // APPLE_WIDTH - safe_margin
max_y = screen_max_y // APPLE_WIDTH - safe_margin

class Apple(pygame.sprite.Sprite):
    def __init__(self, apple_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = apple_img
        self.rect = pygame.Rect(0, 0, APPLE_WIDTH, APPLE_HEIGHT)
        self.newRandomPos()

    def newRandomPos(self):
        self.rect.x = randint(safe_margin, max_x) * 10
        self.rect.y = randint(safe_margin, max_y) * 10