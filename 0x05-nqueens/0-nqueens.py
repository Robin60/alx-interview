#!/usr/bin/python3
""" N queens puzzle solutions """


import sys


def is_safe(board, row, col, N):
    """
    Checks if the board is safe for Queen
    Args:
        Board: (Matrix) the cell combinations to place the queen
        row: (list) board cell row
        col: board cell column
        N: Board lenth size
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens_until(board, col, N, solutions):
    if col >= N:
        solutions.append(get_queen_pos(board))
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_n_queens_until(board, col + 1, N, solutions)
            board[i][col] = 0


def solve_attack(N):
    """
      Checks bombing attack on the queen"""

    board = [[0] * N for _ in range(N)]
    solutions = []
    solve_n_queens_until(board, 0, N, solutions)
    return solutions


def get_queen_pos(board):
    """ Positions the queen where there's no attack
        in row column or diagonal"""

    pos = []
    for row in board:
        for col, cell in enumerate(row):
            if cell == 1:
                pos.append([board.index(row), col])
    return pos


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    stns = solve_attack(N)
    for stn in stns:
        print(stn)


if __name__ == "__main__":
    main()
