def isValid(cols, row, col):
    for i in range(row):
        if (cols[i] == col) or ((row - i) == abs(col - cols[i])):
            return False
    return True

def nqueens(n):

    def nqueensHelper(cols, row, n):
        if row == n:
            return [cols.copy()]
        res = []
        for col in range(n):
            if isValid(cols, row, col):
                cols[row] = col
                partial = nqueensHelper(cols, row+1, n)
                res += partial
        return res

    cols = [0] * n
    return nqueensHelper(cols, 0, n)

solutions = nqueens(8)
print("There are {} solutions:".format(len(solutions)))
print(solutions)

def nqueens_iter(n):
    res = []
    cols = [0] * n
    row = 0
    start = 0

    while True:
        found = False
        if row == n:
            res.append(cols.copy())
            row -= 1
        else:
            for col in range(start, n):
                if isValid(cols, row, col):
                    cols[row] = col
                    start = 0
                    row += 1
                    found = True
                    break

        if not found:
            start = cols[row-1]+1;
            row -= 1
            if start == n:
                if row == 0:
                    break
                else:
                    start = cols[row-1]+1
                    row -= 1
    return res

solutions = nqueens_iter(10)
print("There are {} solutions:".format(len(solutions)))
print(solutions)
