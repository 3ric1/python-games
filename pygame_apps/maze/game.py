import datetime
import time

import pygame

# from pygame import *

import sys, pygame

# creezi aplicatia pygame
from pygame.time import Clock

# import colors
from colors import *
from pygame_apps.maze.actor import Actor
from pygame_apps.maze.sprite_animation import SpriteAnimation

pygame.init()
screen_size = screen_width, screen_height = 400, 400

# folosim pygame.SRCALPHA ca in pixelii ecranului sa existe si un canal ALPHA cu transparenta fiecare pixel
screen = pygame.display.set_mode(screen_size, pygame.SRCALPHA)  # e necesar ca sa creeze o fereastra

texture_wood = pygame.image.load(
    "assets/128x128/Wood/Wood_14-128x128.png").convert_alpha()  # in unele versiuni/cazuri, e nevoie de convert_alpha pt ca nu adauga si canalul alpha in mod automat

# game loop-ul aplicatiei, adica ce scriem in while se executa la fiecare frame in parte
# de aceea, crem un clock care va fi folosit pentru limitarea la un anumit numar de cadre pe secunda
fps = 10
clock = Clock()

# Todo Tema: poti folosi ball_resized_and_rotated.get_rect() ca sa gasesti pozitia mingii, si sa te folosesti de asta pentru a o pozitiona in centrul ecranului

# cream texture de  50 pe 50
text_grass_128 = pygame.image.load("assets/128x128/Grass/Grass_24-128x128.png").convert_alpha()
text_gras_50 = pygame.transform.scale(text_grass_128, (50, 50))
text_wood_128 = pygame.image.load("assets/128x128/Wood/Wood_14-128x128.png").convert_alpha()
text_wood_50 = pygame.transform.scale(text_wood_128, (50, 50))


def create_bg_texture() -> pygame.Surface:
    text = pygame.surface.Surface((400, 400), flags=pygame.SRCALPHA)

    for i in range(8):
        for j in range(8):
            # if i % 2 == 1 and j % 2 == 1:
            #     screen.blit(text_gras_50, pygame.rect.Rect(i * 50, j * 50, 0, 0))
            # elif i % 2 == 0 and j % 2 == 0:
            #     screen.blit(text_gras_50, pygame.rect.Rect(i * 50, j * 50, 0, 0))
            if (i + j) % 2 == 0:
                text.blit(text_gras_50, pygame.rect.Rect(i * 50, j * 50, 0, 0))
            else:
                text.blit(text_wood_50, pygame.rect.Rect(i * 50, j * 50, 0, 0))
    return text


def event_handle_quit(event):
    if event.type == pygame.QUIT:
        sys.exit()
    if event.type == pygame.KEYDOWN:
        # eveniment la apasarea unei taste
        keys = pygame.key.get_pressed()
        print(keys)
        if keys[pygame.K_ESCAPE]:
            sys.exit()


text_bg_tiled = create_bg_texture()




# dog_sprite = pygame.image.load('128x128/Dog_medium.png')
# dog_animation = SpriteAnimation(dog_sprite, (60, 38), [
#     'Bark',  # each row has a different animation
#     'Walk',
#     'Run',
#     'Sit Transition',
#     'Idle Sit',
#     'Idle Stand', ], {
#                                     'Bark': 4,
#                                     'Walk': 6,
#                                     'Run': 5,
#                                     'Sit Transition': 3,
#                                     'Idle Sit': 4,
#                                     'Idle Stand': 4,
#                                 })
# dog = Actor(dog_animation, 'Walk')
# dog.set_state("Run")
#

bird_sprite = pygame.image.load('assets/BirdSprite.png')
bird_animation = SpriteAnimation(bird_sprite, (16, 16), [
    'Idle',
    'Fly',
    'Eating',
], {
     'Idle': 2,
     'Fly': 8,
     'Eating': 3
 })
bird = Actor(bird_animation, 'Fly')
bird.set_state('Fly')

# load the ui icons sprite
ui_sprite = pygame.image.load('assets/ui_icons.png')
ui_sprite = Sprite(ui_sprite, )

while True:
    dtime = clock.tick(fps) / 1000

    for event in pygame.event.get():
        event_handle_quit(event)

    screen.fill(COLOR_WHITE)


    bird1 = bird_animation.at('Fly', 0)
    bird2 = bird_animation.at('Fly', 1)
    bird3 = bird_animation.at('Fly', 2)
    bird4 = bird_animation.at('Fly', 3)
    bird5 = bird_animation.at('Fly', 4)
    bird6 = bird_animation.at('Fly', 5)
    bird7 = bird_animation.at('Fly', 6)
    bird8 = bird_animation.at('Fly', 7)

    bird_text = bird.current_texture()
    bird_text = pygame.transform.scale(bird_text, (64, 64))
    bird_text = pygame.transform.flip(bird_text, True, False)
    screen.blit(bird_text, pygame.rect.Rect(0,0,0,0))

    pygame.display.flip()
