import numpy as np

grid = [
    [0, 0, 0, 0, 0, 9, 0, 7, 0],
    [0, 0, 0, 0, 8, 2, 0, 5, 0],
    [3, 2, 7, 0, 0, 0, 0, 4, 0],
    [0, 1, 6, 0, 4, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 9, 0, 7, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 5],
    [8, 0, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 2, 0, 0, 0, 0, 8]
]

# using numpy to print a perfect matrix
print(np.matrix(grid))

# function to find the possible value of n for grid[y][x] = 0
def possible(y,x,n):
    global grid
    # return False if there is an element at that grid[y][x] position
    # check if number n is exist in the row
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    # check if number n is exist in the column
    for j in range(0, 9):
        if grid[j][x] == n:
            return False
    # // means only take ground or round down to the whole number after the division
    # divide into smaller square (3x3)
    x1 = (x//3)*3
    y1 = (y//3)*3