import ISprite
import pygame
import IGameEvents
import helpers

class IGame(object):
    def __init__(self, fps, width, height, bg_color_rgb,scale = 1):
        self._width = width
        self._height = height
        self._bg_color = bg_color_rgb

        self._group_player = pygame.sprite.Group()
        self._group_game = pygame.sprite.Group()
        #self._group_enemies =
        self._group_projectiles = pygame.sprite.Group()

        self._group_enemies = pygame.sprite.Group()
        self._enemy_list = []



        self._scale = scale

        self._all_groups = [self._group_game, self._group_enemies, self._group_player]

        self._game_events = None
        self._sprites = []
        self._running = True
        self._clock = pygame.time.Clock()
        self._fps = fps
        self._old_ticks = 0
        self._screen = pygame.display.set_mode((width, height))
        self._proj_factory = None

        # will keep the currently selected sprite
        self._selected_sprite = None

    def get_proj_factory(self):
        return self._proj_factory



    def acquire_target(self , requesting_sprite , sprite_firing_range):
        x , y = requesting_sprite._pos_x , requesting_sprite._pos_y

        for s in self._enemy_list:
            if helpers.Helpers.intersects(s.rect, sprite_firing_range, (x,y) ):
                return s
        return None


    def set_proj_factory(self, proj_factory):
        self._proj_factory = proj_factory

    def report_moving_sprite(self, moving_sprite):
        ret = []
        # other_groups = [g for g in self._all_groups if g not in moving_sprite.groups()]
        # _delete = False
        # _colided = None
        # for other_group in other_groups:
        #     ret += pygame.sprite.spritecollide(moving_sprite, other_group, _delete, _colided)
        for s in self._sprites:
            if s is moving_sprite:
                pass
            else:
                if moving_sprite.rect.colliderect(s.rect):
                    ret.append(s)



        print(len(ret))


    def init(self, game_events):
        pygame.init()
        self._game_events = game_events

    def check_collision(self, sprite, is_single_collision = True):
        ret = []

        for s in self._enemy_list:
            if s == sprite:
                continue
            else:
                if s == sprite.get_firing_sprite():
                    continue
                if s.rect.colliderect(sprite.rect):
                    ret.append(s)
                    if is_single_collision:
                        break

        return ret

    def game_loop(self):
        while self._running:
            # run in delay of fps
            self._clock.tick(self._fps)

            # input
            self.process_input()

            # gets the number of milliseconds elapsed after calling 'pygame.init()'
            ticks = pygame.time.get_ticks() * 1.0

            # update
            dt = (ticks - self._old_ticks) / 1000
            self.update(dt)

            # draw
            self.render()

            # save for next iteration
            self._old_ticks = ticks


        self._game_events.on_after_exit()

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._game_events.on_before_exit()
                self._running = False
            else:
                self._game_events.on_pygame_event(event)

        self._game_events.on_process_input()

    def render(self):
        self._screen.fill(self._bg_color)


        for s in self._sprites:
            if isinstance(s, ISprite.ISprite):
                s.render(self._screen)



        pygame.display.flip()

    def add_sprite(self, s):
        if isinstance(s , ISprite.ISprite):
            self._sprites.append(s)

            # tell the sprite to tell me, when its dead.
            s.subscribe_to_on_after_death(self)

    def remove_sprite(self , s):
        if s in self._sprites:
            self._sprites.remove(s)

    def update(self, dt):
        for s in self._sprites:
            if isinstance(s, ISprite.ISprite):
                s.update(dt)

    def add_projectile(self, firing_sprite , projectile):
        self.add_sprite(projectile)

    def kill(self):
        pass

    #event handlers

    def on_after_death(self, sprite):
        self.remove_sprite(sprite)

    def on_after_end_of_path(self, sprite):
        # todo : remove hp from player
        sprite.report_on_after_death(sprite)

    def on_selectablesprite_selected(self,selectable_sprite):
        self._selected_sprite = selectable_sprite