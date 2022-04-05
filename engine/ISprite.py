import IGame
import pygame
class ISprite(pygame.sprite.Sprite):
    def __init__(self,igame,group, sprite_width, sprite_height,start_x , start_y):
        super().__init__(group)
        self._igame = igame

        self._sprite_height = sprite_height
        self._sprite_width = sprite_width



        self._pos_x = start_x
        self._pos_y = start_y

        self.rect = pygame.Rect(self._pos_x, self._pos_y, self._sprite_width, self._sprite_height)
        # Event Listeners
        self._on_after_death_subscribers = []

    # subscribe to event
    def subscribe_to_on_after_death(self, subscriber):
        if subscriber and subscriber not in self._on_after_death_subscribers:
            self._on_after_death_subscribers.append(subscriber)

    def report_on_after_death(self, sprite):
        for subscriber in self._on_after_death_subscribers:
            subscriber.on_after_death(sprite)

    # event invokers
    def report_collision_with(self, colliding):
        if colliding and isinstance(colliding, ISprite):

            colliding.on_after_collision(self)
            self.on_after_collision(colliding)

    # event handlers
    def on_after_collision(self, collided_with):
        return None

    def on_after_death(self, sprite):
        pass

    def get_attack_power(self):
        return 0

    def get_firing_sprite(self):
        return None
    # def _collide(self, other_sprite):
    #     if not isinstance(other_sprite, ISprite):
    #         return False
    #     return other_sprite._pos_x > self._pos_x and other_sprite._pos_x < self._pos_x + self._sprite_width and\
    #         other_sprite._pos_y > self._pos_y and other_sprite._pos_y < self._pos_y + self._sprite_height





    def update(self, dt):
        pass

    def render(self, screen):
        pass