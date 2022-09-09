"""
Objective: create a class named Pickable and a class named Positionable, this class will
"""
import time
import math

from typing import List

from pygame import KEYDOWN, K_ESCAPE
from pygame.constants import QUIT

from pygame_apps.sprite_animation import SpriteAnimation
from pygame_apps.pickable.colors import Colors

from pygame_apps.custom_types import *

class Positionable:

    def __init__(self, pos: Pair):
        self.x, self.y = pos

    @property  # @keyword    it's called decoration, so we decorate a function
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, pos: Pair):
        self.x, self.y = pos


class Pickable(Positionable):
    def __init__(self, pos: Pair, texture: SpriteAnimation):
        self.pos = pos
        self.texture = texture


class SimpleSprite:
    def __init__(self, img_width: int, img_height: int, sprite: pygame.Surface, *,
                 convert_to: Pair = None):
        self.img_width = img_width
        self.img_height = img_height
        self.sprite = sprite
        if convert_to is None:
            self.out_width, self.out_height = img_width, img_height
        self.out_width, self.out_height = convert_to

    def get(self, row: int, col: int) -> pygame.Surface:
        text = pygame.surface.Surface((self.img_width, self.img_height), flags=pygame.SRCALPHA)
        text.blit(
            self.sprite,
            Coords(0, 0),
            area=pygame.rect.Rect(
                col * self.img_width,
                row * self.img_height,
                self.img_width,
                self.img_height
            )
        )
        return pygame.transform.scale(text, (self.out_width, self.out_height))


# There a number (so multiple) objects present in games (items, textures, walls, traps, NPCs, enemies)
#  which have diverse states (standing, sitting, running, attacking, trap getting triggered) which have different animations.

class Stateful:

    def __init__(self, states: List[str], *, initial_state: Union[int, str] = 0):
        self.states = states

        self.state_index = 0
        self.update_state(initial_state)

    def update_state(self, state: Union[int, str]):
        if isinstance(state, int) and 0 <= state < len(self.states):
            self.state_index = state
        else:
            # look up by name
            i = self.states.index(state)
            # if not found, use first animation:
            if i == -1:
                i = 0
            self.state_index = i


class StatefulEntity(Positionable, Stateful):
    def __init__(self,
                 pos: Pair,
                 states: List[str], nominal_anim_fps: int,
                 sprite: pygame.Surface, size: Pair, frame_count_dict: dict,
                 **kwargs):
        # pass fields for Positionable
        Positionable.__init__(self, pos)
        # pass fields for Stateful, it it exists
        Stateful.__init__(self, states, initial_state=kwargs.get('initial_state', 0))

        # create the animation sprite
        self.anim_sprite = SpriteAnimation(sprite, size, states, frame_count_dict)
        self.nominal_anim_fps = nominal_anim_fps

        # for animating continuously
        self.frame_index = 0
        # TODO add a continuous timer
        self.t = time.time()

    @property
    def curr_texture(self) -> pygame.Surface:
        # how many frames, at the nominal_anim_fps, have passed since self.t ?
        dt = time.time() - self.t  # !!! seconds
        frames_since = math.floor(dt * self.nominal_anim_fps)

        # print(dt, frames_since)
        curr_state = self.states[self.state_index]
        self.frame_index = frames_since % self.anim_sprite.frame_count(
            curr_state
        )  # TODO may divide by 0, if the state name is wrong

        return self.anim_sprite.at(self.states[self.state_index], self.frame_index)


# next time: physics such as falling, and player controls, so we also need platforms and collisions today
# today we may also do a pickable? Or next time?


# TODO use caching
class Background:
    """input a texture and repeat it for the given size"""

    def __init__(self, text: pygame.Surface, out_size: Pair, unit_size: Pair = None):
        if unit_size:
            self.text = pygame.transform.scale(text, unit_size)
            self.unit_size = unit_size
        else:
            self.text = text
            self.unit_size = self.text.get_size()

        self.txt_size = self.text.get_size()
        self.out_size = out_size

    def get_bg(self) -> pygame.Surface:
        bg_text = pygame.Surface(self.out_size, flags=pygame.SRCALPHA)
        w, h = self.txt_size
        out_w, out_h = self.out_size
        rows, cols = math.ceil(out_h / h), math.ceil(out_w / w)
        for i in range(0, cols):
            for j in range(0, rows):
                bg_text.blit(self.text, Coords(i * w, j * h, *self.unit_size))
        return bg_text


