import pygame.event

from pygame_apps.pickable import Positionable, Pickable, Stateful, StatefulEntity, SimpleSprite, SpriteAnimation
from pygame_apps.pickable import Background, Terrain
from pygame_apps.pickable import *

from pygame_apps.custom_types import *

"""
Today we create a class which can be used to apply physics to an entity.
Be entity we mean a block, a character, player, enemy, or object.

If time is favourable we shall also build a PickableObject with an animation for "Pick Up".
I.e. the object's texture will gradually minimize until it reaches the character's "hand" or front position.
"""

# 1. Controls
# TODO create a class inside which to keep arguments for a StatefulEntity :)

# there are two ways: get events from pygame directly, or create a function towards
#  which YOU MUST pass the events

from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE

MOVEMENT_KEYS = {K_LEFT, K_RIGHT, K_SPACE}  # , K_UP, K_DOWN}


class Physics:
    g = 9.81

    @classmethod
    def falling_speed(cls, falling_time: float) -> float:
        return cls.g * falling_time * 50


class World:
    platforms = []

    @classmethod
    def is_player_falling(cls, player: 'Player'):
        for platform in cls.platforms:
            if player.bbox_rect.colliderect(platform):
                return False
        return True


class Player(StatefulEntity):
    NECESSARY_STATES = ['Idle Stand',
                        'Walk']  # TODO requirements for creating a player: the aprite animation it uses should contains animations named IdelStand and Walk

    def __init__(self,
                 pos: Pair,
                 states: List[str], nominal_anim_fps: int,
                 sprite: pygame.Surface, size: Pair, frame_count_dict: dict,
                 speed: List[float], direction: List[float],
                 **kwargs
                 ):
        StatefulEntity.__init__(self,
                                pos,
                                states, nominal_anim_fps,
                                sprite, size, frame_count_dict,
                                # no extra
                                **kwargs)
        self.speed = speed
        self.speed[1] = 0
        self.MAX_SPEED = 50
        self.direction = direction  # RIGHT SIDE
        # nor parameters:
        self.pressed_keys = set()  # s.add()  s.remove()     K_DOWN in s

        self.t_jump = None
        self.t_fall = None

    @property
    def flip_x(self):
        return self.direction[0] < 0

    @property
    def bbox_rect(self) -> pygame.rect.Rect:
        w, h = self.curr_texture.get_width(), self.curr_texture.get_height()
        return pygame.rect.Rect(self.pos[0], self.pos[1] + 1, w, h)

    @property
    def curr_texture(self) -> pygame.Surface:
        text = super().curr_texture
        text = pygame.transform.flip(text, flip_x=self.flip_x, flip_y=False)
        return text

    def handle_events(self, events: List[pygame.event.Event]):
        for event in events:
            # update speed and direction
            if event.type == pygame.constants.KEYDOWN and event.key in MOVEMENT_KEYS:
                self.pressed_keys.add(event.key)
                if event.key == K_SPACE:
                    # nu poate sa sara daca este in aer deoarece cade, sau daca deja a sarit
                    if self.t_jump is None and self.t_fall is None:
                        print('JUMP')
                        self.t_jump = time.time()
                        self.t_fall = time.time()
                        self.direction[1] = -1  # upwards
            elif event.type == pygame.constants.KEYUP and event.key in MOVEMENT_KEYS:
                self.pressed_keys.remove(event.key)

        # based on the jump time, update the vertical speed
        JUMP_SPEED = 50
        if self.t_jump is not None:
            dt_jump = time.time() - self.t_jump
            # print('DT JUMP:', dt_jump)
            if 1 > dt_jump >= 0:
                self.speed[1] = JUMP_SPEED * (dt_jump / 1)  # int c =  (a>b) ? a : b;
            elif 2 > dt_jump > 1:
                self.speed[1] = JUMP_SPEED - (JUMP_SPEED * ((dt_jump - 1) / (2 - 1)))
                # folosim numarul de secunde din 1,2)  /   cate secunde au trecut de la secunda 1
            else:
                self.speed[1] = 0
                self.direction[1] = 0
                self.t_jump = None

        # change current direction

        if K_RIGHT in self.pressed_keys:
            self.direction[0] = 1
        elif K_LEFT in self.pressed_keys:
            self.direction[0] = -1
        elif K_RIGHT not in self.pressed_keys and K_LEFT not in self.pressed_keys:
            self.direction[0] /= 1000

        # the texture will flip when the direction changes

        # change player states:
        if self.direction[0] not in {1, -1} and self.curr_state != 'Idle Stand':  # add an enum for the necessary states
            self.update_state('Idle Sit')
        elif self.curr_state != 'Run':
            self.update_state('Run')

        '''
        {'Bark': 4,
                                       'Walk': 6,
                                       'Run': 5,
                                       'Sit': 3,
                                       'Get Up': 3,
                                       'Idle Sit': 4,
                                       'Idle Stand': 4, },
        '''

        # print(self.direction, self.pressed_keys)

    def update_position(self, dt: float):
        """
        Use current position, orientation and speed to compute the next position
        :return:
        """
        # based on fall time

        if World.is_player_falling(self):
            print('FALLING')
            if self.t_fall is None:
                self.t_fall = time.time()
            falling_speed = Physics.falling_speed(falling_time=time.time() - self.t_fall)
        else:
            falling_speed = 0

        self.pos[0] += dt * self.direction[0] * self.speed[0]
        print('DIR, SPEED, FALL:', self.direction[1], self.speed[1], falling_speed)
        self.pos[1] += dt * self.direction[1] * (self.speed[1] - falling_speed)


