import ArcherBuilding
import Archers
import Enemy
import MyProjectileFactory
import TableButton
import TableMenu
import engine
import pygame
import os
import Button

class MyGameEvents(engine.IGameEvents.IGameEvents):
    def __init__(self, game):
        super().__init__()
        if isinstance(game, MyGame):
            self._game = game
        else:
            raise Exception("Invalid , mygame")

    def on_before_exit(self):
        print("cleaning up")



    def on_pygame_event(self,e):
        position = pygame.mouse.get_pos()


        if e.type == pygame.MOUSEBUTTONUP:
            self._game.on_mouse_click(position)




class MyGame(engine.IGame.IGame):
    def __init__(self, fps, width ,height ,bg_color_rgb, scale):
        super().__init__(fps, width,height,bg_color_rgb, scale)
        self._game_events = MyGameEvents(self)

        self._elapsed = 0
        self._selection = None
        animation_start_x = 128 * 4
        animation_start_y = 128 * 7
        start_x = 100
        start_y = 100
        sprite_width = 128
        sprite_height = 128
        frames_per_animation = 4
        millis_per_iteration = 500
        filename = "./assets/jojo.png"
        speed_x = 100
        speed_y = 100
        tile_width = 1920
        tile_height = 1080
        igame = self
        self._enemy_counter = 0
        self._enemies = ['scorpion', 'wizard', 'goblin']



        self._enemy_path = [(1299, 232), (1267, 234), (1243, 225), (1202, 209), (1187, 188), (1169, 173), (1135, 170), (1109, 171), (1065, 165), (1022, 168), (985, 170), (945, 175), (919, 180), (892, 192), (876, 207), (863, 223), (843, 242), (836, 259), (826, 296), (818, 327), (804, 361), (766, 377), (741, 396), (703, 404), (662, 405), (601, 379), (596, 359), (569, 343), (532, 351), (483, 370), (469, 401), (425, 439), (418, 498), (403, 527), (385, 546), (314, 567), (250, 573), (165, 573), (115, 574), (85, 576), (74, 576)]

        # create player and add it to sprites

        the_map = self._get_map()
        map_index = self._get_map_index()
        self._tiles_cells_provider = self._get_tiles_providers(tile_width, tile_height)


        self._tilemap = engine.TileMap.tile_map(igame, self._group_game, width, height, tile_width, tile_height, self._tiles_cells_provider, map_index, the_map)
        self.add_sprite(self._tilemap)

        self._menu = TableMenu.TableMenu(igame,self._group_game, 1000, 500)
        self.add_sprite(self._menu)

        button1 = TableButton.TableButton_Level1ArcherBuilding(igame, self._group_game, self._menu)
        button2 = TableButton.TableButton_Level2ArcherBuilding(igame, self._group_game, self._menu)
        button3 = TableButton.TableButton_Level3ArcherBuilding(igame, self._group_game, self._menu)
        self._game_buttons = [button1 , button2 , button3]

        self.set_proj_factory(MyProjectileFactory.MyProjectileFactory())

        self.set_menu_buttons_to_game_menu_buttons()


    def set_menu_buttons_to_game_menu_buttons(self):
        #self._menu.clear_all()
        for button in self._game_buttons:
            self.add_sprite(button)


    def add_simple_archer_level1_building(self, position):

        self._simple_archer = Archers.SimpleArcher(self, self._group_player, 0,0)
        self.add_sprite(self._simple_archer)

        x = position[0] - ArcherBuilding.ArcherBuilding_Level1.SPRITE_WIDTH / (2*4)
        y = position[1] - ArcherBuilding.ArcherBuilding_Level1.SPRITE_HEIGHT / (2*4)
        self._archer_building = ArcherBuilding.ArcherBuilding_Level1(self, self._group_player,x,y)
        self._archer_building.add_unit(self._simple_archer)
        self.add_sprite(self._archer_building)


    def add_simple_archer_level2_building(self, position):

        self._level_2_archer = Archers.Level2Archer(self, self._group_player, 0,0)
        self.add_sprite(self._level_2_archer)

        x = position[0] - ArcherBuilding.ArcherBuilding_Level2.SPRITE_WIDTH / (2*4)
        y = position[1] - ArcherBuilding.ArcherBuilding_Level2.SPRITE_HEIGHT / (2*4)
        self._archer_building = ArcherBuilding.ArcherBuilding_Level2(self, self._group_player,x,y)
        self._archer_building.add_unit(self._level_2_archer)
        self.add_sprite(self._archer_building)

    def add_simple_archer_level3_building(self, position):

        self._level_3_archer = Archers.Level3Archer(self, self._group_player, 0,0)
        self._level_3_archer_2 = Archers.Level3Archer(self, self._group_player, 0,0)

        self.add_sprite(self._level_3_archer)
        self.add_sprite(self._level_3_archer_2)

        x = position[0] - ArcherBuilding.ArcherBuilding_Level3.SPRITE_WIDTH / (2*4)
        y = position[1] - ArcherBuilding.ArcherBuilding_Level3.SPRITE_HEIGHT / (2*4)
        self._archer_building = ArcherBuilding.ArcherBuilding_Level3(self, self._group_player,x,y)
        self._archer_building.add_unit(self._level_3_archer)
        self._archer_building.add_unit(self._level_3_archer_2)
        self.add_sprite(self._archer_building)




    def update(self,dt):
        self._elapsed += dt


        if self._elapsed > 3:
            self._elapsed = 0
            self.make_enemy(self._enemies[self._enemy_counter % 3], self._enemy_path[:])
            self._enemy_counter += 1
            # for s in self._sprites:
            #     if isinstance(s, Enemy.Enemy):
            #         s.add_hp(-1)

            # self.make_enemy("scorpion" , self._enemy_path[:])
        super().update(dt)


    def make_enemy(self,name, path ):
        enemy = None
        if name == "scorpion":
            enemy = Enemy.ScorpionEnemy(self, self._group_enemies, path)
        elif name == "wizard":
            enemy = Enemy.WizardEnemy(self, self._group_enemies, path)
        elif name == "goblin":
            enemy = Enemy.GoblinEnemy(self, self._group_enemies, path)

        if enemy:
            self.add_sprite(enemy)
            self._enemy_list.append(enemy)

    def _get_map_index(self):
        # index = {}
        #147 + 37
        # for k in range(9):
        #     index[k] = 'road_{}.png'.format(k+1)
        # return index
        index = {}
        for k in range(1):
            index[str(k)] = 'game_background_1.png'

        return index
      # return {str(k):'road_{}.png'.format(k+1) for k in range(10)}



    def _get_map(self):
        base_dir = './assets/'
        map_name = 'level1.map'
        fin = open(os.path.join(base_dir,map_name),'r')
        lines = fin.readlines()

        return lines

    def _get_tiles_providers(self, tile_width, tile_height):
        base_dir = './assets/td-tilesets/tower-defense-game-tile-set-pack-2/PNG/game_background_1/default_background/'
        files = os.listdir(base_dir)
        cells_providers = {}
        for f in files:
            p = os.path.join(base_dir, f)
            cells_providers[f] = engine.cell_list_provider.sprite_sheet_cell_list_provider(
            p,
            0, 0, tile_width, tile_height, 1, self._scale)



        return cells_providers

    def start(self):
        super().init(self._game_events)
        self.game_loop()

    # events handlers
    def on_mouse_click(self, position):
        x = position[0]
        y = position[1]
        handled = False
        if x > self._menu._pos_x and x < self._menu._pos_x + self._menu.SPRITE_WIDTH:
            if y > self._menu._pos_y and y < self._menu._pos_y + self._menu.SPRITE_HEIGHT:
                self._menu.on_mouse_click(position)
                handled = True
        if not handled:
            if self._selection:
                if self._selection == TableButton.TableButton_Level1ArcherBuilding.SELECTION:
                    self.on_selection_change(None)
                    self.add_simple_archer_level1_building(position)
                elif self._selection == TableButton.TableButton_Level2ArcherBuilding.SELECTION:
                    self.on_selection_change(None)
                    self.add_simple_archer_level2_building(position)
                elif self._selection == TableButton.TableButton_Level3ArcherBuilding.SELECTION:
                    self.on_selection_change(None)
                    self.add_simple_archer_level3_building(position)
            else:
                # selectablesprite will have the function on_selected..  therefore will be checking the correct sprite.
                for sprite in [s for s in self._sprites if hasattr(s, "on_selected")]:
                    is_collided = engine.helpers.Helpers.is_colliding(x,y,1,1,sprite._pos_x, sprite._pos_y, sprite._sprite_width,sprite._sprite_height)
                    if is_collided:
                        sprite.on_selected()
                        break


    def on_selectablesprite_selected(self, selectable_sprite):
        super().on_selectablesprite_selected(selectable_sprite)
        self._menu.clear_all()
        self._menu.add_buttons(selectable_sprite._buttons)

    def on_selection_change(self, selection):
        self._selection = selection


def main():
    width = 1366
    height = 738
    animation_width = 1920
    animaton_height = 1080
    # all the graphics are for 1920 x 1080
    scale = animation_width / width
    if animaton_height / height > scale:
        scale = animaton_height / height

    g = MyGame(60 , 1366 , 738 , (100,100,100), scale)
    g.start()



if __name__ == '__main__':
    main()