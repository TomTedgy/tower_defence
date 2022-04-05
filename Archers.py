import engine
import Arrow
class SimpleArcher(engine.AutomaticFiringUnit.AutomaticFiringUnit):
    # outside class members
    FRAMES_PER_ANIMATION = 4
    SPRITE_WIDTH = 87
    SPRITE_HEIGHT  = 60
    MILLIS_PER_ITERATION = 500
    PROJECTILE = Arrow.Arrow
    ARCHER_SCALE = 2
    def __init__(self, igame, group, start_x , start_y):
        self._igame = igame
        self._group = group
        self._start_x = start_x
        self._start_y = start_y

        base_dir = './assets/archer-tower-game-assets/PNG/simplearcher/'
        cells_providers = engine.cell_list_provider.directory_cell_list_provider(base_dir, '.png',
                                                                                     igame._scale * self.__class__.ARCHER_SCALE,
                                                                                     False,
                                                                                     False)



        super().__init__(igame, group, cells_providers, self.__class__.FRAMES_PER_ANIMATION, self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT, start_x , start_y,  self.__class__.MILLIS_PER_ITERATION , self.__class__.PROJECTILE)

    def is_to_flip_horizontally(self, direction):
        if direction == 1 or direction == 0 or direction == 7:
            return True
        return False

    def is_to_flip_vertically(self, direction):
        return False

    def render(self, screen):
        super().render(screen)

    def update(self, dt):
        super().update(dt)


class Level2Archer(engine.AutomaticFiringUnit.AutomaticFiringUnit):
    FRAMES_PER_ANIMATION = 4
    SPRITE_WIDTH = 87
    SPRITE_HEIGHT = 60
    MILLIS_PER_ITERATION = 500
    PROJECTILE = Arrow.Arrow
    ARCHER_SCALE = 2

    def __init__(self, igame, group, start_x, start_y):
        self._igame = igame
        self._group = group
        self._start_x = start_x
        self._start_y = start_y

        base_dir = './assets/archer-tower-game-assets/PNG/sharpshooter/'
        cells_providers = engine.cell_list_provider.directory_cell_list_provider(base_dir, '.png',
                                                                                 igame._scale * self.__class__.ARCHER_SCALE,
                                                                                 False,
                                                                                 False)

        super().__init__(igame, group, cells_providers, self.__class__.FRAMES_PER_ANIMATION,
                         self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT, start_x, start_y,
                         self.__class__.MILLIS_PER_ITERATION, self.__class__.PROJECTILE)

    def is_to_flip_horizontally(self, direction):
        if direction == 1 or direction == 0 or direction == 7:
            return True
        return False

    def is_to_flip_vertically(self, direction):
        return False

    def render(self, screen):
        super().render(screen)

    def update(self, dt):
        super().update(dt)

class Level3Archer(engine.AutomaticFiringUnit.AutomaticFiringUnit):
    FRAMES_PER_ANIMATION = 4
    SPRITE_WIDTH = 87
    SPRITE_HEIGHT = 60
    MILLIS_PER_ITERATION = 500
    PROJECTILE = Arrow.Arrow
    ARCHER_SCALE = 2

    def __init__(self, igame, group, start_x, start_y):
        self._igame = igame
        self._group = group
        self._start_x = start_x
        self._start_y = start_y

        base_dir = './assets/archer-tower-game-assets/PNG/sharpshooter/'
        cells_providers = engine.cell_list_provider.directory_cell_list_provider(base_dir, '.png',
                                                                                 igame._scale * self.__class__.ARCHER_SCALE,
                                                                                 False,
                                                                                 False)

        super().__init__(igame, group, cells_providers, self.__class__.FRAMES_PER_ANIMATION,
                         self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT, start_x, start_y,
                         self.__class__.MILLIS_PER_ITERATION, self.__class__.PROJECTILE)

    def is_to_flip_horizontally(self, direction):
        if direction == 1 or direction == 0 or direction == 7:
            return True
        return False

    def is_to_flip_vertically(self, direction):
        return False

    def render(self, screen):
        super().render(screen)

    def update(self, dt):
        super().update(dt)