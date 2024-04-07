from board import *
from algo import *
from random import randint, choice


if __name__ == "__main__":
    board = PentagoBoard()
    current_player = randint(1, 2)

    print("Welcome playing Pentago!\n")
    board.print_board()

    # Main loop
    while not board.is_terminal:
        if current_player == 1:
            print(f"Current player {current_player}")
            print("Your turn:")

            # Your turn
            row = int(input("Choose row (1-6): ")) - 1
            col = int(input("Choose column (1-6): ")) - 1
            quadrant = int(input("Choose quarter (1-4): ")) - 1
            direction = input("Choose direction (CW or CCW): ").upper()
            
            # Execute
            # Example: board.make_move(row, col, quadrant, direction, current_player)
            board.make_move(row, col, quadrant, current_player, direction)

        if current_player == 2:
            print(f"Current player {current_player}")
            print("Machine makes a move:")
            best_move = None
            best_value = -inf
            legal_moves = generate_legal_moves(board)
            if legal_moves:
                for move in legal_moves:
                    eva = minimax(move, depth=3, maximizingPlayer=False)
                    if eva > best_value:
                        best_value = eva
                        best_move = move
                board = best_move

        board.print_board()

        # Change turns
        current_player = 2 if current_player == 1 else 1

    print("Game over!")