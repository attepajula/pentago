from board import PentagoBoard
from math import inf
import random

def minimax(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or board.is_terminal:
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
    for i in range(-4, 2):
        diag1 = ''.join([board.state[i + j][j] for j in range(max(0, -i), min(6, 6 - i))])
        if len(diag1) == 6:
            lines.append(diag1)

    for i in range(-4, 2):
        diag2 = ''.join([board.state[5 - j][i + j] for j in range(max(0, -i), min(6, 6 - i))])
        if len(diag2) == 6:
            lines.append(diag2)

    ai_symbol = "X"
    user_symbol = "O"
    ai_score = 0
    user_score = 0

    def evaluate_line(line, symbol):
        score = 0
        if symbol == user_symbol:
            if ai_symbol in line:
                return 0
        else:
            if user_symbol in line:
                return 0
        score = 2 ** (line.count(symbol) - 1)
        return score

    for line in lines:
        ai_score += evaluate_line(line, ai_symbol)
        user_score += evaluate_line(line, user_symbol)

    # Center positions
    center_positions = [(1, 1), (1, 4), (4, 1), (4, 4)]
    random.shuffle(center_positions)
    for row, col in center_positions:
        if board.state[row][col] == ai_symbol:
            ai_score += 10
        elif board.state[row][col] == user_symbol:
            user_score += 10

    # Defence
    if ai_score < 10:
        if user_score > 15:
            user_score += 100

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
