from board import PentagoBoard
from math import inf

def minimax(board, depth, maximizingPlayer):
    if depth == 0 or board.is_terminal:
        return evaluate(board)

    if maximizingPlayer:
        maxEval = -inf
        for move in board.generate_legal_moves():
            eva = minimax(move, depth - 1, False)
            maxEval = max(maxEval, eva)
        return maxEval
    else:
        minEval = inf
        for move in board.generate_legal_moves():
            eva = minimax(move, depth - 1, True)
            minEval = min(minEval, eva)
        return minEval
    
def evaluate(board):
    return 0

def generate_legal_moves(board):
    legal_moves = []

    empty_squares = [(row, col) for row in range(6) for col in range(6) if board.state[row][col] == "_"]

    if empty_squares:
        for row, col in empty_squares:
            for quadrant in range(4):
                for direction in ["CW", "CCW"]:
                    new_board = board.copy()
                    if new_board.make_move(row, col, quadrant, 2, direction):
                        legal_moves.append(new_board)

    return legal_moves
