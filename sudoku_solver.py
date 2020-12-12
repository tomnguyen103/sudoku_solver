import numpy as np

# grid = [
#     [0, 0, 0, 0, 5, 0, 6, 3, 1],
#     [0, 9, 0, 1, 0, 0, 0, 0, 4],
#     [7, 0, 0, 0, 0, 0, 0, 0, 0],
#     [6, 0, 7, 0, 0, 8, 0, 1, 0],
#     [0, 0, 4, 0, 3, 0, 9, 6, 0],
#     [1, 0, 0, 0, 4, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 6],
#     [4, 0, 1, 0, 0, 0, 5, 8, 3],
#     [9, 5, 0, 0, 0, 0, 0, 0, 0]
# ]
grid = [
    [0, 0, 0, 0, 5, 0, 6, 3, 1],
    [0, 9, 0, 1, 0, 0, 0, 0, 4],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [6, 0, 7, 0, 0, 8, 0, 1, 0],
    [0, 0, 4, 0, 3, 0, 9, 6, 0],
    [1, 0, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [4, 0, 1, 0, 0, 0, 5, 8, 3],
    [9, 5, 0, 0, 0, 0, 0, 0, 0]
]
# using numpy to print a perfect matrix
print(np.matrix(grid))
print()


# function to check if the position n is valid  or not
# perform to check for the big grid (9x9) and smaller grid (3x3)
# return False if there is a number
def possible_position(x, y, n):
    global grid

    # return False if there is an element at that grid[y][x] position
    # check if number n is exist in the row
    for i in range(0, 9):
        if grid[i][y] == n:
            return False

    # check if number n is exist in the column
    for j in range(0, 9):
        if grid[x][j] == n:
            return False

    # // means only take ground or round down to the whole number after the division
    # divide into smaller square (3x3)
    x1 = (x // 3) * 3
    y1 = (y // 3) * 3

    # perform a check for each small square (3x3)
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x1 + i][y1 + j] == n:
                return False
    return True


# print(possible_position(4, 4, 1))


def solve_puzzle():
    global grid

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:  # which is empty position
                for n in range(1, 10):
                    # backtracking algorithm
                    if possible_position(i, j, n):
                        grid[i][j] = n
                        solve_puzzle()
                        grid[i][j] = 0
                return
    print("Solution: ")
    print(np.matrix(grid))


solve_puzzle()
