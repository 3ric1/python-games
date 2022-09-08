from typing import Tuple, List

import pygame
from pygame.surface import Surface


class SpriteAnimation:
    def __init__(self, sprite: Surface, size: Tuple[int, int], animation_names: List[str],
                 frame_count_dict: dict):
        self.sprite = sprite
        self.size = size
        self.animation_names = animation_names
        self.frame_count_dict = frame_count_dict

    def at(self, animation_name: str, frame: int):
        # find the index for the given animation_name
        j = self.animation_names.index(animation_name)
        if j == -1:
            return None
        # extract the image from that row, and the given column (frame)
        i = frame

        x, y = i * self.size[0], j * self.size[1]

        rect = pygame.rect.Rect(x, y, self.size[0], self.size[1])
        surf = pygame.surface.Surface(self.size, flags=pygame.SRCALPHA)
        surf.blit(self.sprite, pygame.rect.Rect(0, 0, 0, 0),
                  area=rect)  # area= este optional, si ii spune sa copieze doar o parte din self.sprite, conform coordonatelor gasite de noi
        # gasim pozitia in pixeli pentru randul i si coloana j

        return surf

    def frame_count(self, state):
        return self.frame_count_dict.get(state, 0)
