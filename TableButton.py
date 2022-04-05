import engine
class TableButton(engine.FloatingMenu.FloatingButton):
    FRAMES_PER_ANIMATION = 1
    MILLIS_PER_ITERATION = 500
    MENU_SCALE = 1

    def __init__(self, igame, group,cells_provider ,sprite_width, sprite_height, start_x , start_y, on_button_click, belongs_to_menu, selection):
        self._selection = selection
        super().__init__(igame,group,cells_provider, self.__class__.FRAMES_PER_ANIMATION, sprite_width,sprite_height,start_x,start_y, self.__class__.MILLIS_PER_ITERATION,on_button_click, belongs_to_menu)

    def get_selection(self):
        return self._selection

class TableButton_Level1ArcherBuilding(TableButton):
    SPRITE_WIDTH = 168
    SPRITE_HEIGHT = 147
    BUTTON_SCALE = 2
    MILLIS_PER_ITERATION = 500
    SELECTION = "Level1ArcherBuilding"
    def __init__(self,igame, group, belongs_to_menu):
        base_dir = './assets/archer-tower-game-assets/PNG/simplearcherbuilding/level1/'
        cells_provider= engine.cell_list_provider.directory_cell_list_provider(base_dir, '2.png',
                                                                                 igame._scale * self.__class__.BUTTON_SCALE,
                                                                                 False,
                                                                                 False)

        start_x = belongs_to_menu.get_current_x()
        start_y = belongs_to_menu._pos_y
        super().__init__(igame, group,cells_provider ,self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT, start_x , start_y, self.on_button_click, belongs_to_menu, self.__class__.SELECTION)



    def on_button_click(self, position):
        self._igame.on_selection_change(self.get_selection())


class TableButton_Level2ArcherBuilding(TableButton):
    SPRITE_WIDTH = 168
    SPRITE_HEIGHT = 147
    BUTTON_SCALE = 2
    MILLIS_PER_ITERATION = 500
    SELECTION = "Level2ArcherBuilding"

    def __init__(self, igame, group, belongs_to_menu):
        base_dir = './assets/archer-tower-game-assets/PNG/simplearcherbuilding/level2/'
        cells_provider = engine.cell_list_provider.directory_cell_list_provider(base_dir, '4.png',
                                                                                igame._scale * self.__class__.BUTTON_SCALE,
                                                                                False,
                                                                                False)

        start_x = belongs_to_menu.get_current_x()
        start_y = belongs_to_menu._pos_y
        super().__init__(igame, group, cells_provider, self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT,
                         start_x, start_y, self.on_button_click, belongs_to_menu, self.__class__.SELECTION)

    def on_button_click(self, position):
        self._igame.on_selection_change(self.get_selection())


class TableButton_Level3ArcherBuilding(TableButton):
    SPRITE_WIDTH = 168
    SPRITE_HEIGHT = 147
    BUTTON_SCALE = 2
    MILLIS_PER_ITERATION = 500
    SELECTION = "Level3ArcherBuilding"

    def __init__(self, igame, group, belongs_to_menu):
        base_dir = './assets/archer-tower-game-assets/PNG/simplearcherbuilding/level3/'
        cells_provider = engine.cell_list_provider.directory_cell_list_provider(base_dir, '6.png',
                                                                                igame._scale * self.__class__.BUTTON_SCALE,
                                                                                False,
                                                                                False)

        start_x = belongs_to_menu.get_current_x()
        start_y = belongs_to_menu._pos_y
        super().__init__(igame, group, cells_provider, self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT,
                         start_x, start_y, self.on_button_click, belongs_to_menu, self.__class__.SELECTION)

    def on_button_click(self, position):
        self._igame.on_selection_change(self.get_selection())

