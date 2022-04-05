import os

import pygame


class cell_list_provider(object):
    def __init__(self, scale):
        self._scale = scale
        self._cell_list = []

    def provide(self):
        pass

    def get_scale (self):
        return self._scale


class directory_cell_list_provider(cell_list_provider):
    def __init__(self, directory , filter, scale, flip_horizontally, flip_vertically):
        super().__init__(scale)

        self._flip_horizontally = flip_horizontally
        self._flip_vertically = flip_vertically

        self._files = [os.path.join(directory,f) for f in os.listdir(directory) if filter in f]
        self._surface = pygame.image.load(self._files[0])

        self._sprite_width = self._surface.get_width()
        self._sprite_height = self._surface.get_height()
        self._frames_per_animation = len(self._files)


        self._cell_list = self._create_cell_list(self._files)

    def _create_cell_list(self, files):
        cell_list = []
        for f in files:
            s = pygame.image.load(f)
            s = pygame.transform.scale(s, (s.get_width()/ self._scale, s.get_height() / self._scale))
            if self._flip_vertically or self._flip_horizontally :
                s = pygame.transform.flip(s, self._flip_horizontally , self._flip_vertically)
            cell_list.append(s)
        return cell_list

    def provide(self):
        return self._cell_list


class sprite_sheet_cell_list_provider(cell_list_provider):
    def __init__(self,filename,x,y,sprite_width,sprite_height, frames_per_animation, scale):
        super().__init__(scale)
        self._sprite_width = sprite_width
        self._sprite_height = sprite_height
        self._frames_per_animation = frames_per_animation

        self._animation_start_x = x
        self._animation_start_y = y

        self._current_filename = filename
        self._mainsheet = pygame.image.load(self._current_filename)


        self._cell_list = self._create_cell_list(self._animation_start_x, self._animation_start_y)

    def _create_cell_list(self, start_x, start_y):
        cell_list = []
        w = self._sprite_width
        h = self._sprite_height
        for x in range(start_x, start_x + (self._frames_per_animation * self._sprite_width), self._sprite_width):
            y = start_y
            surface = pygame.Surface((w, h))
            surface.blit(self._mainsheet, (0, 0), (x, y, w, h))

            # scaling
            surface = pygame.transform.scale(surface, (w / self._scale, h / self._scale))

            # if self._mirror:
            #     surface = pygame.transform.flip(surface, True, False)
            cell_list.append(surface)
        return cell_list

    def provide(self):
        return self._cell_list


class many_image_files_cell_list_provider(cell_list_provider):
    def __init__(self, scale):
        super().__init__(scale)
