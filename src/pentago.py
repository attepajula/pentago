from board import *
from algo import *
from random import randint

def your_turn():
    # Your turn
    # Need to raise an error in case of string in place of integer!!!!!
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
                moves = your_turn()
                # Execute
                # Example: board.make_move(row, col, quadrant, current_player, direction)
                if board.make_move(moves[0], moves[1], moves[2], current_player, moves[3]):
                    break

        if current_player == 2:
            print(f"Current player {current_player}")
            print("Machine makes a move:")
            best_move = None
            best_value = -inf
            legal_moves = generate_legal_moves(board)
            if legal_moves:
                for move in legal_moves:
                    eva = minimax(move, depth=50, maximizingPlayer=False)
                    if eva > best_value:
                        best_value = eva
                        best_move = move
                board = best_move
        if board.is_terminal():
            board.terminal = True
        board.print_board()

        # Change turns
        current_player = 2 if current_player == 1 else 1

    print("Game over!")