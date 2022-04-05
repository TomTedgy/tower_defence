import pygame
import IEightDirAnimationSprite
import helpers
class Projectile(IEightDirAnimationSprite.IEightDirAnimationSprite):
    def __init__(self, igame, group , proj_type ,firing_sprite ,sprite_width , sprite_height,proj_speed, proj_direction, proj_power, start_x, start_y, cells_providers, is_single_collision, firing_freq):

        self._proj_direction = proj_direction
        self._proj_power = proj_power

        # todo : need to make who shot the projectile

        self._is_power_gone = False

        self._proj_type = proj_type

        self._firing_sprite = firing_sprite

        self.set_direction(self._proj_direction)

        super().__init__(igame,group,sprite_width, sprite_height,start_x,start_y, proj_speed, proj_speed,cells_providers,  400)

        self._is_single_collision = is_single_collision

        self._range = proj_power * proj_speed
        self._firing_freq = firing_freq


        self._current_x = start_x
        self._current_y = start_y
        self._target_x, self._target_y = self.get_target(self._current_x, self._current_y, self._proj_direction, self._proj_power * self._speed_x)
        # self.set_direction(direction)


    def get_proj_type(self):
        return self._proj_type

    def get_firing_sprite(self):
        return self._firing_sprite

    def get_target(self,x1,y1, direction , distance):
        x2,y2 = helpers.Helpers.get_target_point_from_point_angle_distance(x1,y1,direction,distance)
        return x2,y2

    @staticmethod
    def get_range():
        return None

    @staticmethod
    # how many seconds between bullets
    def get_firing_freq():
        return None

    @staticmethod
    def get_type():
        return None


    def update(self,dt):

        if self._is_power_gone:
            self.report_on_after_death(self)
        else:

            dx, dy = helpers.Helpers.linear_move_between_two_points(self._current_x, self._current_y, self._target_x, self._target_y, dt, self._speed_x, self._speed_y)

            self._current_x += dx
            self._current_y += dy

            sprite_list = self._igame.check_collision(self, self._is_single_collision)
            if sprite_list:

                for s in sprite_list:
                    s.report_collision_with(self)

            self._pos_x = self._current_x
            self._pos_y = self._current_y

            self._proj_power -= 1*dt
            if self._proj_power <= 0:
                self._is_power_gone = True


        super().update(dt)


