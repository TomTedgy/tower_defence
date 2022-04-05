import IAnimationSprite

class SelectableSprite(IAnimationSprite.IAnimationSprite):
    def __init__ (self, igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration, on_selected, menu_buttons):

        self._on_selected = on_selected
        self._buttons = menu_buttons[:]
        super().__init__(igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration)

    # event handlers
    def on_selected(self):
        # raise callback
        self._on_selected()
        # report to igame
        self._igame.on_selectablesprite_selected(self)
