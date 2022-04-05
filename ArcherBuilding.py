import engine

class ArcherBuilding_Level1(engine.Building.Building):
    MILLIS_PER_ITERATION = 500
    MAX_UNITS = 2
    SPRITE_WIDTH = 168
    SPRITE_HEIGHT = 147 + 37
    FRAMES_PER_ANIMATION = 1
    BUILDING_SCALE = 2
    def __init__(self,game, group, start_x , start_y):
        base_dir = './assets/archer-tower-game-assets/PNG/simplearcherbuilding/level1/'
        cells_providers = engine.cell_list_provider.directory_cell_list_provider(base_dir, '2.png',
                                                                                 game._scale * self.__class__.BUILDING_SCALE,
                                                                                 False,
                                                                                 False)
        self._menu_buttons = []

        super().__init__(game, group , cells_providers,self.__class__.FRAMES_PER_ANIMATION , self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT, start_x, start_y, self.__class__.MILLIS_PER_ITERATION, self.__class__.MAX_UNITS,self.on_selected_handler, self._menu_buttons)

    def on_selected_handler(self):
        pass

class ArcherBuilding_Level2(engine.Building.Building):
    MILLIS_PER_ITERATION = 500
    MAX_UNITS = 2
    SPRITE_WIDTH = 168
    SPRITE_HEIGHT = 147 + 37
    FRAMES_PER_ANIMATION = 1
    BUILDING_SCALE = 2
    def __init__(self,game, group, start_x , start_y):
        base_dir = './assets/archer-tower-game-assets/PNG/simplearcherbuilding/level2/'
        cells_providers = engine.cell_list_provider.directory_cell_list_provider(base_dir, '4.png',
                                                                                 game._scale * self.__class__.BUILDING_SCALE,
                                                                                 False,
                                                                                 False)
        self._menu_buttons = []

        super().__init__(game, group , cells_providers,self.__class__.FRAMES_PER_ANIMATION , self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT, start_x, start_y, self.__class__.MILLIS_PER_ITERATION, self.__class__.MAX_UNITS, self.on_selected_handler, self._menu_buttons)

    def on_selected_handler(self):
        pass


class ArcherBuilding_Level3(engine.Building.Building):
    MILLIS_PER_ITERATION = 500
    MAX_UNITS = 2
    SPRITE_WIDTH = 171
    SPRITE_HEIGHT = 163
    FRAMES_PER_ANIMATION = 1
    BUILDING_SCALE = 2
    def __init__(self,game, group, start_x , start_y):
        base_dir = './assets/archer-tower-game-assets/PNG/simplearcherbuilding/level3/'
        cells_providers = engine.cell_list_provider.directory_cell_list_provider(base_dir, '6.png',
                                                                                 game._scale * self.__class__.BUILDING_SCALE,
                                                                                 False,
                                                                                 False)
        self._menu_buttons = []
        super().__init__(game, group , cells_providers,self.__class__.FRAMES_PER_ANIMATION , self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT, start_x, start_y, self.__class__.MILLIS_PER_ITERATION, self.__class__.MAX_UNITS, self.on_selected_handler, self._menu_buttons)

    def on_selected_handler(self):
        pass
