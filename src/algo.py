from board import PentagoBoard
from math import inf
import random

def iterative_deepening(board, max_depth):
    best_move = None
    best_value = float('-inf')
    for depth in range(1, max_depth + 1):
        move = minimax(board, depth)
        value = evaluate(move)
        if value > best_value:
            best_value = value
            best_move = move
    return best_move

def minimax(board, depth):
    alpha = float('-inf')
    beta = float('inf')
    maximizingPlayer = False
    best_move = None
    best_value = float('-inf')
    for move in generate_legal_moves(board):
        value = min_value(move, depth - 1, alpha, beta, maximizingPlayer)
        if value > best_value:
            best_value = value
            best_move = move
    return best_move

def max_value(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or board.is_terminal():
        return evaluate(board)
    v = float('-inf')
    for move in generate_legal_moves(board):
        v = max(v, min_value(move, depth - 1, alpha, beta, not maximizingPlayer))
        alpha = max(alpha, v)
        if beta <= alpha:
            break
    return v

def min_value(board, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or board.is_terminal():
        return evaluate(board)
    v = float('inf')
    for move in generate_legal_moves(board):
        v = min(v, max_value(move, depth - 1, alpha, beta, not maximizingPlayer))
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v

def evaluate(board):
    ai_symbol = "X"
    user_symbol = "O"
    ai_score = 0
    user_score = 0

    # Weight center points of segments
    center_positions = [(1, 1), (1, 4), (4, 1), (4, 4)]
    for row, col in center_positions:
        if board.state[row][col] == ai_symbol:
            ai_score += 2
        elif board.state[row][col] == user_symbol:
            user_score += 2

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
