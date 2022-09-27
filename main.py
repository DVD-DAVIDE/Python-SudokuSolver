from xml.etree.ElementTree import tostring
import numpy as np
grid = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i]==n:
            return False
    for i in range(0,9):
        if grid[i][x]==n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j]==n:
                return False
    return True

print(np.matrix(grid)) # type: ignore
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid)) # type: ignore
    input("More?")

def inputSudoku():
    global grid
    for y in range(9):
        for x in range(9):
            n = grid[y][x]
            while True:
                k = input(("L{}C{} ({}):").format(y+1,x+1,n))
                if k == "":
                    break
                else:
                    n = int(k)
                    if (n >= 1) and (n <= 9):
                        break
                    else:
                        print("Invalid number. Insert a valid number (1-9) or press ENTER for an empty cell.")
            grid[y][x] = n
    print("Sudoku table:")
    print(np.matrix(grid)) #type: ignore
    c = input("Is the sudoku correct? (y/n): ")
    if c.upper()[0] == 'N':
        inputSudoku()
inputSudoku()
solve()