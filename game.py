import sys, os
import curses

#This is model game

#menu status
def menu_game():
    menu = 'Добро пожаловать в игру "Летающие коты"'
    return print(menu)

#rules of the game: набор правил,по которым контроллер обрабатывает игровую обстановку
def rules_game():
    rule = 'Управляйте летающими котами, уворачиваясь от препятствий в виде крыш домов.'
    return print(rule)

#object status (cat, roof, field's game)
class CatObject:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed_y = 0

    def set_position(self,x,y):
        self.x = x
        self.y = y

    def get_position(self):
       return self.x, self.y

    def set_speed_y(self,speed_y):
        self.speed = speed_y

    def get_speed_y(self):
        return self.speed_y

class RoofObject:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def set_position(self,x,y):
        self.__x = x
        self.__y = y

    def get_position(self):
       return self.__x, self.__y

class Player:
    def __init__(self):
        pass

class FieldObject:
    def __init__(self):
        self.width = 0
        self.height = 0

#This is controller game
def init():
#prepare all game set

def loop():
user_input = receive_user_input()
controller_step(user_input)
view_step()

main():
init()

while not game_over:
loop()
#main loop - event handling, game status update, update screen
def main():
   pass
#game process

#This is view


cat_game = '''
               ^---^  
              ( o.o )   
              /     \\  
             /(  _  )\\ 
              ^^^ ^^^   '''


roof_object = '''
                   ххх
                 ххххххх
               хххххххххххх
            хххххххххххххххххх
              хххххххххххххх
                хххх  хххх              
                хххх  хххх
                хххх  хххх
                хххх  хххх
                хххх  хххх
                хххх  хххх
                хххх  хххх
                хххх  хххх
                хххх  хххх
                хххх  хххх   
                                      '''



def test_game():
    screen = curses.initscr()
    screen.addstr(7, 7, '''    
                            ^---^  
                           ( o.o )   
                           /     \\  
                          /(  _  )\\ 
                           ^^^ ^^^    ''')

    screen.refresh()
    curses.napms(2000)
    curses.endwin()
    print("Window ended.")

if __name__ == '__main__':
    test_game()

