#!/usr/bin/python3
""" Returns the perimeter of the island described in grid """


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid
       Args:
          grid: a list of integers
    """
    width = len(grid[0])
    height = len(grid)
    size = 0
    edge = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edge += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edge += 1
    return size * 4 - edge * 2
