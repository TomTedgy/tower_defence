import IMovingSprite
import IAnimationSprite
import pygame
import cell_list_provider

class IEightDirAnimationSprite(IMovingSprite.IMovingSprite):
    # def __init__(self,igame, group, sprite_width, sprite_height, start_x , start_y,speed_x , speed_y , cells_provider,animation_start_x, frames_per_animation, millis_per_iteration):
    def __init__(self, igame, group, sprite_width, sprite_height, start_x, start_y, speed_x, speed_y,
                     cells_provider, millis_per_iteration):
        super().__init__(igame, group, sprite_width, sprite_height, start_x , start_y, speed_x , speed_y)
        self._dir_to_animation = {k: IAnimationSprite.IAnimationSprite(self._igame,self.groups(),
                                                                       cells_provider[k],
                                                                       len(cells_provider[k]._cell_list),
                                                                       sprite_width, sprite_height, 0,0,
                                                                       millis_per_iteration) for k in range(8)}
        # self._dir_to_animation = {k: IAnimationSprite.IAnimationSprite(self._igame,self.groups(),
        #                                                                cell_list_provider.sprite_sheet_cell_list_provider(filename,animation_start_x,k * sprite_height ,sprite_width,sprite_height,frames_per_animation, igame._scale),
        #                                                                frames_per_animation,
        #                                                                  sprite_width, sprite_height, 0,0,
        #                                                                  millis_per_iteration) for k in range(8)}
        self._current_direction = 5


    def set_is_one_time_animation(self, is_one_time_animation, on_animation_done_callback):
        for k in self._dir_to_animation:
            self._dir_to_animation[k].set_one_time_animation(is_one_time_animation, on_animation_done_callback)



    def set_cell_list(self, cell_list):
        for k in self._dir_to_animation:
            self._dir_to_animation[k].set_cell_list(cell_list)


    def set_direction(self, direction):
        if direction >= 0 and direction <= 7:
            self._current_direction = direction

    def set_moving(self, moving):
        if moving is False:
            self.stop_moving()
            self._dir_to_animation[self._current_direction].set_animation(False)
        else:
            self._dir_to_animation[self._current_direction].set_animation(True)
            if self._current_direction == 0:
                self.set_moving_left()
                self.stop_moving_up_down()
            elif self._current_direction == 1:
                self.set_moving_up()
                self.set_moving_left()
            elif self._current_direction == 2:
                self.set_moving_up()
                self.stop_moving_left_right()
            elif self._current_direction == 3:
                self.set_moving_up()
                self.set_moving_right()
            elif self._current_direction == 4:
                self.set_moving_right()
                self.stop_moving_up_down()
            elif self._current_direction == 5:
                self.set_moving_down()
                self.set_moving_right()
            elif self._current_direction == 6:
                self.set_moving_down()
                self.stop_moving_left_right()
            elif self._current_direction == 7:
                self.set_moving_down()
                self.set_moving_left()
             # print("dir: {}, speed: {}, {}".format(self._current_direction, self._current_speed_x, self._current_speed_y))

    def update(self, dt):
        self._dir_to_animation[self._current_direction].update(dt)
        super().update(dt)

    def render(self, screen):
        # create a surface for the sprite to be drawn on.
        surface = pygame.Surface((self._sprite_width, self._sprite_height), pygame.SRCALPHA, 32)
        # surface.set_alpha(100)

        # draw the correct facing (direction) sprite on the new surface.
        self._dir_to_animation[self._current_direction].render(surface)

        # draw the drawn sprite (surface) on the screen
        screen.blit(surface, (self._pos_x, self._pos_y), (0, 0, screen.get_width(), screen.get_height()))
