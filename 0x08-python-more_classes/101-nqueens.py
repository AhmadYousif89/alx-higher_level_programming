#!/usr/bin/python3
def main():
    """Entry point function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N", file=sys.stderr)
        sys.exit(1)

    nqueens_puzzle(sys.argv[1])


def nqueens_puzzle(N):
    """
    The N-queens puzzle.
    ====================
    - The challenge of placing N non-attacking queens on an NxN chessboard.

    Usage:
    - ./101-nqueens.py N

    Args:
    - N: The number of queens.
    Execptions:
    - ValueError:
                N must be be a number.
                N must be an integer >= 4.
    Attributes:
    - board type(list): A list of lists representing the chessboard.
    - results type(list): A list containing all possible solutions.

    - Solutions are represented in this format [[r, c], [r, c], [r, c], [r, c]]
    where `r` and `c` represent the row and column, respectively, where a
    queen must be placed on the chessboard.
    """
    try:
        N = int(N)
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)

    if N < 4:
        print("N must be at least 4", file=sys.stderr)
        sys.exit(1)

    # Initialize the chess board with zeros
    board = [[0 for _ in range(N)] for _ in range(N)]
    results = []

    solve_puzzle(board, 0, N, results)

    for solution in results:
        for row, col in enumerate(solution):
            print(
                f'[{row}, {col}]', end=' ' if row != len(solution) - 1 else '\n'
            )


def solve_puzzle(board, row, N, results):
    # Base case: all queens are placed
    # add the current solution to the results
    if row == N:
        results.append(board.copy())
        return

    # Try placing a queen in each row of the current column
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            # Recusively move to next row
            solve_puzzle(board, row + 1, N, results)


def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if (
            board[i] == col  # queen vertically in the same column
            or board[i] + i == col + row  # queen in the right diagonal
            or board[i] - i == col - row  # queen in the left diagonal
        ):
            return False
    return True


if __name__ == "__main__":
    import sys

    main()
