import curses
from GameObject import GameObject
from GameObject import AssetsStore
from GameObject import SceneObject


def init(Scene):
    score = 0
    cat_object = GameObject('asset_cat','object_cat')
    roof_object = GameObject('asset_roof','object_roof')
    Scene.add_object(cat_object)
    Scene.add_object(roof_object)
    screen = curses.initscr()
    screen.keypad(1)
    screen.addstr(0,0, 'Hello')
    screen.refresh()
    curses.napms(3000)
    curses.endwin()
    print("Window ended.")

def receive_user_input():
    player = curses.KEY_ENTER



def game_over():
    pass

def loop():
    pass
#user_input = receive_user_input()
#controller_step(user_input)
#view_step
# clear screen
    # display the cat
    # display the roof
    # display the score
    # listen to keypress event
    # respond to keypress event
    # stop the game if the cat hits the roof

def controller_step():
    event = receive_user_input()
    pass

def view_step():
    asset = AssetsStore()
    object = SceneObject()
    object.get_object()
    for object in AssetsStore.get_asset():
        object.addstr()


def main():
    main_scene = SceneObject()
    init(main_scene)



while not game_over:
 loop()

if __name__ == '__main__':
    main()

