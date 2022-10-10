import math
import time
from typing import List

from pygame.constants import KEYDOWN, K_ESCAPE, QUIT

from pygame_apps.custom_types import *
from pygame_apps.pickable import SpriteAnimation, Colors


class Positionable:
    """
    A class used for storing the x and y coordinates.
    Will be inherited in other classes that need this feature, such as platforms, player, enemies
    Practically everything which is set or can move on the screen.
    """

    def __init__(self, pos: Pair):
        self.x, self.y = pos

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, pos: Pair):
        self.x, self.y = pos


# There a number (so multiple) objects present in games (items, textures, walls, traps, NPCs, enemies)
#  which have diverse states (standing, sitting, running, attacking, trap getting triggered) which have different animations.

class Stateful:
    """
    Input: a list of possible states, as str's
            an optional current/initial state
    FUnctions: update_state which used either an index/str (the name of the state) to update the current state

            when you type obj.state it returns the current state

    """

    def __init__(self, states: List[str], *, initial_state: Union[str, int] = 0):
        self.states = states
        self.state = 0
        self.update_state(initial_state)

    # proprietate care returneaza numele state-ului din prezent:
    @property
    def current_state(self):
        return self.states[self.state]

    # o functie update state
    def update_state(self, state: Union[str, int]):
        if isinstance(state, int):  # is initial_state an int?
            if 0 <= state < len(self.states):
                self.state = state  # current state
            else:
                self.state = 0
        # pe ramura else, cautam indicele care corespunde cu valoarea primita in initial_state
        else:
            self.state = self.states.index(state)
            if self.state == -1:
                self.state = 0  # use first state, when the given one is not correct


class StatefulEntity(Positionable, Stateful):
    # noi avem 2 obiective cand mostenim doua clase
    # 1. sa apelam constructorul fiecareia  (ca sa setam field-urile)
    # 2. constructorul lui StatefulEnttiy trebuie sa aiba date pentru ambele clase (adica si pos, dar si states,initial_state

    def __init__(self,
                 # for Positionable
                 pos: Pair,
                 # for Stateful
                 states: List[str],  # also used for SpriteAnimation
                 # for SpriteAnimation
                 sprite: pygame.Surface, size: Tuple[int, int], frame_count_dict: dict,
                 # for animating
                 nominal_anim_fps: int,
                 *, initial_state: Union[str, int] = 0):
        Positionable.__init__(self, pos)
        Stateful.__init__(self, states, initial_state=initial_state)

        # add the animation sprite:
        self.anim_sprite = SpriteAnimation(sprite, size, states, frame_count_dict)
        self.nominal_anim_fps = nominal_anim_fps

        # for animating continuously
        self.frame_index = 0  # current frame for the current animation
        # store the initial time
        self.t = time.time()

    @property
    def curr_texture(self) -> pygame.Surface:
        # how many frames, at the nominal_anim_fps, have passed since self.t ?
        dt = time.time() - self.t  # !!! seconds

        if math.floor(dt * self.nominal_anim_fps) > 0:
            # has one  more fram passed
            self.frame_index += 1
            self.frame_index = self.frame_index % self.anim_sprite.frame_count(
                self.current_state
            )

        return self.anim_sprite.at(self.states[self.state], self.frame_index)

    def update_state(self, state: Union[str, int]):
        super().update_state(state)
        self.frame_index = 0

    # override: Ctrl+O


# TODO Examples

# if __name__ == '__main__':
#     se = StatefulEntity((100, 100), ['run', 'eat'], initial_state='run')
#     se.update_state('eat')
#     se.x = 0


# if __name__ == '__main__':
#     # Info #1    transmiterea parametrilor prin pozitie si prin nume (parametrii numiti)
#     #           = passed by position parameters, named parameters
#     def sum1(a: int, b: int, c: int = 0):
#         return a + b + c
#
#
#     print(sum1(2, 3))
#     print(sum1(2, 3, 100))
#
#
#     def sum2(a: int, b: int, *,
#              c: int = 0):  # *   obliga este pusa la finalul parametrilor simpli (transmisi prin pozitie)
#         return a + b + c
#
#
#     print(sum2(2, 3))
#     print(sum2(2, 3, c=100))
#
#     s = Stateful(['Bark', 'Walk', 'Run', 'Sit', 'Get Up', 'Idle Sit', 'Idle Stand'], initial_state=0)
#     s = Stateful(['Bark', 'Walk', 'Run', 'Sit', 'Get Up', 'Idle Sit', 'Idle Stand'], initial_state=-3)
#     s = Stateful(['Bark', 'Walk', 'Run', 'Sit', 'Get Up', 'Idle Sit', 'Idle Stand'], initial_state=30)
#     s = Stateful(['Bark', 'Walk', 'Run', 'Sit', 'Get Up', 'Idle Sit', 'Idle Stand'], initial_state='Wak')


