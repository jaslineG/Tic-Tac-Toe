# Tic Tac Toe Game (2 Players - Console Version)

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    win_positions = [
        [0, 1, 2],  # rows
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],  # columns
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],  # diagonals
        [2, 4, 6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False


def check_draw(board):
    return " " not in board


def play_game():
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)

        try:
            move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position! Choose 1-9.")
                continue

            if board[move] != " ":
                print("Position already taken! Try again.")
                continue

            board[move] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"🎉 Player {current_player} wins!")
                break

            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number!")

    replay = input("Do you want to play again? (y/n): ").lower()
    if replay == "y":
        play_game()
    else:
        print("Thanks for playing!")


# Start the game
play_game()