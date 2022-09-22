from enum import Enum

import pygame


class Direction(Enum):
    Up = 1
    Down = 2
    Left = 4
    Right = 3
    # NONE = 5


def collide_rects(rect1: pygame.rect.Rect, rect2: pygame.rect.Rect):
    # trebuie sa obtinem o lista cu laturile (up,down,left, right) lui rect1, unde are loc coliziunea
    directions = set()

    # daca are loc coliziunea pe latura up
    if rect2.y + rect2.h > rect1.y > rect2.y:
        directions.add(Direction.Up)
    # left
    if rect2.x < rect1.x < rect2.x + rect2.w:
        directions.add(Direction.Left)
    # # right
    # if rect1.x + rect1.w > rect2.x > rect1.x:
    #     directions.add(Direction.Right)
    # dowm
    if rect1.y + rect1.h > rect2.y > rect1.y:
        directions.add(Direction.Down)

    return directions


if __name__ == '__main__':

    # s1 = {2, 3, 4}
    # s2 = {2, 4, 3}
    # print(s1 == s2)
    # print({Direction.Up, Direction.Left} == collide_rects(r1, r2))
    # print({Direction.Right, Direction.Down} == collide_rects(r1, r2))

    r1 = pygame.rect.Rect(0, 0, 10, 10)
    r2 = pygame.rect.Rect(5, 5, 15, 15)
    assert collide_rects(r1, r2) == {Direction.Right, Direction.Down}

    # assert collide_rects(r1, r3) == set()

# if __name__ == '__main__':
#     dir = Direction.Up
#     # Test Driven Development
#
#     if dir == Direction.Up:
#         print('going up')
