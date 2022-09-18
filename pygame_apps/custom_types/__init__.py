
# trick #2
from typing import Union, Tuple, List

import pygame

Number = Union[int, float]
Pair = Tuple[Number, Number]
Triple = Tuple[Number, Number, Number]
Quad = Tuple[Number, Number, Number, Number]


# trick #3
def Coords(x: int, y: int, w: int = 0, h: int = 0) -> pygame.rect.Rect:
    return pygame.rect.Rect(x, y, w, h)