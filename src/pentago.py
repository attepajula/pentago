from board import *
from algo import *
from random import randint

def your_turn():
    # Your turn
    row = int(input("Choose row (1-6): ")) - 1
    col = int(input("Choose column (1-6): ")) - 1
    quadrant = int(input("Choose quarter (1-4): ")) - 1
    direction = input("Choose direction (CW or CCW): ").upper()

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
            best_move = None
            best_value = -inf
            beta = inf
            legal_moves = generate_legal_moves(board)
            if legal_moves:
                for move in legal_moves:
                    new_board = move.copy()
                    eva = minimax(new_board, depth=6, alpha=best_value, beta=beta, maximizingPlayer=False)
                    if eva > best_value:
                        best_value = eva
                        best_move = move
                board = best_move
        board.print_board()

        # Change turns
        current_player = 2 if current_player == 1 else 1

    print("Game over!")