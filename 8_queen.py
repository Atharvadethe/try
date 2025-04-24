N = 8

def print_solution(board):
    for row in board:
        # Debug print to show what col is for each cell
        print("Values in this row:", row)
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    # Check same column
    for i in range(row):
        if board[i][col]:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j]:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, N)):
        if board[i][j]:
            return False

    return True

def solve(board, row):
    if row == N:
        print_solution(board)
        return True  # To print only one solution, return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen
            if solve(board, row + 1):  # Move to next row
                return True
            board[row][col] = 0  # Backtrack

    return False

# Create 8x8 chess board initialized with 0
board = [[0 for _ in range(N)] for _ in range(N)]

if not solve(board, 0):
    print("No solution exists.")
