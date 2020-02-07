import pygame
from constants import *

INITIAL_X = 100
INITIAL_Y = 100

class SnakePart(pygame.sprite.Sprite):
    def __init__(self, img, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = rect
        self.store_previous_coord()

    def store_previous_coord(self):
        self.__prev_x__ = self.rect.x
        self.__prev_y__ = self.rect.y

    def get_previous_coord(self):
        return (self.__prev_x__, self.__prev_y__)

class Snake():
    def __init__(self, head_img, body_img, tail_img):
        self.__head_img__ = head_img
        self.__body_img__ = body_img
        self.__tail_img__ = tail_img
        rect = pygame.Rect(INITIAL_X, INITIAL_Y, SNAKE_PART_WIDTH, SNAKE_PART_HEIGHT)
        head = SnakePart(self.__head_img__, rect)
        self.__parts__ = [head]
        self.__direction__ = DOWN

    def set_direction(self, direction):
        self.__direction__ = direction

    @property
    def head(self):
        return self.__parts__[0]

    @property
    def is_out_of_bounds(self):
        cur_x = self.head.rect.x
        cur_y = self.head.rect.y
        return (cur_y >= screen_max_y) or (cur_y < 0) or (cur_x >= screen_max_x) or (cur_x < 0)

    def grow(self):
        does_have_tail = len(self.__parts__) > 1
        coordinates = self.head.get_previous_coord()
        rect = pygame.Rect(coordinates[0], coordinates[1], SNAKE_PART_WIDTH, SNAKE_PART_HEIGHT)
        new_part = SnakePart(self.__body_img__ if does_have_tail else self.__tail_img__, rect)
        self.__parts__.insert(1, new_part)
        return new_part

    def redraw_body(self):
        if len(self.__parts__) <= 1:
            return
        for i in range(1, len(self.__parts__)):
            coords = self.__parts__[i-1].get_previous_coord()
            self.__parts__[i].store_previous_coord()
            self.__parts__[i].rect.x = coords[0]
            self.__parts__[i].rect.y = coords[1]

    def move_head(self):
        self.head.store_previous_coord()
        if self.__direction__ == DOWN:
            self.head.rect.y += SNAKE_PART_HEIGHT
        if self.__direction__ == UP:
            self.head.rect.y -= SNAKE_PART_HEIGHT
        if self.__direction__ == LEFT:
            self.head.rect.x -= SNAKE_PART_WIDTH
        if self.__direction__ == RIGHT:
            self.head.rect.x += SNAKE_PART_WIDTH

    @property
    def is_eating_self(self):
        if (len(self.__parts__) <= 1):
            return False
        for body_part in self.__parts__[1:]:
            if pygame.sprite.collide_rect(self.head, body_part):
                return True
        return False
