from person import person
from blessings import Terminal

t = Terminal()


class player (person):
    def __init__(self):
        # self.matrix = matrix
        __x = 2
        __y = 4
        self.flag_bomb = 0

    def initialisation(self, matrix):
        self.__x = 2
        self.__y = 4
        matrix = self.print_var(2, 4, t.blue('B'), matrix)
        return matrix

    def dead_check(self, matrix):
        if (matrix[self.__x][self.__y] == 'e' or
           matrix[self.__x][self.__y] == 'E' or
           matrix[self.__x][self.__y] == ' '):
            return 'dead'
        return 'alive'

    def move_right(self, matrix):
        if (self.dead_check(matrix) == 'dead'):
            return 'death'
        i = self.__x
        j = self.__y
        if (matrix[i][j+4] != ' '):
            return matrix
        self.__y += 4
        matrix = self.print_var(i, j, ' ', matrix)
        matrix = self.print_var(i, j+4, t.blue('B'), matrix)
        return matrix

    def move_left(self, matrix):
        if (self.dead_check(matrix) == 'dead'):
            return 'death'
        i = self.__x
        j = self.__y
        if (matrix[i][j-1] != ' '):
            return matrix
        self.__y -= 4
        matrix = self.print_var(i, j, ' ', matrix)
        matrix = self.print_var(i, j-4, t.blue('B'), matrix)
        return matrix

    def move_down(self, matrix):
        if (self.dead_check(matrix) == 'dead'):
            return 'death'
        i = self.__x
        j = self.__y
        if (matrix[i+3][j] != ' '):
            return matrix
        self.__x += 2
        matrix = self.print_var(i, j, ' ', matrix)
        matrix = self.print_var(i+2, j, t.blue('B'), matrix)
        return matrix

    def move_up(self, matrix):
        if (self.dead_check(matrix) == 'dead'):
            return 'death'
        i = self.__x
        j = self.__y
        if (matrix[i-1][j] != ' '):
            return matrix
        self.__x -= 2
        matrix = self.print_var(i, j, ' ', matrix)
        matrix = self.print_var(i-2, j, t.blue('B'), matrix)
        return matrix
