import pygame, random, time, winsound
from pygame import display
from pygame import font
from pygame.locals import *

 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [dis_y/2, dis_x/2])


def on_grip_random():
    x = random.randint(10, 790)
    y = random.randint(10, 590)
    return(x//10 * 10, y//10 * 10)


def collision(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

dis_x = 800
dis_y = 600

pygame.init()
screen = pygame.display.set_mode((dis_x, dis_y))
pygame.display.set_caption('Snake, Contador: 0')

font_style = pygame.font.SysFont(None, 50)

snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255,255,255))
snake = [(200, 200), (210, 200), (220, 200)]

apple_pos = on_grip_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = RIGHT

game_over = False

clock = pygame.time.Clock()

cont = int(3)
while not game_over:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if my_direction == UP:
                if event.key == K_a or event.key == K_LEFT:
                    my_direction = LEFT
                if event.key == K_d or event.key == K_RIGHT:
                    my_direction = RIGHT
            if my_direction == DOWN:
                if event.key == K_a or event.key == K_LEFT:
                    my_direction = LEFT
                if event.key == K_d or event.key == K_RIGHT:
                    my_direction = RIGHT
            if my_direction == RIGHT:
                if event.key == K_w or event.key == K_UP:
                    my_direction = UP
                if event.key == K_s or event.key == K_DOWN:
                    my_direction = DOWN
            if my_direction == LEFT:
                if event.key == K_w or event.key == K_UP:
                    my_direction = UP
                if event.key == K_s or event.key == K_DOWN:
                    my_direction = DOWN


    if collision(snake[0], apple_pos):
        apple_pos = on_grip_random()
        snake.append((0,0))
        cont += 1
        pygame.display.set_caption(f'Snake, Contador: {cont - 3}')
        winsound.Beep(2000,10)
        

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    if snake[0][0] >= dis_x or snake[0][0] < 0 or snake[0][1] >= dis_y or snake[0][1] < 0:
        game_over = True
    
    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)
    pygame.display.update()

message("Game Over",(255,255,255))
pygame.display.update()
time.sleep(1)
pygame.quit()