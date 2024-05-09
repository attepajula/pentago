from board import *
from algo import *
from random import randint

def your_turn():
    # Your turn
    row = int(input("Choose row (1-6): ")) - 1
    col = int(input("Choose column (1-6): ")) - 1
    quadrant = int(input("Choose quarter (1-4): ")) - 1
    directionInput = input("Choose direction (CW or CCW): ").upper()
    if directionInput == "CW":
        direction = 1
    elif directionInput == "CCW":
        direction = -1
    else:
        direction = None

    return [row, col, quadrant, direction]

def play():
    board = PentagoBoard()
    current_player = randint(1, 2)

    print("Welcome playing Pentago!\n")
    board.print_board()

    # Main loop
    while not board.terminal:
        if current_player == 1:
            print(f"Current player {current_player}")
            print("Your turn:")
            
            while True:
                # Your turn
                try:
                    moves = your_turn()
                    if board.make_move(moves[0], moves[1], moves[2], current_player, moves[3]):
                        break
                except(ValueError):
                    print("Invalid input!")

        if current_player == 2:
            print(f"Current player {current_player}")
            print("Machine makes a move:")
            best_move = iterative_deepening(board, max_depth=3, time_limit=1)
            if best_move:
                board = best_move

        board.is_terminal()
        board.print_board()

        # Change turns
        current_player = 2 if current_player == 1 else 1

    print("Game over!")