import ISprite
import pygame
import cell_list_provider


class IAnimationSprite(ISprite.ISprite):
    def __init__(self, igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration):
        super().__init__(igame, group, sprite_width , sprite_height,start_x , start_y )
        self._frames_per_animation = frames_per_animation
        self._millis_for_one_frame_animation = int(1000 / self._frames_per_animation)

        self._cell_list_provider = cells_provider

        self._is_animation = False

        self._millis_per_iteration = millis_per_iteration

        self._millis_from_start = 0
        self._current_frame = 0

        self._is_one_time_animation = False

        self._cell_list = self._cell_list_provider.provide()

        self._on_animation_done_callback = None

    def update(self, dt):
        # make millis
        dt *= 1000
        self._millis_from_start += dt
        current_frame = self._current_frame

        if self._is_animation:
            self._current_frame = int(((self._millis_from_start % self._millis_per_iteration) * self._frames_per_animation) / self._millis_per_iteration)

        if self._is_one_time_animation:
            if self._current_frame < current_frame:
                self.set_animation(False)
                if self._on_animation_done_callback is not None:
                    self._on_animation_done_callback()

        # print(self._millis_from_start)
        super().update(dt)

    def render(self, screen):

        screen.blit(self._cell_list[self._current_frame], (self._pos_x, self._pos_y))

    def set_cell_list(self, cell_list):
        self._current_frame = 0
        self._cell_list = cell_list

    def set_animation(self, is_animation):
        self._is_animation = is_animation

    def set_one_time_animation(self, is_one_time_animation, on_animation_done_callback):
        self._current_frame = 0
        self._is_one_time_animation = is_one_time_animation
        self._on_animation_done_callback = on_animation_done_callback


if __name__ == "__main__":
    animation_start_x = 128* 4
    animation_start_y = 128 * 7
    start_x = 100
    start_y = 100
    a = IAnimationSprite("./assets/jojo.png", 4, 128, 128, start_x , start_y , animation_start_x , animation_start_y,500)
    print(a._size)