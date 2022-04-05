import engine

class TableMenu(engine.FloatingMenu.FloatingMenu):
    FRAMES_PER_ANIMATION = 1
    SPRITE_WIDTH = 336
    SPRITE_HEIGHT = 93
    MILLIS_PER_ITERATION = 500
    MENU_SCALE = 1
    def __init__(self, igame, group ,start_x , start_y):
        base_dir = './assets/td-gui/PNG/menu/'
        cells_providers = engine.cell_list_provider.directory_cell_list_provider(base_dir, 'table_2.png',
                                                                                 igame._scale * self.__class__.MENU_SCALE,
                                                                                 False,
                                                                                 False)

        super().__init__(igame, group, cells_providers, self.__class__.FRAMES_PER_ANIMATION, self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT, start_x , start_y,  self.__class__.MILLIS_PER_ITERATION)


    # event handlers
    def on_mouse_click(self, position):
        relative_x = position[0] - self._pos_x
        relative_y = position[1] - self._pos_y

        accumulative_sprite_width = 0
        accumulative_sprite_height = 0
        handled = False
        for button in self._buttons:
            button_width =button._sprite_width /4
            button_height = button._sprite_height/4
            if relative_x > accumulative_sprite_width and relative_x < button_width + accumulative_sprite_width:
                if relative_y > accumulative_sprite_height and relative_y <button_height + accumulative_sprite_height:
                    button._on_button_click((relative_x - accumulative_sprite_width, relative_y - accumulative_sprite_height))
                    handled = True
                    break
            # accumulative_sprite_height += button._sprite_height / 4
            accumulative_sprite_width += button._sprite_width / 4






