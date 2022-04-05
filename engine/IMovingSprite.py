import ISprite


class IMovingSprite(ISprite.ISprite):
    def __init__(self,igame, group, sprite_width, sprite_height, start_x , start_y, speed_x , speed_y):
        super().__init__(igame, group, sprite_width, sprite_height, start_x, start_y)

        self._speed_x = speed_x
        self._speed_y = speed_y

        self._current_speed_x = 0
        self._current_speed_y = 0

    def update(self, dt):
        self._pos_x += int(self._current_speed_x * (dt))
        self._pos_y += int(self._current_speed_y * (dt))

        self.rect.x = self._pos_x
        self.rect.y = self._pos_y

        # print('{},{}'.format(self._pos_x , self._pos_y))
        super().update(dt)
        # check collision
        if self._current_speed_x != 0 or self._current_speed_y != 0:
            self._igame.report_moving_sprite(self)



    def set_moving_right(self):
        self._current_speed_x = self._speed_x

    def set_moving_left(self):
        self._current_speed_x = -self._speed_x

    def set_moving_up(self):
        self._current_speed_y = -self._speed_y

    def set_moving_down(self):
        self._current_speed_y = self._speed_y

    def stop_moving_up_down(self):
        self._current_speed_y = 0

    def stop_moving_left_right(self):
        self._current_speed_x = 0

    def stop_moving(self):
        self.stop_moving_left_right()
        self.stop_moving_up_down()

    def render(self, screen):
        pass