class Terrain:
    """Input a texture for most of the platform, and a different texture for the top "top_height" pixels

    it has a function which outputs a terrain of given size

    """

    def __init__(self, main_text: pygame.Surface, top_text: pygame.Surface,
                 top_height: int, unit_size: Pair):
        self.main_text = main_text
        self.top_text = top_text
        self.top_height = top_height
        self.unit_size = unit_size

    def create(self, size: Pair):
        bottom_size = (size[0], size[1] - self.top_height)
        bottom = Background(self.main_text, bottom_size, self.unit_size).get_bg()

        top_size = (size[0], self.top_height)
        top = Background(self.top_text, top_size, self.unit_size).get_bg()

        surf = pygame.Surface(size, flags=pygame.SRCALPHA)
        surf.blit(top, Coords(0, 0))
        surf.blit(bottom, Coords(0, self.top_height))

        return surf


"""
TODO collisions
"""

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600, 200), flags=pygame.SRCALPHA)

    GAME_FPS = 9

    # create textures and other actors/entities..
    text_ui_icons = pygame.image.load('../maze/assets/ui_icons.png').convert_alpha()
    ui_sprite = SimpleSprite(500, 500, text_ui_icons, convert_to=(50, 50))

    dog_sprite = pygame.image.load('../maze/assets/Dog_medium.png').convert_alpha()
    dog_entity = StatefulEntity(
        (0, 0),
        ['Bark', 'Walk', 'Run', 'Sit', 'Get Up', 'Idle Sit', 'Idle Stand'],
        9,  # so the image changes 10 times per second, no matter the state
        #       maybe we should set it for each frame, optionally?
        dog_sprite, (60, 38), {'Bark': 4,
                               'Walk': 6,
                               'Run': 5,
                               'Sit': 3,
                               'Get Up': 3,
                               'Idle Sit': 4,
                               'Idle Stand': 4, }
    )
    dog_entity.update_state(3)
    dog_entity.pos = 50, 80

    # background
    text_bg = pygame.image.load('../maze/assets/128x128/Tile/Tile_01-128x128.png').convert_alpha()
    bg = Background(text_bg, (600, 200), (50, 50)).get_bg()
    bg.set_alpha(70)
    # terrain
    surf_bottom = pygame.image.load('../maze/assets/128x128/Grass/Grass_06-128x128.png')
    surf_top = pygame.image.load('../maze/assets/128x128/Bricks/Bricks_18-128x128.png')
    terrain = Terrain(surf_bottom, surf_top, 20, (40, 40)).create((550, 100))

    # use time passed for moving the dog using one different animations (sit, get up, walk, run)
    t = time.time()

    clock = pygame.time.Clock()
    while True:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    quit()

            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                quit()

        dtime = clock.tick(GAME_FPS) / 1000

        screen.fill(Colors.BLACK)
        # BG:
        screen.blit(bg, Coords(0, 0))
        # TERRAING
        screen.blit(terrain, Coords(0, 115))

        coin = ui_sprite.get(0, 0)
        coin = pygame.transform.scale(coin, (30, 30))
        screen.blit(coin, Coords(500, 85))

        dog = dog_entity.curr_texture
        dog = pygame.transform.flip(dog, flip_x=True, flip_y=False)

        dt = time.time() - t
        print(dt, dtime)
        if dt < .3:
            dog_entity.update_state('Get Up')
            dog_entity.x += dtime * 20
        elif dt < 4:
            dog_entity.update_state('Run')
            dog_entity.x += dtime * 80
        elif dt < 7:
            dog_entity.update_state('Walk')
            dog_entity.x += dtime * 50
        elif dt < 7.5:
            dog_entity.update_state('Sit')
            dog_entity.x += dtime * 10
        else:
            dog_entity.update_state('Idle Sit')

        screen.blit(dog, Coords(*dog_entity.pos))

        pygame.display.flip()
