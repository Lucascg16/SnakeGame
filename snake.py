import pygame, random, time, winsound
from pygame import display
from pygame import font
from pygame.locals import *

#Função para gerar a mensagem na tela
def message(msg, color, position):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, position)

#Transformando o grid 10x10 em padrão
def on_grip_random():
    x = random.randint(10, 790)
    y = random.randint(10, 590)
    return(x//10 * 10, y//10 * 10)

#Função que verifica colisão
def collision(c1, c2):
    return (c1[0] == c2[0] and c1[1] == c2[1])

#Fazendo a tradução de das direções
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

#Gerando uma posição aleatoria para a cobra nascer
snake_init_posx = random.randint(110,690)//10 * 10
snake_init_posy = random.randint(110,490)//10 * 10

#Criando a cobra
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((0,255,0))
snake = [(snake_init_posx, snake_init_posy), (snake_init_posx + 10, snake_init_posy), (snake_init_posx + 20, snake_init_posy)]

#Criando a maçã
apple_pos = on_grip_random()
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

#Direção que o jogo vai começar
my_direction = random.randint(0, 3)

#Clock usado para limitar a velocidade da cobra
clock = pygame.time.Clock()

#Contador de pontuação
cont = int(0)

game_over = False
while not game_over:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        #Verificação de movimento da cobra
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

    #Verificando a colisão da cobra com a maçã
    if collision(snake[0], apple_pos):
        apple_pos = on_grip_random()
        snake.append((0,0))
        cont += 1
        pygame.display.set_caption(f'Snake, Contador: {cont}')
        winsound.Beep(2000,10)
        

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    #Movimento que a cobra faz baseado na direção atual
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    #Verificando a colisão da cobra com as bordas 
    if snake[0][0] >= dis_x or snake[0][0] < 0 or snake[0][1] >= dis_y or snake[0][1] < 0:
        game_over = True
    
    #Verificando a colisão da cobra com ela mesma 
    for i in range(3, len(snake)):
        if snake[0] == snake[i]:
            game_over = True

    screen.fill((0,0,0))
    screen.blit(apple, apple_pos)

    for pos in snake:
        screen.blit(snake_skin, pos)
    pygame.display.update()

pontuação = str(cont)
message("Game Over",(255,255,255), [dis_y/2, dis_x/2])
message("pontuação: " + pontuação,(255,255,255), [dis_y/2.1, dis_x/1.8])
pygame.display.update()
time.sleep(1)
pygame.quit()