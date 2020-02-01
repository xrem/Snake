import os
import pygame
from random import randint

from Snake import SnakePart, Snake
from apple import Apple

base_path = os.path.dirname(__file__)
head_path = os.path.join(base_path, "head.png")
body_path = os.path.join(base_path, "body.png")
tail_path = os.path.join(base_path, "tail.png")
apple_path = os.path.join(base_path, "apple.png")


pygame.init()

settings = (900, 500)
scene = pygame.display.set_mode(settings)
FPS = 20
CLOCK = pygame.time.Clock()


head_img = pygame.image.load(head_path).convert()
body_img = pygame.image.load(body_path).convert()
tail_img = pygame.image.load(tail_path).convert()
apple_img = pygame.image.load(apple_path).convert()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
ANOTHER_YELLOW = (230, 230, 5)
GREEN = (0, 255, 0)
LIGHTBLUE = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

apple = pygame.Rect(randint(3,87)*10, randint(3,47)*10, 10, 10)
new_snake = Snake(head_img, body_img, tail_img)
snake = [new_snake.get_head_rect()]
snakeHead = snake[0]


RAINBOW = [RED, ORANGE, ANOTHER_YELLOW, GREEN, LIGHTBLUE, BLUE, PURPLE]

dir = DOWN

def move_rect():

    global dir

    cur_y = snakeHead.y
    cur_x = snakeHead.x

    if (cur_y >= settings[1] - snakeHead.height) or (cur_y <= 0) or (cur_x >= settings[0] - snakeHead.width) or (cur_x <= 0):
        pygame.quit()
    if dir == DOWN:
        cur_y += 10
    if dir == UP:
        cur_y -= 10
    if dir == LEFT:
        cur_x -= 10
    if dir == RIGHT:
        cur_x += 10

    prev_x = snakeHead.x
    prev_y = snakeHead.y
    snakeHead.y = cur_y
    snakeHead.x = cur_x
    headSprite = SnakePart(head_img, snakeHead)
    pygame.draw.rect(scene, BLACK, snakeHead)
    scene.blit(head_img, snakeHead)
    headSprite.update()

    if len(snake)>1:
        isTail = True
        for j in range(len(snake)-1, 0, -1):
            if (j == 1):
                snake[j].y = prev_y
                snake[j].x = prev_x
            else:
                snake[j].y = snake[j-1].y
                snake[j].x = snake[j-1].x
            pygame.draw.rect(scene, BLACK, snake[j])
            if (isTail == True):
                scene.blit(tail_img, snake[j])
                isTail = False
            else:
                scene.blit(body_img, snake[j])

    appleSprite = Apple(apple_img, apple)

    #if (snakeHead.x == apple.x and snakeHead.y == apple.y):
    if (pygame.sprite.collide_rect(headSprite, appleSprite)):
        snake.append(pygame.Rect(prev_x, prev_y, 10, 10))
        apple.x = randint(3, 87) * 10
        apple.y = randint(3, 47) * 10

    pygame.draw.rect(scene, BLACK, apple)
    scene.blit(apple_img, apple)
    appleSprite.update()

    pygame.display.update()


Running = True
while Running:
    events = pygame.event.get()
    for ev in events:
        if ev.type == pygame.QUIT:
            Running = False
            print('You lose')

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT or ev.unicode == 'a':
                dir = LEFT
            if ev.key == pygame.K_RIGHT or ev.unicode == 'd':
                dir = RIGHT
            if ev.key == pygame.K_UP or ev.unicode == 'w':
                dir = UP
            if ev.key == pygame.K_DOWN or ev.unicode == 's':
                dir = DOWN

    CLOCK.tick(FPS)
    scene.fill(BLACK)
    move_rect()
pygame.quit()