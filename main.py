import os
import pygame

from Snake import Snake
from apple import Apple
from constants import *

base_path = os.path.dirname(__file__)
head_path = os.path.join(base_path, "head.png")
body_path = os.path.join(base_path, "body.png")
tail_path = os.path.join(base_path, "tail.png")
apple_path = os.path.join(base_path, "apple.png")

pygame.init()

scene = pygame.display.set_mode(settings)
CLOCK = pygame.time.Clock()

head_img = pygame.image.load(head_path).convert()
body_img = pygame.image.load(body_path).convert()
tail_img = pygame.image.load(tail_path).convert()
apple_img = pygame.image.load(apple_path).convert()

apple = Apple(apple_img)
snake = Snake(head_img, body_img, tail_img)
allSprites = pygame.sprite.Group()
allSprites.add(snake.head)
allSprites.add(apple)

Running = True
score = 0


def process():
    global score
    global Running

    if snake.is_out_of_bounds or snake.is_eating_self:
        Running = False

    snake.move_head()

    if (pygame.sprite.collide_rect(snake.head, apple)):
        allSprites.add(snake.grow())
        score += 1
        apple.newRandomPos()
    else:
        snake.redraw_body()


while Running:
    events = pygame.event.get()
    for ev in events:
        if ev.type == pygame.QUIT:
            Running = False

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_LEFT or ev.unicode == 'a':
                snake.set_direction(LEFT)
            if ev.key == pygame.K_RIGHT or ev.unicode == 'd':
                snake.set_direction(RIGHT)
            if ev.key == pygame.K_UP or ev.unicode == 'w':
                snake.set_direction(UP)
            if ev.key == pygame.K_DOWN or ev.unicode == 's':
                snake.set_direction(DOWN)

    CLOCK.tick(FPS + score)
    scene.fill((BLACK[0] + (score * 6), BLACK[1] + (score * 3), BLACK[2] + (score * 3)))
    process()
    allSprites.update()
    allSprites.draw(scene)
    pygame.display.flip()

pygame.quit()
print('Score: ' + str(score))