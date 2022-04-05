import IAnimationSprite
import ISprite


class tile_map(ISprite.ISprite):
    def __init__(self,igame,group,width,height,tile_width, tile_height, cells_providers, map_index, the_map):
        super().__init__(igame,group,width,height,0,0)
        self._tilemap = []

        self._map_translator = map_translator(map_index,cells_providers)

        self._width = width
        self._height = height

        self._tile_width = tile_width
        self._tile_height = tile_height

        self._number_of_tiles_x = int(width/tile_width)
        self._number_of_tiles_y = int(height/tile_height)

        self._cells_providers = cells_providers

        x = 0
        y = 0
        for line in the_map:
            line = line.replace('\n' , '')
            current_tile_line = []
            for t in line:
            # gets here, doesnt work for some reason, trying to figure it out
                current_tile = tile(igame, group, self._map_translator.get_cell_provider_for_map_key(t), self._tile_width, self._tile_height,
                     x * self._tile_width, y * self._tile_height)
                x += 1
                current_tile_line.append(current_tile)
            x = 0
            y += 1
            self._tilemap.append(current_tile_line)

    def render(self,screen):
        for line in self._tilemap:
            for t in line:
                t.render(screen)




class tile(IAnimationSprite.IAnimationSprite):
    def __init__(self, igame, group, cells_provider, tile_width, tile_height, start_x, start_y):
        # igame, group, cells_provider, frames_per_animation, sprite_width, sprite_height, start_x , start_y,  millis_per_iteration
        super().__init__(igame, group,cells_provider,1,tile_width,tile_height,start_x,start_y,9000)



class map_translator(object):
    def __init__(self, index,  cells_providers):
        #index is a dictionary with a value from map to key in cells_providers
        self._index = index
        self._cells_providers = cells_providers

    def _translate_map_character_to_cell_provider_key(self, map_character):
        if map_character in self._index:
            return self._index[map_character]
        # gets here and returns None
        return None

    def get_cell_provider_for_map_key(self, map_key):

        cell_provider_key = self._translate_map_character_to_cell_provider_key(map_key)

        cell_provider = self._cells_providers[cell_provider_key]
        return cell_provider

