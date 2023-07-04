#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    # Check if a queen can be placed at the given position (row, col)

    # Check the current column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check the upper diagonal on the left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the upper diagonal on the right side
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, solutions):
    # Solve the N Queens problem using backtracking

    n = len(board)

    # Base case: If all queens are placed, add the solution to the list
    if row == n:
        queens = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    queens.append([i, j])
        solutions.append(queens)
        return

    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col):
            # Place the queen at position (row, col)
            board[row][col] = 1

            # Recursively solve the problem for the next row
            solve_nqueens(board, row + 1, solutions)

            # Backtrack and remove the queen from position (row, col)
            board[row][col] = 0


def print_solutions(solutions):
    # Print all the solutions to the N Queens problem

    for queens in solutions:
        print(queens)

    print()


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Get the value of N from the command line argument
        N = int(sys.argv[1])

        # Check if N is at least 4
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)

        # Create an empty chessboard of size N x N
        board = [[0 for _ in range(N)] for _ in range(N)]
        solutions = []

        # Solve the N Queens problem
        solve_nqueens(board, 0, solutions)

        # Print the solutions
        print_solutions(solutions)

    except ValueError:
        print("N must be a number")
        sys.exit(1)


if __name__ == '__main__':
    main()
