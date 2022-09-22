# background
from datetime import time

import pygame
from pygame.time import Clock

from pygame_apps.pickable import Background, Terrain, Colors, Positionable

screen = pygame.display.set_mode((800, 600), flags=pygame.SRCALPHA)

text_bg_ = pygame.image.load('../../maze/assets/128x128/Backgrounds/Trees2_Background.png')
text_bg_brick = pygame.image.load('../../maze/assets/128x128/Tile/Tile_01-128x128.png')
# text_bg_sky = pygame.image.load('../../maze/assets/128x128/Backgrounds/Stars2_Background.png')
bg = Background(text_bg_brick, (800, 600), (25, 25)).get_bg()
bg.set_alpha(100)
# terrain
surf_bottom = pygame.image.load('../../maze/assets/128x128/Bricks/Bricks_17-128x128.png')
surf_top = pygame.image.load('../../maze/assets/128x128/Grass/Grass_07-128x128.png')
terrain_creator = Terrain(surf_bottom, surf_top, 20, (40, 40))
terrain1 = terrain_creator.create((550, 100))
terrain2 = terrain_creator.create((100, 500))

clock = Clock()
init_time = time.time()
FPS = 10

while True:
    dt = clock.tick(FPS)
    dtime = time.time() - init_time  # seconds till the game started

    screen.fill(Colors.BLACK)
    # bg = pygame.transform.scale(text_bg, (screen.get_width(), screen.get_height()))
    #bg = pygame.transform.scale(text_bg_brick, (screen.get_width(), screen.get_height()))
    screen.blit(bg, pygame.rect.Rect(0, 0, 0, 0))
    screen.blit(terrain1, pygame.rect.Rect(200, 50, 0, 0))
    screen.blit(terrain2, pygame.rect.Rect(700, 400, 0, 0))

    # # TODO tema  de creat 3 nivele cu platforme
    # #  optional -> de creeate o clasa Platform care este initializata cu un background (de tip Surface)
    # #              pozitia lui (prin mostenire Positionable)
    # #              si de scris cod
    # class Platform(Positionable):
    #     pass
    # platform = Platform(...)
    # platform.x += 10

    # poti avea o variabile curr_direction care sa fie    "LEFT" sau "RIGHT"
    #  la fiecare 3 secunde, schimb directia        if dtime % 3 < 1/FPS

    pygame.display.flip()
