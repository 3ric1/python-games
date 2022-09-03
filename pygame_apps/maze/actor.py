import time

from pygame_apps.maze.sprite_animation import SpriteAnimation


class Actor:
    def __init__(self, anim_sprite: SpriteAnimation, state: str, fps: int = 5):
        self.anim_sprite = anim_sprite
        self.fps = fps

        self.state = state
        self.time = time.time()
        self.state_frame = 0

    def set_state(self, new_state: str):
        self.state = new_state
        self.time = time.time()
        self.state_frame = 0

    def current_texture(self):
        # depending on the time passed after the last frame,
        #  it will return another frame
        # e.g. we set the frames to changes every 0.25 seconds (at a 4 fps rate)

        # extract the fractional part

        dtime = time.time() - self.time  #
        fractional = dtime

        if fractional > 1 / self.fps:
            self.time = time.time()
            self.state_frame += 1
            self.state_frame = self.state_frame % self.anim_sprite.frame_count(self.state)

        return self.anim_sprite.at(self.state, self.state_frame)