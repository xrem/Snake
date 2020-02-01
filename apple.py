import pygame

class Apple(pygame.sprite.Sprite):
    def __init__(self, apple_img, apple_rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = apple_img
        self.rect = apple_rect