import curses
import random
from GameObject import AssetsStore
from GameObject import SceneObject

screen = curses.initscr()
curses.curs_set(0)
sh, sw = screen.getmaxyx()
win = curses.newwin(sh, sw, 0, 0)
win.keypad(1)
curses.curs_set(1)
key = curses.KEY_ENTER
game_objects = SceneObject()


screen.addstr(1, 5, )

screen.refresh()
curses.napms(2000)
curses.endwin()






#objects_game = {'cat': [' ^---^', '( o.o )', '/     \\', '(  _  )', ' uu-uu'],
#                'roof': ['ххх  ххх ', 'ххх  ххх', 'ххх  ххх', 'ххх  ххх', 'ххх  ххх', 'ххх  ххх']}

#cat_x = objects_game.get('cat')
#for x in cat_x:
#    print(x)

#roof_x = objects_game.get('roof')
#for y in roof_x:
#    print(y)

#for keys, values in object_cat.items():
    #print(values)


#roof_object = {'roof': ['ххх','ххххххх', 'ххх  ххх ', 'ххх  ххх', 'ххх  ххх', 'ххх  ххх', 'ххх  ххх']}
#for roof, value in enumerate(roof_object):
    ##print(roof, value)

# keys, values in roof_object.items():
    #print(values)







#for x in roof_object:
    #print(x)


#cat_object = {'cat': ['{} {} {} {} {}'.format('fff','fgf','fkf','fjf','ffj')]}

#for keys, values in cat_object.items():
    #print(values)


#cat_user = ['^---^', '( o.o )', '/     \\', '/(  _  )\\', '^^^ ^^^']
#user_get = ('{},{},{},{},{}'.format(*cat_user))
#for x in user_get:
    #print(x)






