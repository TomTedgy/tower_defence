import engine
import pygame
import Arrow




class Enemy(engine.IEightDirAnimationSprite.IEightDirAnimationSprite):
    def __init__(self,igame,group,path,sprite_width, sprite_height, speed_x, speed_y,
                     cells_providers,millis_per_iteration, hp):

        self._path = path

        self._hp = hp
        self._full_hp = hp

        self._is_dying = False


        start_x, start_y, direction, is_last = self.get_next_point_in_path(0)
        self.set_direction(direction)

        super().__init__(igame,group,sprite_width, sprite_height,start_x,start_y, speed_x, speed_y,cells_providers,  millis_per_iteration)


        self._current_x = start_x
        self._current_y = start_y
        self._target_x, self._target_y,direction , is_last= self.get_next_point_in_path(self._current_direction)
        self.set_direction(direction)

    def die(self):
        self._is_dying = True
        self.stop_moving()
        self.set_is_one_time_animation(True, self.on_animation_done)
        self.begin_death()


    def report_collision_with(self, colliding):
        if colliding:
            self.add_hp(-1 * colliding.get_attack_power())

        #todo: check groups
        super().report_collision_with(colliding)



    def is_to_flip_horizontally(self, direction):
        if direction == 1 or direction == 0 or direction == 7:
            return True
        return False

    def is_to_flip_vertically(self, direction):
        return False

    def begin_death(self):
        pass


    def get_next_point_in_path(self, old_direction):
        direction = old_direction
        is_last = False
        if len(self._path) == 0:
            x = -1
            y = -1
            is_last = True
        elif len(self._path) == 1:
            x = self._path[0][0]
            y = self._path[0][1]
            self._path = []
            is_last = True
            direction = engine.helpers.Helpers.get_direction_between_two_points(x, y, x, y, old_direction)
        else:
            x = self._path[0][0]
            y = self._path[0][1]

            self._path = self._path[1:]

            x2 = self._path[0][0]
            y2 = self._path[0][1]

            direction = engine.helpers.Helpers.get_direction_between_two_points(x,y,x2,y2,old_direction)


        return x, y -100 , direction , is_last

    def add_hp(self,num):
        self._hp += num
        if self._hp <= 0:
            self.die()

    def update(self,dt):
        if not self._is_dying:
            self.move_in_path(dt)
            # self.stop_moving()
            self._pos_x = self._current_x
            self._pos_y = self._current_y
        super().update(dt)

    def render(self, screen):
        super().render(screen)
        rgb = 0,255,0
        if self._hp * 2 < self._full_hp:
            rgb = 255,0,0

        pygame.draw.rect(screen, rgb, pygame.Rect(self._pos_x, self._pos_y,
                                                  int(self._sprite_width * (self._hp / self._full_hp)),
                                                  20))

    def move_in_path(self,dt):
        self.set_moving(True)
        distance = engine.helpers.Helpers.distance_between_two_points(self._current_x, self._current_y, self._target_x, self._target_y)

        if distance < 1:
            self._current_x = self._target_x
            self._current_y = self._target_y
            self._target_x, self._target_y , direction , is_last= self.get_next_point_in_path(self._current_direction)

            if self._target_x == -1 and self._target_y == -1:
                self._target_x = self._current_x
                self._target_y = self._current_y

            else:
                self.set_direction(direction)

            if is_last:
                self._igame.on_after_end_of_path(self)
        # dx,dy = engine.helpers.Helpers.move_between_two_points(self._current_x, self._current_y, self._target_x, self._target_y, dt)
        # if self._current_x > self._target_x:
        #     dx = -dx
        # if self._current_y > self._target_y:
        #     dy = -dy

        dx, dy = engine.helpers.Helpers.linear_move_between_two_points(self._current_x, self._current_y, self._target_x, self._target_y, dt, self._speed_x, self._speed_y)

        self._current_x += dx
        self._current_y += dy

    def on_animation_done(self):
        self.report_on_after_death(self)

    # theses functions need to somehow change cells provider to "run" instead of walk
    def run(self):
        pass

    def jump(self):
        pass

    def attack(self):
        pass


