import random

import pygame
from pygame.constants import SRCALPHA
from pygame.rect import Rect
from pygame.surface import Surface
from typing import List

from game1_warden.assets.colors import Colors

WIDTH_TILE = 64

wall = pygame.image.load('assets/Walls/Bricks_17-128x128.png')
wall = pygame.transform.scale(wall, (WIDTH_TILE, WIDTH_TILE))
floor = pygame.image.load('assets/Floors/Tile_19-128x128.png')
floor = pygame.transform.scale(floor, (WIDTH_TILE, WIDTH_TILE))
flash_drive = pygame.image.load('assets/Object/only one game time.png')
flash_drive = pygame.transform.scale(flash_drive, (WIDTH_TILE // 2, WIDTH_TILE // 2))
drone = pygame.image.load('assets/EnemyId_110091_gray.png')
drone = pygame.transform.scale(drone, (WIDTH_TILE, WIDTH_TILE))

# creezi ecranul
WIDTH, HEIGHT = WIDTH_TILE * 10, WIDTH_TILE * 10
screen_size = [WIDTH, HEIGHT]

screen = pygame.display.set_mode(screen_size, flags=SRCALPHA)


# a function which returns a GRID_WIDTH x GRID_HEIGHT matrix of zeros
def compute_maze(rows: int, cols: int):
    # [0] + [0]  =>  [0,0]

    one_row = [0] * cols
    matrix = [
        [0] * cols
        for _ in range(cols)
    ]

    # add obstacles
    for i in range(rows):
        for j in range(cols):
                if random.random() <= 0.2:
                    matrix[i][j] = 1
    return matrix


# [
#     [0, 1], # 1 is wall
#     [0, 0], # 0 is floor
# ]
import pprint

GRID_SIZE = GRID_COLS, GRID_ROWS = 10, 10
# a function which randomly fills 20% of the matrix with 1's


def generate_map_surface(mat: List[List]) -> Surface:
    # create a surface, of the size of the screen
    surf = Surface((WIDTH_TILE * GRID_COLS, WIDTH_TILE * GRID_ROWS), flags=SRCALPHA)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                surf.blit(wall, Rect(i * WIDTH_TILE, j * WIDTH_TILE, 0, 0))
            else:
                surf.blit(floor, Rect(i * WIDTH_TILE, j * WIDTH_TILE, 0, 0))
    return surf

maze = compute_maze(10, 10)
pprint.pprint(maze)
# for i in range(10):
#     print(random.random())
#     # print(random.randint(0,1))
#     # print(random.randint(0,4))

bg = generate_map_surface(maze)

# TODO creeaza o functie care genereaza random o locatie din matrice, care este si libera (floor)
#  hint: random.randint(0, len(maze) - 1) alege un rand random
#        similar pt coloana
# cat timp maze[random_row][random_col] == 1, mai incerci generarea

# pasul 2 => de trei ori, apeleaza functia de mai sus, pune valoarea 2 in matrice unde a fost generata pozitia
#              si repeti pentru 3 drone

# pasul 3 => ai retinut intr-o lista pozitiile dronelor, in mainloop parcurge pozitiile generate,
#  si foloseste blit ca dupa ce ai copiat (blit) backgroundul, sa afisezi si drona intr-o pozitie din matrice


while True:
    screen.fill(Colors.BLACK)
    WHITE = (255, 255, 255, 100)

    # surf = Surface((WIDTH_TILE, WIDTH_TILE), flags=SRCALPHA).convert_alpha()
    # surf.fill(WHITE)

    # screen.blit(surf, Rect(0, 0, WIDTH_TILE, WIDTH_TILE))

    screen.blit(bg, Rect(0, 0, 0, 0))

    # TODO draw 3 drones, at the random locations generated before the while True

    pygame.display.flip()