# class Entity(Positionable):
#     def __init__(self,
#                  pos: Pair):
#         # pass fields for Positionable
#         Positionable.__init__(self, pos)
#
# # if __name__ == '__main__':
# #     positioned_dog = Positionable((2, 3))
# #     print(positioned_dog.x, positioned_dog.y, positioned_dog.pos)
# #     positioned_dog.pos = 100, 10  # apeleaza functia decorata cu    @pos.setter
# #
# #     # using Entity:
# #     dog = Entity((50, 100))
# #     dog.x += 20


# simple sprite


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


# TODO The Game:

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1000, 600), flags=pygame.SRCALPHA)

    GAME_FPS = 9

    # create textures and other actors/entities..
    text_ui_icons = pygame.image.load('../maze/assets/ui_icons.png').convert_alpha()
    ui_sprite = SimpleSprite(500, 500, text_ui_icons, convert_to=(50, 50))

    dog_sprite = pygame.image.load('../maze/assets/Dog_medium.png').convert_alpha()
    dog_entity = StatefulEntity(
        (0, 0),
        ['Bark', 'Walk', 'Run', 'Sit', 'Get Up', 'Idle Sit', 'Idle Stand'],
        dog_sprite, (60, 38), {'Bark': 4,
                               'Walk': 6,
                               'Run': 5,
                               'Sit': 3,
                               'Get Up': 3,
                               'Idle Sit': 4,
                               'Idle Stand': 4, },

        9,  # so the image changes 10 times per second, no matter the state
        #       maybe we should set it for each frame, optionally?
    )
    dog_entity.update_state(3)
    dog_entity.pos = 50, 80

    # # background
    # text_bg = pygame.image.load('../maze/assets/128x128/Floors/Tile_01-128x128.png').convert_alpha()
    # bg = Background(text_bg, (600, 200), (50, 50)).get_bg()
    # bg.set_alpha(70)
    # # terrain
    # surf_bottom = pygame.image.load('../maze/assets/128x128/Grass/Grass_06-128x128.png')
    # surf_top = pygame.image.load('../maze/assets/128x128/Walls/Bricks_18-128x128.png')
    # terrain = Terrain(surf_bottom, surf_top, 20, (40, 40)).create((550, 100))

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
        # # BG:
        # screen.blit(bg, Coords(0, 0))
        # # TERRAING
        # screen.blit(terrain, Coords(0, 115))

        coin = ui_sprite.get(0, 0)
        coin = pygame.transform.scale(coin, (30, 30))
        screen.blit(coin, Coords(500, 85))

        dog = dog_entity.curr_texture
        dog = pygame.transform.flip(dog, flip_x=True, flip_y=False)

        dt = time.time() - t
        print(dt, dtime)
        if dt < .15:
            if dog_entity.current_state != 'Get Up':
                dog_entity.update_state('Get Up')
            dog_entity.x += dtime * 20
        elif dt < 4:
            if dog_entity.current_state != 'Run':
                dog_entity.update_state('Run')
            dog_entity.x += dtime * 80
        elif dt < 7:
            if dog_entity.current_state != 'Walk':
                dog_entity.update_state('Walk')
            dog_entity.x += dtime * 50
        elif dt < 7.15:
            if dog_entity.current_state != 'Sit':
                dog_entity.update_state('Sit')
            dog_entity.x += dtime * 10
        else:
            if dog_entity.current_state != 'Idle Sit':
                dog_entity.update_state('Idle Sit')

        screen.blit(dog, Coords(*dog_entity.pos))

        surface = pygame.display.set_mode((400, 300))

        # Initialing Color
        color = (255, 0, 0)

        # Drawing Rectangle
        pygame.draw.rect(surface, color, pygame.Rect(0, 250, 800, 50))
        pygame.display.flip()

        pygame.display.flip()

# TODO tema
#  de implementat urmatoarele exemple: Background, Platform si folosit pentru a crea un "level"
#  sa modifici si marimea ecranului (1000, 600)
#  use event icons such as coint, hearts, and place them where you want