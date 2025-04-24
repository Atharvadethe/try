N = 8  # Size of the chessboard

def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    # Check column above
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row):
    if row == N:
        print_board(board)
        return True  # Return True if you only want the first solution

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if solve_n_queens(board, row + 1):
                return True  # Comment this line to print all solutions
            board[row][col] = 0  # Backtrack

    return False

# Initialize an empty 8x8 board
board = [[0] * N for _ in range(N)]

print("One possible solution to the 8-Queens problem:")
solve_n_queens(board, 0)
