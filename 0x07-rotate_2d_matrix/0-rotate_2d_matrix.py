#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """
       Rotates a n by n matrix to 90 degrees
    """

    n = len(matrix)

    # Transpose the matrix
    for row in range(n):
        for col in range(row, n):
            matrix[row][col], matrix[col][row] = matrix[col][row],\
                    matrix[row][col]

    # Reverse each row
    for row in range(n):
        matrix[row].reverse()
