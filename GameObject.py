
class GameObject:
    def __init__(self, asset_name, object_name):
        self.x = 0
        self.y = 0
        self.speed_y = 0
        self.speed_x = 0
        self.asset_name = asset_name
        self.object_name = object_name

    def set_position(self, x,y):
        self.x = x
        self.y = y

    def get_position(self):
       return self.x, self.y

    def set_speed_y(self, speed_y):
        self.speed = speed_y

    def get_speed_y(self):
        return self.speed_y

    def get_asset_name(self):
        return self.asset_name


class AssetStore:
    def __init__(self):
        self.assets = {'cat_asset': [' ^---^', '( o.o )', '/     \\', '(  _  )', ' uu-uu'],
                             'roof_asset': ['ххх  ххх ', 'ххх  ххх', 'ххх  ххх', 'ххх  ххх', 'ххх  ххх', 'ххх  ххх']
                       }

    def get_asset(self,asset_name):
        if asset_name in self.assets.keys():
            return self.assets[asset_name]
        else:
            return None


class Scene:
    def __init__(self):
        self.game_objects = []

    def add_object(self, new_object):
        if isinstance(new_object, GameObject):
            self.game_objects.append(new_object)

    def get_objects(self):
        return self.game_objects

