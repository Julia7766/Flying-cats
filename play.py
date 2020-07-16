import curses
from GameObject import GameObject
from GameObject import AssetStore
from GameObject import Scene


def init(scene_to_init):
    score = 0
    cat = GameObject('cat_asset','cat')
    roof = GameObject('roof_asset','roof')
    scene_to_init.add_object(cat)
    scene_to_init.add_object(roof)

    return clear_screen()


def clear_screen():
    screen = curses.initscr()
    screen.keypad(1)
    screen.addstr(0, 0, 'Hello')
    screen.refresh()
    curses.napms(3000)
    return screen
    #curses.endwin()


def receive_user_input():
    player = curses.KEY_ENTER

def game_over():
    pass

def loop():
    pass
#user_input = receive_user_input
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
    pass

def view_step(scene_to_draw, asset_store, canvas):
    objects_to_draw = scene_to_draw.get_objects()
    for item in objects_to_draw:
        asset_name = item.get_asset_name()
        asset = asset_store.get_asset(asset_name)
        draw_in_curses(canvas, asset, item)

def draw_in_curses(canvas, asset, item):
    item_pos = item.get_position()
    for rownum, line in enumerate(asset):
        canvas.addstr(item_pos[1] + rownum, item_pos[0], line)
        canvas.refresh()





def main():
    main_scene = Scene()
    asset_store = AssetStore()
    canvas = init(main_scene)
    view_step(main_scene,asset_store, canvas)
    while not game_over:
        loop()


if __name__ == '__main__':
    main()

