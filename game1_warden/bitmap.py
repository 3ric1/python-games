from pprint import pprint

import pygame
from itertools import product
from pygame.constants import SRCALPHA
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.time import Clock

from game1_warden.assets.colors import Colors


def generate_bitmap(surf: Surface, fill_value=1) -> list[list[int]]:
    return [
        [
            fill_value
            for j in range(surf.get_width())
        ] for i in range(surf.get_height())
    ]


def set_alpha(surf: Surface, image_bitmap: list[list[int]], *, alphaifone=125, alphaifzero=0):
    for x, y in product(range(surf.get_height()), range(surf.get_width())):

        #  pentru fiecare pixel in parte,
        #   daca bit-ul de la aceasta pozitie este 1 pastram alpha 125,
        #   altfel setam alpha la 0 pentru acel pixel

        pixel = surf.get_at((x, y))
        if image_bitmap[x][y] == 1:
            new_pixel = [*pixel[:3], alphaifone]  # [*[1,2,3], 4]   ...    [1,2,3,4]  unpack
        else:
            new_pixel = [*pixel[:3], alphaifzero]
        surf.set_at((x, y), new_pixel)


if __name__ == '__main__':
    image_bitmap = "00000000 " \
                   "01100110 " \
                   "01100110 " \
                   "01111110 " \
                   "01111110 " \
                   "00000000 " \
                   "01111110 " \
                   "00000000 "
    orig_bitmap = [
        [
            int(c)  # True if c == '1' else False
            for c in list(elem)
        ]
        for elem in image_bitmap.split()
    ]
    # magnify the matrix
    scale = 4
    rows, cols = len(orig_bitmap), len(orig_bitmap[0])
    image_bitmap = [
        [
            0
            for j in range(cols * scale)
        ] for i in range(rows * scale)
    ]
    for x1, y1 in product(range(cols), range(rows)):
        for x, y in product(
                range(x1 * scale, (x1 + 1) * scale),
                range(y1 * scale, (y1 + 1) * scale),
        ):
            image_bitmap[x][y] = orig_bitmap[x1][y1]
    # pprint(orig_bitmap)
    # pprint(image_bitmap)
    # quit()

    rows, cols = len(image_bitmap), len(image_bitmap[0])
    print(image_bitmap)  # list('abc')  ==  ['a', 'b', 'c']

    screen = pygame.display.set_mode((cols, rows), flags=SRCALPHA)

    surf = Surface((cols, rows), flags=SRCALPHA).convert_alpha()
    surf.fill((0, 0, 255, 255))  # blue

    clock = Clock()
    while True:
        clock.tick(1)

        screen.fill(Colors.WHITE)
        # parcurgem i,j indicii pixelilor (aceiasi indici precum  ai bitmap-ului asociat cu surf)
        for x, y in product(range(rows), range(cols)):

            #  pentru fiecare pixel in parte,
            #   daca bit-ul de la aceasta pozitie este 1 pastram alpha 125,
            #   altfel setam alpha la 0 pentru acel pixel

            pixel = surf.get_at((x, y))
            if image_bitmap[x][y] == 1:
                new_pixel = [*pixel[:3], 255]  # [*[1,2,3], 4]   ...    [1,2,3,4]  unpack
            else:
                new_pixel = [*pixel[:3], 100]
            surf.set_at((x, y), new_pixel)

        screen.blit(surf, Rect(0, 0, 0, 0))

        pygame.display.flip()
