import engine


class Arrow(engine.Projectile.Projectile):
    SPRITE_WIDTH  = 117
    SPRITE_HEIGHT = 115
    PROJ_SPEED = 800
    PROJ_POWER = 0.5
    ATTACK_POWER = 0.5
    IS_SINGLE_COLLISION = True
    ARROW_SCALE = 2
    FIRING_FREQ = 0.8
    PROJECTILE_TYPE = "arrow"

    def __init__(self,igame,  group ,firing_sprite,  proj_direction, start_x, start_y):

        # initialize
        base_dir = 'assets/archer-tower-game-assets/PNG/'
        #directory , filter, scale, flip_horizontally, flip_vertically
        cells_providers = {k: engine.cell_list_provider.directory_cell_list_provider(base_dir, '35.png', igame._scale  * self.__class__.ARROW_SCALE,
                                                                                     self.is_to_flip_horizontally(k),
                                                                                     self.is_to_flip_vertically(k)) for
                           k in range(8)}

        super().__init__(igame, group ,self.__class__.PROJECTILE_TYPE , firing_sprite,
                         self.__class__.SPRITE_WIDTH , self.__class__.SPRITE_HEIGHT,
                         self.__class__.PROJ_SPEED, proj_direction, self.__class__.PROJ_POWER,
                         start_x, start_y, cells_providers, self.__class__.IS_SINGLE_COLLISION,
                         self.__class__.FIRING_FREQ)

    # event handlers
    def on_after_collision(self, collided_with):
        self.report_on_after_death(self)

    @staticmethod
    def get_range():
        return Arrow.PROJ_POWER * Arrow.PROJ_SPEED

    @staticmethod
    def get_firing_freq():
        return Arrow.FIRING_FREQ


    @staticmethod
    def get_type():
        return Arrow.PROJECTILE_TYPE

    def get_attack_power(self):
        return self.__class__.ATTACK_POWER

    def is_to_flip_horizontally(self, direction):
        if direction == 1 or direction == 0 or direction == 7:
            return True
        return False

    def is_to_flip_vertically(self, direction):
        return False

