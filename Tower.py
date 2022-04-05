import engine
import pygame

class Tower():
    def __init__(self,x,y):
        self._proj_x = x
        self._proj_y = y
        self._width = 0
        self._height = 0
        #not sure
        self.tower_images = []
        self._dmg = 1

        self._is_tower_selected = False

    def render(self, screen):
        #need to blit images with self.tower_imges
        pass

    def draw_range(self,screen):
        # if pressed on tower , selected , draw range circle
        #if selected:
        # pasted google
        if self._is_tower_selected:
            pass
            # draw circle
            #pygame.draw.circle
            #blit

    def update(self):
        pass



class ArcherTower(Tower):
    def __init__(self,x,y):
        super().__init__(x,y)

        pass

