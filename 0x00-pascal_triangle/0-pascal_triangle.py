#!/usr/bin/python3
"""
0. Pascal's Triangle.
"""


def pascal_triangle(n):
    """ Returns a list of lists of integers representing the
        Pascals triangle of "n" else return empty  if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prow = triangle[-1]

        for j in range(1, i):
            row.append(prow[j - 1] + prow[j])

        row.append(1)
        triangle.append(row)
    return triangle
