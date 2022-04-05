import IAnimationSprite

class FloatingButton(IAnimationSprite.IAnimationSprite):
    def __init__(self, igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration, on_button_click, belongs_to_menu):

        self._on_button_click = on_button_click

        super().__init__(igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration)

        self._belongs_to_menu = belongs_to_menu
        self._belongs_to_menu.add_button(self)

    def __del__(self):
        self._belongs_to_menu.remove_button(self)



class FloatingMenu(IAnimationSprite.IAnimationSprite):
    def __init__(self, igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration):
        super().__init__(igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration)

        self._buttons = []

    def get_current_x(self):
        ret = self._pos_x
        for button in self._buttons:
            ret += (button._sprite_width / 4 )
        return ret

    def add_button(self, button):
        if isinstance(button, FloatingButton):
            self._buttons.append(button)

    def remove_button(self, button):
        if button in self._buttons:
            self._buttons.remove(button)

    def clear_all(self):
        for button in self._buttons:
            self.remove_button(button)

    def add_buttons(self, buttons):
        for button in buttons:
            self.add_button(button)