class ScorpionEnemy(Enemy):
    SPEED_X = 100
    SPEED_Y = 100
    SPRITE_WIDTH = 192
    SPRITE_HEIGHT = 226
    MILLIS_PER_ITERATION = 500
    HP = 1
    SCORPION_SCALE = 2
    def __init__(self,igame,group,path):

        base_dir = './assets/2d-monster-sprites/PNG/1/'

        cells_providers ={k:engine.cell_list_provider.directory_cell_list_provider(base_dir, 'walk',igame._scale * self.__class__.SCORPION_SCALE, self.is_to_flip_horizontally(k) , self.is_to_flip_vertically(k)) for k in range(8)}
        for i in range(8):
            for cell_index in range(len(cells_providers[i]._cell_list)):
                c = cells_providers[i]._cell_list[cell_index]


        death_cells_provider = engine.cell_list_provider.directory_cell_list_provider(base_dir, 'die',igame._scale * self.__class__.SCORPION_SCALE, False, False)

        self._death_cells_provider = death_cells_provider


        super().__init__(igame,group,path,self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT,  self.__class__.SPEED_X,self.__class__.SPEED_Y,
                     cells_providers, self.__class__.MILLIS_PER_ITERATION, self.__class__.HP)

    def render(self, screen):
        super().render(screen)

        # theses functions need to somehow change cells provider to "run" instead of walk

    def update(self,dt):
        super().update(dt)

    def begin_death(self):
        cell_list = self._death_cells_provider.provide()
        self.set_cell_list(cell_list)


    def run(self):
        pass

    def jump(self):
        pass

    def attack(self):
        pass

class WizardEnemy(Enemy):
    SPEED_X = 100
    SPEED_Y = 100
    SPRITE_WIDTH = 388
    SPRITE_HEIGHT = 338
    MILLIS_PER_ITERATION = 500
    HP = 2
    WIZARD_SCALE = 2
    def __init__(self,igame, group,path):
        base_dir = './assets/2d-monster-sprites/PNG/2/'

        cells_providers ={k:engine.cell_list_provider.directory_cell_list_provider(base_dir, 'walk',igame._scale * self.__class__.WIZARD_SCALE, self.is_to_flip_horizontally(k) , self.is_to_flip_vertically(k)) for k in range(8)}

        death_cells_provider = engine.cell_list_provider.directory_cell_list_provider(base_dir, 'die',igame._scale* self.__class__.WIZARD_SCALE, False, False)

        self._death_cells_provider = death_cells_provider

        super().__init__(igame, group, path, self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT,
                         self.__class__.SPEED_X, self.__class__.SPEED_Y,
                         cells_providers, self.__class__.MILLIS_PER_ITERATION,self.__class__.HP)

    def begin_death(self):
        cell_list = self._death_cells_provider.provide()
        self.set_cell_list(cell_list)

    def render(self, screen):
        super().render(screen)

        # theses functions need to somehow change cells provider to "run" instead of walk

    def run(self):
        pass

    def jump(self):
        pass

    def attack(self):
        pass




class GoblinEnemy(Enemy):
    SPEED_X = 100
    SPEED_Y = 100
    SPRITE_WIDTH = 331
    SPRITE_HEIGHT = 299
    MILLIS_PER_ITERATION = 500
    HP = 4
    GOBLIN_SCALE = 2
    def __init__(self,igame, group,path):
        base_dir = './assets/2d-monster-sprites/PNG/3/'

        cells_providers ={k:engine.cell_list_provider.directory_cell_list_provider(base_dir, 'walk',igame._scale * self.__class__.GOBLIN_SCALE, self.is_to_flip_horizontally(k) , self.is_to_flip_vertically(k)) for k in range(8)}

        death_cells_provider = engine.cell_list_provider.directory_cell_list_provider(base_dir, 'die',igame._scale * self.__class__.GOBLIN_SCALE, False , False)

        self._death_cells_provider = death_cells_provider


        super().__init__(igame, group, path, self.__class__.SPRITE_WIDTH, self.__class__.SPRITE_HEIGHT,
                         self.__class__.SPEED_X, self.__class__.SPEED_Y,
                         cells_providers, self.__class__.MILLIS_PER_ITERATION, self.__class__.HP)




    def begin_death(self):
        cell_list = self._death_cells_provider.provide()
        self.set_cell_list(cell_list)

    def render(self, screen):
        super().render(screen)

        # theses functions need to somehow change cells provider to "run" instead of walk

    def run(self):
        pass

    def jump(self):
        pass

    def attack(self):
        pass