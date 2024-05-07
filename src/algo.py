from board import PentagoBoard
from math import inf
import time

def iterative_deepening(board, max_depth, time_limit):
    best_move = None
    best_value = float('-inf')
    start_time = time.time()
    
    depth = 1
    hash_table = {}
    
    while depth <= max_depth and time.time() - start_time < time_limit:
        move, value = minimax(board, depth, hash_table)
        if value > best_value:
            best_value = value
            print("Value:", value)
            best_move = move
        depth += 1
    
    return best_move

def minimax(board, depth, hash_table, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=True):
    if board in hash_table and hash_table[board][1] >= depth:
        return hash_table[board]
    
    if depth == 0 or board.is_terminal():
        return None, evaluate(board)
    
    best_move = None
    best_value = float('-inf') if maximizingPlayer else float('inf')
    
    for move in generate_legal_moves(board):
        new_board = move
        _, value = minimax(new_board, depth - 1, hash_table, alpha, beta, not maximizingPlayer)
        if maximizingPlayer:
            if value > best_value:
                best_value = value
                best_move = move
            alpha = max(alpha, best_value)
        else:
            if value < best_value:
                best_value = value
                best_move = move
            beta = min(beta, best_value)
        if beta <= alpha:
            break
    
    hash_table[board] = (best_move, depth)
    
    return best_move, best_value


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
    ai_symbol = 2
    user_symbol = 1
    ai_score = 0
    user_score = 0
    row_counts = []
    col_counts = []
    diagonal_counts = []

    for row in board.state:
        if user_symbol in row[:5]:
            ai_score = 0
            row_counts.append(0)
        else:
            row_counts.append(row.count(ai_symbol))

    for col in zip(*board.state):
        if user_symbol in col[:5]:
            ai_score = 0
            col_counts.append(0)
        else:
            col_counts.append(col.count(ai_symbol))

        # Top-left to bottom-right
        for i in range(3):
            if i == 0:
                diag1 = [board.state[1][0], board.state[2][1], board.state[3][2], board.state[4][3], board.state[5][4]]
            if i == 1:
                diag1 = [board.state[0][0], board.state[1][1], board.state[2][2], board.state[3][3], board.state[4][4], board.state[5][5]]
                if user_symbol in diag1[:5]:
                    ai_score = 0
                    diagonal_counts.append(0)
            if i == 2:
                diag1 = [board.state[0][1], board.state[1][2], board.state[2][3], board.state[3][4], board.state[4][5]]
            else:
                diagonal_counts.append(diag1.count(ai_symbol))
            
        # Top-right to bottom-left
        for i in range(3):
            if i == 0:
                diag2 = [board.state[0][4], board.state[1][3], board.state[2][2], board.state[3][1], board.state[4][0]]
            if i == 1:
                diag2 = [board.state[0][5], board.state[1][4], board.state[2][3], board.state[3][2], board.state[4][1], board.state[5][0]]
                if user_symbol in diag2[:5]:
                    ai_score = 0
                    diagonal_counts.append(0)
            if i == 2:
                diag2 = [board.state[1][5], board.state[2][4], board.state[3][3], board.state[4][2], board.state[5][1]]
            else:
                diagonal_counts.append(diag2.count(ai_symbol))

    max_row_count = max(row_counts)
    max_col_count = max(col_counts)
    max_diagonal_count = max(diagonal_counts)
    ai_score += max(max_row_count, max_col_count, max_diagonal_count) ** 2

    # Weight center points of segments
    if ai_score < 60:
        center_positions = [(1, 1), (1, 4), (4, 1), (4, 4)]
        for row, col in center_positions:
            if board.state[row][col] == ai_symbol:
                ai_score += max(max_row_count, max_col_count) ** 2 + 10 
            elif board.state[row][col] == user_symbol:
                user_score += max(max_row_count, max_col_count) ** 2 + 10

    #print("AI:", ai_score)
    return ai_score

def generate_legal_moves(board):
    legal_moves = []

    empty_squares = [(row, col) for row in range(6) for col in range(6) if board.state[row][col] == 0]

    if empty_squares:
        for row, col in empty_squares:
            for quadrant in range(4):
                for direction in [1, -1]:
                    new_board = board.copy()
                    if new_board.make_move(row, col, quadrant, 2, direction):
                        legal_moves.append(new_board)

    return legal_moves
