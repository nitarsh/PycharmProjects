def value(grid, x, y):
    if (x < 0 or y < 0):
        return 0
    gsize = len(grid)
    if (x >= gsize or y >= gsize):
        return 0
    return grid[x][y]


def next_life_status(grid, x, y):
    surr = ((x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if x != 0 or y != 0)
    # surr = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
    live_cells = 0
    for tup in surr:
        live_cells += value(grid, x + tup[0], y + tup[1])

    if (grid[x][y] == 0 and live_cells == 3):
        return 1
    if (grid[x][y] == 1):
        if (live_cells < 2):
            return 0
        elif (live_cells > 3):
            return 0
        else:
            return 1

    return 0
    # gsize = int(input("Enter the size of the grid"))


import os
import time
import random


def printer(num):
    if (num == 0):
        return " "
    else:
        return "*"


gsize = 30
grid = [[round(random.random()) for x in range(gsize)] for x in range(gsize)]
# grid = [[0 for x in range(gsize)] for x in range(gsize)]
grid_cpy = [row[:] for row in grid]
iter = 0
while (True):
    os.system('clear')

    for x in range(gsize):
        for y in range(gsize):
            grid_cpy[x][y] = next_life_status(grid, x, y)
            print printer(grid_cpy[x][y]),
        print ""
    print iter
    iter += 1
    # grid_cpy = [row[:] for row in grid]
    grid = [row[:] for row in grid_cpy]
    time.sleep(0.2)
