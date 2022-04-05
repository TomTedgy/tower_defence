import engine
import Arrow
class MyProjectileFactory(engine.ProjectileFactory.ProjectileFactory):
    def __init__(self):
        super().__init__()

    @staticmethod
    def create_projectile(proj_type, igame, groups, creating_sprite, direction, x, y):
        if proj_type == "arrow":
            return Arrow.Arrow(igame,groups,creating_sprite, direction, x,y)

        return None