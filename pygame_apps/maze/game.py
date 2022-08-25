import pygame

# from pygame import *

import sys, pygame

# creezi aplicatia pygame
from pygame.time import Clock

# import colors
from colors import *

pygame.init()
screen_size = screen_width, screen_height = 400, 400

# folosim pygame.SRCALPHA ca in pixelii ecranului sa existe si un canal ALPHA cu transparenta fiecare pixel
screen = pygame.display.set_mode(screen_size, pygame.SRCALPHA)  # e necesar ca sa creeze o fereastra

texture_wood = pygame.image.load(
    "128x128/Wood/Wood_14-128x128.png").convert_alpha()  # in unele versiuni/cazuri, e nevoie de convert_alpha pt ca nu adauga si canalul alpha in mod automat

# game loop-ul aplicatiei, adica ce scriem in while se executa la fiecare frame in parte
# de aceea, crem un clock care va fi folosit pentru limitarea la un anumit numar de cadre pe secunda
fps = 10
clock = Clock()

# Todo Tema: poti folosi ball_resized_and_rotated.get_rect() ca sa gasesti pozitia mingii, si sa te folosesti de asta pentru a o pozitiona in centrul ecranului

# cream texture de  50 pe 50
text_grass_128 = pygame.image.load("128x128/Grass/Grass_24-128x128.png").convert_alpha()
text_gras_50 = pygame.transform.scale(text_grass_128, (50, 50))
text_wood_128 = pygame.image.load("128x128/Wood/Wood_14-128x128.png").convert_alpha()
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

while True:
    dtime = clock.tick(fps) / 1000

    for event in pygame.event.get():
        event_handle_quit(event)

    screen.fill(COLOR_WHITE)

    # # practic, cu blit desenam texturi pe ecran, sau pe alte texturi
    # screen.blit(texture_wood, pygame.rect.Rect((10, 10, 148, 148)))
    # # pe alte texturi?
    # double_wood = pygame.Surface((384, 384), flags=pygame.SRCALPHA)
    # double_wood.fill(COLOR_WHITE)
    # double_wood.blit(texture_wood, pygame.rect.Rect(0, 0, 0, 0))
    # double_wood.blit(texture_wood, pygame.rect.Rect(0, 128, 0, 0))

    # # daca vrem sa marim/ micsoram texturile e.g. facem un joccu tiles the 50x50
    # #  putem folosi pygame.transform, atat pentru micsorare cat si pentru marire
    # texture_wood_50 = pygame.Surface((250, 250))
    # pygame.transform.scale(texture_wood, (250, 250), texture_wood_50)
    # # txt = pygame.transform.rotate(texture_wood_50, 90)
    #
    #
    # screen.blit(txt, pygame.rect.Rect(0,0,0,0))

    # ex. 1    pentru ecranul de 400 pe 400 de pixeli, vom crea un grid de 8x8 texturi de
    #           50x50 px.    Ca sa lucram eficient, vom crea un surface de 400x400 unde desenam toate texturile
    # Bonus: sa folosim ce am invatat pentru a crea o textura de 400 pe 400 cu doua modele de pioatra intercalate
    # ex 1' ca TODO tema, sa si rotim la 45 de grade un numar suficient de mare de tiles intercalate, ca sa obtinem ex1.png
    # TODO practic la 1' este nevoia s acreezi un background suficient de mare cat sa acopere intreg ecranul cand il rotesti la 45 grade
    # TODO recomandare: creeaza o functie care il genereaza (returneaza un surface
    # rotated = pygame.transform.rotate(text_bg_tiled, 45)
    # screen.blit(rotated, pygame.rect.Rect((-100,-100,0,0)))

    text_wood_50_transparent = text_wood_50.copy()
    text_wood_50_transparent.set_alpha(100)
    for i in range(0, 11, 2):
        for j in range(0, 11, 2):
            rotated = pygame.transform.rotate( text_wood_50_transparent, 45)
            screen.blit(rotated, pygame.rect.Rect(i * 35, j * 35, 0, 0))



    pygame.display.flip()



