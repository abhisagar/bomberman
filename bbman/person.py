class person ():
    def print_var(self, i, j, var, arr):
        for m in range(0, 2):
            for n in range(0, 4):
                arr[i+m][j+n] = var
        return arr
