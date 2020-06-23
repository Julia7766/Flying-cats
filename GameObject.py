
class GameObject:
    def __init__(self, asset_name, object_name):
        self.x = 0
        self.y = 0
        self.speed_y = 0
        self.speed_x = 0
        self.asset_name = asset_name
        self.object_name = object_name

    def set_position(self,x,y):
        self.x = x
        self.y = y

    def get_position(self):
       return self.x, self.y

    def set_speed_y(self,speed_y):
        self.speed = speed_y

    def get_speed_y(self):
        return self.speed_y


class AssetsStore:
    def __init__(self):
        self.asset_object = {'cat': [' ^---^', '( o.o )', '/     \\', '(  _  )', ' uu-uu'],
                             'roof': ['ххх  ххх ', 'ххх  ххх', 'ххх  ххх', 'ххх  ххх', 'ххх  ххх', 'ххх  ххх']
                             }

    def get_asset(self,asset_name):
        return self.asset_object[asset_name]


class SceneObject:
    def __init__(self):
        self.game_objects = []

    def add_object(self, game_objects):
        self.game_objects.append(game_objects)

    def get_object(self):
        return self.game_objects

