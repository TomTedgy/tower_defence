import helpers
import IAnimationSprite

class AutomaticFiringUnit(IAnimationSprite.IAnimationSprite):
    def __init__(self, igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration , projectile):
        super().__init__(igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration)

        self._projectile = projectile
        self._range = self._projectile.get_range()
        self._firing_freq = self._projectile.get_firing_freq()
        self._target = None
        # auto firing
        self._old_arrow_time = 0
        self._elapsed_time = 0


    def get_target(self):
        return self._target

    def set_target(self,target):
        self._target = target

    def update(self, dt):

        self._elapsed_time += dt

        if self._elapsed_time - self._old_arrow_time > self._firing_freq:
            if self._target:
                self.set_animation(True)
                self.set_one_time_animation(True, None)
                target_direction = helpers.Helpers.get_angle_between_two_points(self._pos_x , self._pos_y, self._target._pos_x , self._target._pos_y)
                self._old_arrow_time = self._elapsed_time
                #proj_type ,  igame , groups , creating_sprite,direction , x,y
                projectile = self._igame.get_proj_factory().create_projectile(self._projectile.get_type(),self._igame, self.groups(), self, target_direction, self._pos_x, self._pos_y)
                self._igame.add_projectile(self, projectile)
            else:
                self._target = self._igame.acquire_target(self, self._range)
                if self._target:
                    self._target.subscribe_to_on_after_death(self)


        super().update(dt)


    def render(self, screen):
        super().render(screen)

    # event handlers
    def on_after_death(self, sprite):
        if sprite == self._target:
            self._target = None