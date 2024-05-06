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
        ai_score += evaluate_line(line, "X", ai_score, user_score)
        user_score += evaluate_line(line, "O", ai_score, user_score)

    def evaluate_line(line, symbol):
        ai_score += line.count(ai_symbol) / 2
        user_score += line.count(user_symbol) / 2

        if line.count(symbol) == 5 or line.count(symbol) == 6:
            if line[1]:
                if symbol == user_symbol:
                    user_score += 50
                if symbol == ai_symbol:
                    ai_score += 50

        # Center positions
        center_positions = [(1, 1), (1, 4), (4, 1), (4, 4)]
        random.shuffle(center_positions)
        for row, col in center_positions:
            if board.state[row][col] == ai_symbol:
                ai_score += 3
            elif board.state[row][col] == user_symbol:
                user_score += 3

        # Defence
        if ai_score < 10:
            if user_score > 15:
                user_score += 15
        
        if symbol == "O":
            return user_score
        else:
            return ai_score

    for line in lines:
        ai_score += evaluate_line(line, "X")
        user_score += evaluate_line(line, "O")

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
