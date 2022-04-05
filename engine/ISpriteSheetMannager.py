import pygame
class ISpriteSheetMannager(object):
    def __init__(self, filename,frames_per_animation):
        self._filename = filename
        self._frames_per_animation = frames_per_animation

        self._mainsheet = pygame.image.load(self._filename)
        self._size = self._mainsheet.get_size()
        # single drawing , height and width
        self._height = int(self._size[1] / 8)
        self._width = int(self._size[0] / 28)

        self._cell_list = self._create_cell_list()


    def get_cells(self, row, col, number_of_frames):
        ret = []


        return ret

    def _create_cell_list(self):
        cell_list = []
        start_x = 128 * 4
        start_y = 128 * 7
        w = self._width
        h = self._height
        for x in range(start_x, start_x + (self._frames_per_animation * self._width), self._width):
            y = start_y
            surface = pygame.Surface((w, h))
            surface.blit(self._mainsheet, (0, 0), (x, y, w, h))
            # if self._mirror:
            #     surface = pygame.transform.flip(surface, True, False)
            cell_list.append(surface)
        return cell_list
