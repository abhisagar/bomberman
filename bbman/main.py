import os
from bricks import *
import sys
import tty
import termios
from player import *
from board import *
from wall import *
from bomb import *
from enemy import *
from blessings import Terminal
t = Terminal()

level = 1
lives = 3
won = 0
board = board()
matrix = board.boa()

wall = wall()
matrix = wall.provide_matrix(matrix)

bricks = bricks()
matrix = bricks.provide_matrix(matrix)

bomb = bomb()

bomberman = player()

enemy = enemy()
enemy.create_enemy(5, matrix)


def print_wall():
    print()
    for i in range(38):
        for j in range(76):
            print(matrix[i][j], end='')
        print('')
    print(" ")

print_wall()

planted = 0
explode = 0
explosion_done = 0

while (lives):
    matrix = bomberman.initialisation(matrix)
    if (planted):
        planted = 0
        matrix = bomb.clear_mess(matrix)
    print_wall()
    temp = 'alive'
    while (True):
        # time.sleep(1)
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            x = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        if (explosion_done):
            explosion_done = 0
            matrix = bomb.clear(matrix)
            print_wall()

        if (x == 'q'):
            break

        elif (x == 'd'):
            temp = bomberman.move_right(matrix)
            if (temp == 'death'):
                matrix = bomberman.initialisation(matrix)
                break
            else:
                matrix = temp

        elif (x == 's'):
            temp = bomberman.move_down(matrix)
            if (temp == 'death'):
                matrix = bomberman.initialisation(matrix)
                break
            else:
                matrix = temp

        elif (x == 'a'):
            temp = bomberman.move_left(matrix)
            if (temp == 'death'):
                matrix = bomberman.initialisation(matrix)
                break
            else:
                matrix = temp

        elif (x == 'w'):
            temp = bomberman.move_up(matrix)
            if (temp == 'death'):
                matrix = bomberman.initialisation(matrix)
                break
            else:
                matrix = temp

        elif (x == 'b' and planted == 0):
            matrix = bomb.plant(matrix)
            planted = 3
        else:
            pass

        temp = enemy.move_random(matrix)
        if (temp == 'death'):
            bomberman.initialisation(matrix)
            break
        elif (temp == 'won'):
            print('\t\tYou won, cheers!!!!!')
            won = 1
            break
        else:
            matrix = temp

        os.system('cls' if os.name == 'nt' else 'clear')
        print_wall()

        if (explosion_done):
            explosion_done = 0
            matrix = bomb.clear(matrix)
            print_wall()

        if (explode):
            temp = bomb.explode(matrix)
            if (temp == 'death' or bomberman.dead_check(matrix) == 'dead'):
                print_wall()
                matrix = bomb.clear(matrix)
                matrix = bomberman.initialisation(matrix)
                break
            else:
                matrix = temp
            explosion_done = 1
            explode = 0
            print_wall()

        if (planted != 3 and planted != 0):
            matrix = bomb.explosion_process(planted, matrix)
            planted -= 1
            print_wall()
            if (planted == 0):
                explode = 1

        if (planted == 3):
            planted -= 1
        print("\tScore : " +
              str(bomb.give_score()) + "\tLives : " + str(lives))
        print("")

    if x == 'q' or won == 1:
        break
    lives -= 1
    print("\tScore : " + str(bomb.give_score()) + "\tLives : " + str(lives))
    print("\tYou lost a life :(")
if won == 0:
    print(t.red("\tGame Over"))
