import SelectableSprite

class Building(SelectableSprite.SelectableSprite):
    def __init__(self, igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration, max_units, on_selected, menu_buttons):
        super().__init__(igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration , on_selected, menu_buttons)
        self._max_units = max_units
        self._units = []


    def can_add_unit(self):
        return len(self._units) < self._max_units


    def render(self, screen):
        super().render(screen)

    def update(self, dt):
        super().update(dt)

    def add_unit(self, unit):
        if len(self._units) < self._max_units:
            self._units.append(unit)
            unit._pos_x = self._pos_x
            unit._pos_y = self._pos_y - (unit._sprite_height / 4 )
            if len(self._units) == 2:
                unit._pos_x = self._pos_x + (self._sprite_width - unit._sprite_width) / 2.5

    def remove_unit(self, unit):
        if unit in self._units:
            self._units.remove(unit)