import engine
class Button(engine.FloatingMenu.FloatingButton):
    FRAMES_PER_ANIMATION = 1
    SPRITE_WIDTH = 87
    SPRITE_HEIGHT = 60
    MILLIS_PER_ITERATION = 500
    MENU_SCALE = 1
    def __init__(self,  igame, group,  start_x , start_y):
        base_dir = "./assets/archer-tower-game-assets/PNG/simplearcherbuilding/level1/"
        cells_provider = engine.cell_list_provider.directory_cell_list_provider(base_dir, '2.png',
                                                                                 igame._scale * self.__class__.MENU_SCALE,
                                                                                 False,
                                                                                 False)


        super().__init__(igame, group, cells_provider, self.__class__.FRAMES_PER_ANIMATION, self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT, start_x , start_y,  self.__class__.MILLIS_PER_ITERATION)
