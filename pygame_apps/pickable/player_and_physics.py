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

from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT

ARROW_KEYS = {K_LEFT, K_RIGHT}  # , K_UP, K_DOWN}


class Player(StatefulEntity):
    NECESSARY_STATES = ['Idle Stand', 'Walk']

    def __init__(self,
                 pos: Pair,
                 states: List[str], nominal_anim_fps: int,
                 sprite: pygame.Surface, size: Pair, frame_count_dict: dict,
                 speed: Pair = (0, 50), direction: Pair = (0, 0),
                 **kwargs
                 ):
        StatefulEntity.__init__(self,
                                pos,
                                states, nominal_anim_fps,
                                sprite, size, frame_count_dict,
                                # no extra
                                **kwargs)
        self.speed = speed
        self.MAX_SPEED = 50
        self.direction = direction  # RIGHT SIDE
        # nor parameters:
        self.pressed_keys = set()

    @property
    def flip_x(self):
        return self.direction[0] < 0

    @property
    def bbox_rect(self) -> pygame.rect.Rect:
        w, h = self.curr_texture.get_width(), self.curr_texture.get_height()
        return pygame.rect.Rect(*self.pos, w, h)

    @property
    def curr_texture(self) -> pygame.Surface:
        text = super().curr_texture
        text = pygame.transform.flip(text, flip_x=self.flip_x, flip_y=False)
        return text

    def handle_events(self, events: List[pygame.event.Event]):
        for event in events:
            # update speed and direction
            if event.type == pygame.constants.KEYDOWN and event.key in ARROW_KEYS:
                self.pressed_keys.add(event.key)
            elif event.type == pygame.constants.KEYUP and event.key in ARROW_KEYS:
                self.pressed_keys.remove(event.key)

        # change current direction

        if K_RIGHT in self.pressed_keys:
            self.direction = (1, self.direction[1])
        elif K_LEFT in self.pressed_keys:
            self.direction = (-1, self.direction[1])
        elif K_RIGHT not in self.pressed_keys and K_LEFT not in self.pressed_keys:
            self.direction = (self.direction[0] / 1000, self.direction[1])

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

        print(self.direction, self.pressed_keys)

    def update_position(self, dt: float):
        """
        Use current position, orientation and speed to compute the next position
        :return:
        """
        self.pos = (
            self.pos[0] + dt * self.direction[0] * self.speed[0],
            self.pos[1] + dt * self.direction[1] * self.speed[1]
        )


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
        (120, 0)
    )
    player.update_state(3)
    player.pos = 50, 80

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

    clock = pygame.time.Clock()
    while True:
        dtime = clock.tick(GAME_FPS) / 1000

        # Look at every event in the queue
        events = pygame.event.get()
        handle_events_quit(events)

        # handle the key events
        player.handle_events(events)
        # and adapt the speed and position
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

        # TODO physics for platforms:
        print(dtime, player.speed[1])
        player.pos = (player.pos[0], player.pos[1] + dtime * player.speed[1])

        rect1 = pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect(50, 120, 50, 50))
        rect2 = pygame.draw.rect(screen, (255, 255, 255), pygame.rect.Rect(100, 140, 50, 50))
        if player.bbox_rect.colliderect(rect1):
            player.pos = player.pos[0], rect1.y - player.bbox_rect.height
        elif player.bbox_rect.colliderect(rect2):
            player.pos = player.pos[0], rect2.y - player.bbox_rect.height

        # draw player:

        dog = player.curr_texture
        dog = pygame.transform.flip(dog, flip_x=True, flip_y=False)
        screen.blit(dog, Coords(*player.pos))

        pygame.display.flip()
