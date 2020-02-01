import pygame

class SnakePart(pygame.sprite.Sprite):
    def __init__(self, img, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = rect

class Snake():
    def __init__(self, head_img, body_img, tail_img):
        self.__head_img__ = head_img
        self.__body_img__ = body_img
        self.__tail_img__ = tail_img
        rect = pygame.Rect(100, 100, 10, 10)
        head = SnakePart(self.__head_img__, rect)
        self.__parts__ = [head]

    def get_head_rect(self):
        return self.__parts__[0].rect



