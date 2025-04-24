# Step 1: Create the board
board = [" " for _ in range(9)]

# Step 2: Function to print the board
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Step 3: Function to check for winner
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

# Step 4: Main game loop
def play_game():
    current_player = "X"
    for turn in range(9):
        print_board()
        move = int(input(f"{current_player}'s turn. Choose position (1-9): ")) - 1
        if board[move] != " ":
            print("Position already taken! Try again.")
            continue
        board[move] = current_player
        if check_winner(current_player):
            print_board()
            print(f"{current_player} wins!")
            return
        current_player = "O" if current_player == "X" else "X"
    print_board()
    print("It's a tie!")

# Step 5: Start the game
play_game()
