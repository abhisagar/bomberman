import random
from person import person
from blessings import Terminal

t = Terminal()


class enemy (person):

    def __init__(self):
        # self.matrix = matrix
        self.num = 0
        __x = 0
        __y = 0
        self.dir = [0, 0, 0, 0]
        self.flag = 0

    def create_enemy(self, num, matrix):
        self.num = num
        count = 0
        while (count < num):
            i = random.randint(2, 36)
            j = random.randint(4, 72)
            i = i - (i % 2)
            j = j - (j % 4)
            if (i < 4 and j < 8):
                continue
            else:
                if (matrix[i][j] == ' ' and matrix[i + 1][j + 3] == ' ' and
                        matrix[i][j + 3] == ' ' and matrix[i + 1][j] == ' '):
                    matrix = self.print_var(i, j, t.magenta('E'), matrix)
                    count += 1
        return matrix

    # in direcitons
        # 0 stands for down
        # 1 stands for up
        # 2 stands for right
        # 3 stands for left

    def directions(self, i, j, matrix):
        # here j+5 is used as if the bomb is just planted then the j+4'th index
        # would be 'B' only
        if (matrix[i][j + 5] == ' ' or matrix[i][j + 5] == t.blue('B')):
            self.dir[2] = 1
        else:
            self.dir[2] = 0

        if (matrix[i][j - 3] == ' ' or matrix[i][j - 3] == t.blue('B')):
            self.dir[3] = 1
        else:
            self.dir[3] = 0

        if (matrix[i - 2][j + 1] == ' ' or
                matrix[i - 2][j + 1] == t.blue('B')):
            self.dir[1] = 1
        else:
            self.dir[1] = 0

        if (matrix[i + 2][j + 1] == ' ' or
                matrix[i + 2][j + 1] == t.blue('B')):
            self.dir[0] = 1
        else:
            self.dir[0] = 0
        return matrix

    def move_random(self, matrix):
        present = 0
        done = [[0 for i in range(76)] for j in range(38)]
        for i in range(36):
            for j in range(72):
                if (matrix[i][j] == t.magenta('E') and done[i][j] == 0):
                    present += 1
                    self.directions(i, j, matrix)
                    helper = [0, 0, 0, 0]
                    count = 0
                    new_direction = -1
                    self.__x = i
                    self.__y = j
                    for k in range(4):
                        if (self.dir[k] == 1):
                            helper[count] = k
                            count += 1

                    if (count != 0):
                        temp = random.randint(0, count - 1)
                        new_direction = helper[temp]

                    if (new_direction == -1):
                        done = self.print_var(self.__x, self.__y, 1, done)

                    else:
                        matrix = self.print_var(self.__x, self.__y, ' ', matrix)

                        if (new_direction == 0):
                            if (matrix[self.__x + 2][self.__y] == t.blue('B')):
                                self.flag = 1
                            matrix = self.print_var(
                                self.__x + 2, self.__y, t.magenta('E'), matrix)
                            done = self.print_var(self.__x + 2, self.__y, 1, done)

                        if (new_direction == 1):
                            if (matrix[self.__x - 2][self.__y] == t.blue('B')):
                                self.flag = 1
                            matrix = self.print_var(
                                self.__x - 2, self.__y, t.magenta('E'), matrix)

                            done = self.print_var(self.__x - 2, self.__y, 1, done)

                        if (new_direction == 2):
                            if (matrix[self.__x][self.__y + 4] == t.blue('B')):
                                self.flag = 1
                            matrix = self.print_var(
                                self.__x, self.__y + 4, t.magenta('E'), matrix)
                            done = self.print_var(self.__x, self.__y + 4, 1, done)

                        if (new_direction == 3):
                            if (matrix[self.__x][self.__y - 4] == t.blue('B')):
                                self.flag = 1
                            matrix = self.print_var(
                                self.__x, self.__y - 4, t.magenta('E'), matrix)
                            done = self.print_var(self.__x, self.__y - 4, 1, done)
        if (self.flag):
            self.flag = 0
            return 'death'
        if (present == 0):
            return 'won'
        else:
            return matrix
