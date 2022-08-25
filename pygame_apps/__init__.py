import pygame

# from pygame import *

import sys, pygame

# creezi aplicatia pygame
from pygame.time import Clock

x: int
y: int
pygame.init()
size = width, height = 320, 240
speed = [15, 15]
COLOR_BLACK = 0, 0, 0  # RGB colors :)
COLOR_WHITE = 255, 255, 255
semi_transparent_black = 0, 0, 0, 122  # RGBA    Red Green Blue Alpha     Alpha=opacity   transparenta   de la 0 la 2**8 - 1    255

screen = pygame.display.set_mode(size, )  # e necesar ca sa creeze o fereastra

ball = pygame.image.load("intro_ball.gif").convert_alpha()  # in unele versiuni/cazuri, e nevoie de convert_alpha pt ca nu adauga si canalul alpha in mod automat
angle = 0

# game loop-ul aplicatiei, adica ce scriem in while se executa la fiecare frame in parte
# de aceea, crem un clock care va fi folosit pentru limitarea la un anumit numar de cadre pe secunda
fps = 10
clock = Clock()

# Todo Tema: poti folosi ball_resized_and_rotated.get_rect() ca sa gasesti pozitia mingii, si sa te folosesti de asta pentru a o pozitiona in centrul ecranului

ball_resized = pygame.Surface((50, 50), flags=pygame.SRCALPHA)
pygame.transform.scale(ball, (50, 50), ball_resized)
ball_resized_and_rotated = pygame.transform.rotate(ball_resized, angle)


ball_rect = ball_resized_and_rotated.get_rect()  # .x, .y, .width, .height
ball_rect.width, ball_rect.height
width, height  # latimea si inaltimea ecranului
y = height/2 - ball_rect.height / 2
x = width / 2 - ball_rect.width / 2

while True:
    dtime = clock.tick(fps) / 1000

    print('One more second')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # eveniment la apasarea unei taste
            keys = pygame.key.get_pressed()
            print(keys)
            if keys[pygame.K_ESCAPE]:
                sys.exit()



    angle += 180 * dtime

    screen.fill(COLOR_WHITE)



    # TODO Observatie?
    #  ecranul numara x-ul de la stanga la dreapta, iar y-ul de sus in jos.

    ball_width, ball_height =ball_resized_and_rotated.get_width(), ball_resized_and_rotated.get_height()
    screen.blit(ball_resized_and_rotated, pygame.rect.Rect((x,y, ball_width, ball_height)))
    # TODO ce inseamna blit? Transfer de blocuri de biti.
    #  e un sir de byti, grupati cate 4 sau 3, sau 1 pt black-white screens
    #  ball va fi locul de unde transferi, iar ballrect sectiunea din ball de unde transferi


    pygame.display.flip()

