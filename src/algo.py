from board import PentagoBoard
from math import inf
import random

def minimax(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or board.is_terminal() == True:
        return evaluate(board)
    if maximizingPlayer:
        maxEval = -inf
        for move in generate_legal_moves(board):
            eva = minimax(move, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eva)
            alpha = max(alpha, eva)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = inf
        for move in generate_legal_moves(board):
            eva = minimax(move, depth - 1, alpha, beta, True)
            minEval = min(minEval, eva)
            beta = min(beta, eva)
            if beta <= alpha:
                break
        return minEval

def evaluate(board):
    rows = [''.join(row) for row in board.state]
    cols = [''.join(col) for col in zip(*board.state)]
    lines = rows + cols
    ai_symbol = "X"
    user_symbol = "O"
    ai_score = 0
    user_score = 0

    for line in lines:
        # Count AI and user symbols in the line
        ai_count = line.count(ai_symbol)
        user_count = line.count(user_symbol)

        # Update AI and user scores
        ai_score += ai_count / 2
        user_score += user_count / 2

        # Check for winning patterns and update scores accordingly
        if ai_count == 5 or ai_count == 6:
            if ai_symbol in line[1]:
                ai_score += 50
        elif user_count == 5 or user_count == 6:
            if user_symbol in line[1]:
                user_score += 50

        # Center positions
        center_positions = [(1, 1), (1, 4), (4, 1), (4, 4)]
        random.shuffle(center_positions)
        for row, col in center_positions:
            if board.state[row][col] == ai_symbol:
                ai_score += 3
            elif board.state[row][col] == user_symbol:
                user_score += 3

        # Defence
        if ai_score < 10 and user_score > 15:
            user_score += 15

    return ai_score - user_score
 
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
