from blessings import Terminal
t = Terminal()


class bomb ():
    def __init__(self):
        # self.matrix = matrix
        __x = -1  # this is the x -coodinate of the bomb
        __y = -1  # initialisation to -1 means it's not planted yet
        self.score = 0

    def detect(self, matrix):
        pos = [0, 0]
        flag = 0
        for m in range(2, 36):
            for n in range(4, 74):
                if (matrix[m][n] == t.blue('B')):
                    pos[0] = m
                    pos[1] = n
                    flag = 1
                    break
            if(flag):
                break
        return pos

    def bomb_detector(self, matrix):
        pos = [0, 0]
        flag = 0
        for m in range(2, 36):
            for n in range(4, 76):
                if (matrix[m][n] == 'O'):
                    pos[0] = m
                    pos[1] = n-1
                    flag = 1
                    break
            if (flag):
                break
        return pos

    def give_score(self):
        return self.score

    def plant(self, matrix):
        position = self.detect(matrix)
        self.__x = position[0]
        self.__y = position[1]
        matrix[self.__x][self.__y+1] = t.cyan('O')
        matrix[self.__x][self.__y+2] = t.cyan('M')
        matrix[self.__x+1][self.__y+1] = t.cyan('O')
        matrix[self.__x+1][self.__y+2] = t.cyan('M')
        return matrix

    def explosion_process(self, time_remaining, matrix):
        if (self.__x == -1):
            position = self.bomb_detector(matrix)
        else:
            position = [self.__x, self.__y]
        i = position[0]
        j = position[1]
        for m in range(0, 2):
            for n in range(0, 4):
                matrix[i+m][j+n] = t.yellow(str(time_remaining))

        return matrix

    def print_var(self, i, j, var, matrix):
        for m in range(0, 2):
            for n in range(0, 4):
                matrix[i+m][j+n] = var
        return matrix

    def clear_mess(self, matrix):
        matrix = self.print_var(self.__x, self.__y, ' ', matrix)
        return matrix

    def explode(self, matrix):
        dead = 0
        i = self.__x
        j = self.__y
        matrix = self.print_var(i, j, t.red('e'), matrix)

        if (matrix[i-1][j] != 'X'):
            if (matrix[i-1][j] == t.green('/')):
                self.score += 20
            if (matrix[i-1][j] == t.magenta('E')):
                self.score += 100
            if (matrix[i-1][j] == t.blue('B')):
                dead = 1
            matrix = self.print_var(i-2, j, t.red('e'), matrix)

        if (matrix[i+3][j] != 'X'):
            if (matrix[i+3][j] == t.green('/')):
                self.score += 20
            if (matrix[i+3][j] == t.magenta('E')):
                self.score += 100
            if (matrix[i+3][j] == t.blue('B')):
                dead = 1
            matrix = self.print_var(i+2, j, t.red('e'), matrix)

        if (matrix[i][j+4] != 'X'):
            if (matrix[i][j+4] == t.green('/')):
                self.score += 20
            if (matrix[i][j+4] == t.magenta('E')):
                self.score += 100
            if (matrix[i][j+4] == t.blue('B')):
                dead = 1
            matrix = self.print_var(i, j+4, t.red('e'), matrix)

        if (matrix[i][j-1] != 'X'):
            if (matrix[i][j-1] == t.green('/')):
                self.score += 20
            if (matrix[i][j-1] == t.magenta('E')):
                self.score += 100
            if (matrix[i][j-1] == t.blue('B')):
                dead = 1
            matrix = self.print_var(i, j-4, t.red('e'), matrix)

        if dead == 1:
            return 'death'
        return matrix

    def clear(self, matrix):
        i = self.__x
        j = self.__y
        self.__x = -1
        self.__y = -1
        matrix = self.print_var(i, j, ' ', matrix)

        if (matrix[i-1][j] == t.red('e')):
            matrix = self.print_var(i-2, j, ' ', matrix)

        if (matrix[i+2][j] == t.red('e')):
            matrix = self.print_var(i+2, j, ' ', matrix)

        if (matrix[i][j-1] == t.red('e')):
            matrix = self.print_var(i, j-4, ' ', matrix)

        if (matrix[i][j+4] == t.red('e')):
            matrix = self.print_var(i, j+4, ' ', matrix)
        return matrix
