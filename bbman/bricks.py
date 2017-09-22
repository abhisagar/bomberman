import random
from blessings import Terminal
t = Terminal()


class bricks ():
    def provide_matrix(self, matrix):
        count = 0
        while (count < 20):
            i = random.randint(2, 36)
            j = random.randint(4, 72)
            i = i - (i % 2)
            j = j - (j % 4)
            if (matrix[i][j] == ' ' and
               matrix[i+1][j+3] == ' ' and
               matrix[i+1][j] == ' ' and
               matrix[i][j+3] == ' '):
                for m in range(0, 2):
                    for n in range(0, 4):
                        matrix[i+m][j+n] = t.green('/')
                count += 1
        return matrix