if __name__ == '__main__':
    def handle_events_quit(events: List[pygame.event.Event]):
        for event in events:
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? If so, stop the loop.
                if event.key == K_ESCAPE:
                    quit()

            # Did the user click the window close button? If so, stop the loop.
            elif event.type == QUIT:
                quit()


    pygame.init()
    screen = pygame.display.set_mode((600, 200), flags=pygame.SRCALPHA)

    GAME_FPS = 9
    # TODO move inside a separate file
    dog_sprite = pygame.image.load('../maze/assets/Dog_medium.png').convert_alpha()
    player = Player(
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
                               'Idle Stand': 4, },
        [120, 50], [0, 0]
    )
    player.update_state(3)
    player.pos = [50, 80]

    # # background
    # text_bg = pygame.image.load('../maze/assets/128x128/Tile/Tile_01-128x128.png').convert_alpha()
    # bg = Background(text_bg, (600, 200), (50, 50)).get_bg()
    # bg.set_alpha(70)
    # # terrain
    # surf_bottom = pygame.image.load('../maze/assets/128x128/Grass/Grass_06-128x128.png')
    # surf_top = pygame.image.load('../maze/assets/128x128/Bricks/Bricks_18-128x128.png')
    # terrain = Terrain(surf_bottom, surf_top, 20, (40, 40)).create((550, 100))

    # use time passed for moving the dog using one different animations (sit, get up, walk, run)
    t = time.time()
    falling_time = time.time()

    clock = pygame.time.Clock()
    while True:
        dtime = clock.tick(GAME_FPS) / 1000

        # Look at every event in the queue
        events = pygame.event.get()
        handle_events_quit(events)

        # handle the key events
        player.handle_events(events)
        # and update the speed and position on the screen
        player.update_position(dtime)

        screen.fill(Colors.BLACK)
        # # BG:
        # screen.blit(bg, Coords(0, 0))
        # # TERRAIN
        # screen.blit(terrain, Coords(0, 115))

        # coin = ui_sprite.get(0, 0)
        # coin = pygame.transform.scale(coin, (30, 30))
        # screen.blit(coin, Coords(500, 85))

        # dt = time.time() - t
        # print(dt, dtime)
        # if dt < .3:
        #     dog_entity.update_state('Get Up')
        #     dog_entity.x += dtime * 20
        # elif dt < 4:
        #     dog_entity.update_state('Run')
        #     dog_entity.x += dtime * 80
        # elif dt < 7:
        #     dog_entity.update_state('Walk')
        #     dog_entity.x += dtime * 50
        # elif dt < 7.5:
        #     dog_entity.update_state('Sit')
        #     dog_entity.x += dtime * 10
        # else:
        #     dog_entity.update_state('Idle Sit')

        # compute the vertical speed
        World.platforms = [
            # player-ul trebuie sa cunoasca toate platformele din jurul lui ca sa stie daca inca este in cadere :)
            pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect(50, 120, 50, 50)),
            pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect(100, 170, 50, 50)),
            pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect(150, 120, 50, 50)),
            pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect(200, 70, 50, 50)),
        ]
        # draw player:

        dog = player.curr_texture
        dog = pygame.transform.flip(dog, flip_x=True, flip_y=False)
        screen.blit(dog, Coords(*player.pos))

        pygame.display.flip()
