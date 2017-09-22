class wall ():
    def provide_matrix(self, matrix):
        for i in range(38):
            for j in range(76):
                if (i <= 1 or j <= 3 or i >= 36 or j >= 72):
                    matrix[i][j] = 'X'
                if ((i % 4 <= 1) and (j % 8 <= 3)):
                    matrix[i][j] = 'X'
        return matrix
