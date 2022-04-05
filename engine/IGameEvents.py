import pygame

class IGameEvents(object):
    def __init__(self):
        pass

    def on_before_exit(self):
        pass

    def on_after_exit(self):
        pass

    def on_process_input(self):
        pass

    def get_pressed_keys(self):
        return pygame.key.get_pressed()

    def on_pygame_event(self,e):
        pass
