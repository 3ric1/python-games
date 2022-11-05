import math
import random
import time
from itertools import product

import pygame
from pygame.constants import SRCALPHA
from pygame.rect import Rect
from pygame.surface import Surface
from typing import List

from pygame.time import Clock

from game1_warden.assets.colors import Colors
from game1_warden.bitmap import generate_bitmap, set_alpha
from game1_warden.controls import PressedKeys
from game1_warden.navigation import compute_path

WIDTH_TILE = 32
HEIGHT_TILE = 32

surf_wall = pygame.image.load('assets/Walls/Bricks_17-128x128.png')
surf_wall = pygame.transform.scale(surf_wall, (WIDTH_TILE, WIDTH_TILE))
surf_floor = pygame.image.load('assets/Floors/Tile_19-128x128.png')
surf_floor = pygame.transform.scale(surf_floor, (WIDTH_TILE, WIDTH_TILE))
surf_flash_drive = pygame.image.load('assets/Object/only one game time.png')
surf_flash_drive = pygame.transform.scale(surf_flash_drive, (WIDTH_TILE // 2, WIDTH_TILE // 2))
surf_lamp = pygame.image.load('assets/32x32_Steampunk_Lamps.png')
surf_lamp = pygame.transform.scale(surf_lamp, (WIDTH_TILE // 2, WIDTH_TILE // 2))
surf_drone = pygame.image.load('assets/EnemyId_110091_gray.png')
surf_drone = pygame.transform.scale(surf_drone, (WIDTH_TILE, WIDTH_TILE))

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
    cnt_drones = 0
    obstacle_positions = []
    lamps = []
    cnt_lamps = 10
    for i in range(rows):
        for j in range(cols):
            if random.random() <= 0.2:
                matrix[i][j] = 1
            else:
                # add the drones

                if random.random() <= 0.24 and cnt_lamps != 0:
                    lamps.append([i, j])
                    cnt_lamps -= 1
                if random.random() <= 0.08 and cnt_drones < 3:
                    matrix[i][j] = 2  # 2=occupied by a drone
                    obstacle_positions.append([i, j])
                    cnt_drones += 1

    return matrix, obstacle_positions, lamps


# [
#     [0, 1], # 1 is wall
#     [0, 0], # 0 is floor
# ]
import pprint

GRID_SIZE = GRID_COLS, GRID_ROWS = 10, 10
# a function which randomly fills 20% of the matrix with 1's

"""
Used only at the beginning of the progrtam to generate the unique background
"""


def generate_map_surface(mat: List[List]) -> Surface:
    # create a surface, of the size of the screen
    c = 0
    surf = Surface((WIDTH_TILE * GRID_COLS, WIDTH_TILE * GRID_ROWS), flags=SRCALPHA)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                surf.blit(surf_wall, Rect(i * WIDTH_TILE, j * WIDTH_TILE, 0, 0))
            else:
                surf.blit(surf_floor, Rect(i * WIDTH_TILE, j * WIDTH_TILE, 0, 0))
    return surf


def generate_flash(maze: List[List[int]]) -> List[int]:
    rows, cols = len(maze), len(maze[0])
    is_free = {
        (i, j): maze[i][j] == 0
        for i, j in product(range(rows), range(cols))
    }
    while True:
        i = random.randint(0, rows - 1)
        j = random.randint(0, cols - 1)
        if is_free[(i, j)]:
            break
    return [i, j]


maze, drones, lamps = compute_maze(10, 10)
pprint.pprint(maze)
pprint.pprint(drones)
pprint.pprint(lamps)

surf_bg = generate_map_surface(maze)
bits_bg = generate_bitmap(surf_bg, fill_value=0)

# generate the flash position, and a path plan for each drone to reach the drive

flash_drive_pos = generate_flash(maze)
# the drones' path planning
# TODO create a function which computes a path from start to goal
#  and also uses the maze
path_plans = []
for drone in drones:
    path_plans.append(compute_path(drone, flash_drive_pos, maze))
    del path_plans[-1][0]  # remove the first position

clock = Clock()
t_start = time.time()
dt_start = 0
FPS = 60

SEMIDARK_ALPHA = 125

x_player, y_player = 100, 100

from pygame.constants import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)

pressed_keys = PressedKeys()

while True:
    # dt will always mean the difference of time sine the last frame
    dt = clock.tick(FPS) / 1000
    dt = (time.time() - t_start) - dt_start
    dt_start = time.time() - t_start
    # print(dt_start)

    # TODO THE game logic
    # advance the drones
    #   iterate the path_plan for each drone
    #   for each drone, pop the next position, and move the drone
    #   !!! pay attention to updating the maze

    # after each whole second, update the drones' position:
    if dt_start - math.floor(dt_start) < 1 / FPS:
        for i, path_plan in enumerate(path_plans):
            print(i, path_plan)

            if len(path_plan) == 0:
                continue

            x, y = path_plan[0]
            if maze[x][y] != 0:
                continue

            x_prev, y_prev = drones[i]
            x, y = path_plan.pop(0)
            # update the matrix
            maze[x_prev][y_prev] = 0
            maze[x][y] = 2
            # update the drone's coords
            drones[i] = [x, y]

    # first layer is black
    screen.fill(Colors.BLACK)
    WHITE = (255, 255, 255, 100)


    # second layer is the surface
    # we need to update the alpha for the bg

    # filled the semidark for the bg
    # for a circle around x,y player, set alpha to 255

    def find_circle_bounds(x, y, radius):

        if x - radius < 0:
            startx = 0
        else:
            startx = int(x) - radius
        if x + radius > len(bits_bg[0]) - 1:
            stopx = len(bits_bg[0]) - 1
        else:
            stopx = int(x) + radius
        if y - radius < 0:
            starty = 0
        else:
            starty = int(y) - radius
        if y + radius > len(bits_bg) - 1:
            stopy = len(bits_bg) - 1
        else:
            stopy = int(y) + radius
        return startx, starty, stopx, stopy


    player_radius = 2 * WIDTH_TILE
    startx, starty, stopx, stopy = find_circle_bounds(x_player, y_player, player_radius)

    for x, y in product(range(startx, stopx), range(starty, stopy)):
        if (x - x_player) ** 2 + (y - y_player) ** 2 <= player_radius ** 2:
            bits_bg[x][y] = 1

    for x_lamp, y_lamp in lamps:
        lamp_radius = WIDTH_TILE
        startx, starty, stopx, stopy = find_circle_bounds(x_lamp, y_lamp, lamp_radius)
        for x, y in product(range(startx, stopx), range(starty, stopy)):
            if (x - x_lamp) ** 2 + (y - y_lamp) ** 2 <= lamp_radius ** 2:
                bits_bg[x][y] = 1

    set_alpha(surf_bg, bits_bg, alphaifone=125, alphaifzero=0)

    for x, y in product(range(startx, stopx), range(starty, stopy)):
        if (x - x_player) ** 2 + (y - y_player) ** 2 <= player_radius ** 2:
            newpx = surf_bg.get_at((x, y))
            newpx[3] = 255
            surf_bg.set_at((x, y), newpx)

    # for each lamp, set a little radiusof light

    screen.blit(surf_bg, Rect(0, 0, 0, 0))

    for x, y in lamps:
        screen.blit(surf_lamp, Rect(x * WIDTH_TILE, y * HEIGHT_TILE, 0, 0))

    # TODO draw 3 drones, at the random locations generated before the while True
    # iterate the obstacles, and at that position in the matrix, blit the drone
    for x, y in drones:  # unpacking inside a loop
        # pe ecran, in patratul (Rect) care corespunde cu pozitia x,y, vom da blit la o drona
        screen.blit(surf_drone, Rect(x * WIDTH_TILE, y * HEIGHT_TILE, 0, 0))

    # show the flash drive
    x, y = flash_drive_pos
    screen.blit(surf_flash_drive, Rect(x * WIDTH_TILE, y * HEIGHT_TILE, 0, 0))

    # check the apressed keys and apply a movement
    events = pygame.event.get()
    pressed_keys.update(events)

    print(pressed_keys)
    print(K_UP in pressed_keys)

    # daca < exista si > nu exista, valoarea lui dx va fi -1
    # daca < exista si > exista, valoarea lui dx va fi 0
    # daca > exista si < nu exista, valoarea lui dx va fi 1
    dx, dy = 0, 0
    if K_LEFT in pressed_keys:
        dx = -1
        if K_RIGHT in pressed_keys:
            dx = 0
    elif K_RIGHT in pressed_keys:
        dx = 1
        if K_LEFT in pressed_keys:
            dx = 0
    if K_UP in pressed_keys:
        dy = -1
        if K_DOWN in pressed_keys:
            dy = 0
    elif K_DOWN in pressed_keys:
        dy = 1
        if K_UP in pressed_keys:
            dy = 0

    print('dt', dt)

    x_player += dx * 50 * dt
    y_player += dy * 50 * dt

    pygame.display.flip()
