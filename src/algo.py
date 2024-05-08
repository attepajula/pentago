from board import PentagoBoard
from math import inf
import time

def iterative_deepening(board, max_depth, time_limit):
    hash_table = {}
    best_move = None
    best_value = float('-inf')
    start_time = time.time()
    start_time_minimax = time.time()
    
    depth = 1
    
    while depth <= max_depth and time.time() - start_time < time_limit:
        while time.time() - start_time_minimax < time_limit:
            move, value = minimax(board, depth, hash_table)
            if value > best_value:
                best_value = value
                print("Value:", value)
                best_move = move
        depth += 1
        start_time_minimax = time.time()
    
    return best_move

def minimax(board, depth, hash_table, alpha=float('-inf'), beta=float('inf'), maximizingPlayer=True):
    if board in hash_table and hash_table[board][1] == depth:
        minimax(board, depth - 1, hash_table, alpha, beta, hash_table[board][2])
    
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
    
    hash_table[board] = (best_move, depth, maximizingPlayer)
    
    return best_move, best_value

def evaluate(board):
    ai_symbol = 2
    user_symbol = 1
    ai_score = 0
    user_score = 0
    row_counts = [0]
    col_counts = [0]
    diagonal_counts = [0]
    user_row_counts = [0]
    user_col_counts = [0]
    user_diagonal_counts = [0]

    for row in board.state:
        if user_symbol in row[1:5]:
            user_row_counts.append(row.count(user_symbol))
        elif user_symbol == row[0] and user_symbol == row[5] :
            pass
        else:
            row_counts.append(row.count(ai_symbol))

    for col in zip(*board.state):
        if user_symbol in col[1:5]:
            user_col_counts.append(col.count(user_symbol))
        elif user_symbol == col[0] and user_symbol == col[5] :
            pass
        else:
            col_counts.append(col.count(ai_symbol))

        # Top-left to bottom-right
        for i in range(3):
            if i == 0:
                diag1 = [board.state[1][0], board.state[2][1], board.state[3][2], board.state[4][3], board.state[5][4]]
                if user_symbol not in diag1:
                    diagonal_counts.append(diag1.count(user_symbol))
                else:
                    user_diagonal_counts.append(diag1.count(user_symbol))
            if i == 1:
                diag1 = [board.state[0][0], board.state[1][1], board.state[2][2], board.state[3][3], board.state[4][4], board.state[5][5]]
                if user_symbol in diag1[1:5]:
                    user_diagonal_counts.append(diag1.count(user_symbol))
                elif user_symbol == diag1[0] and user_symbol == diag1[5] :
                    pass
                else:
                    diagonal_counts.append(diag1.count(ai_symbol))
            if i == 2:
                diag1 = [board.state[0][1], board.state[1][2], board.state[2][3], board.state[3][4], board.state[4][5]]
                if user_symbol not in diag1:
                    diagonal_counts.append(diag1.count(ai_symbol))
                else:
                    user_diagonal_counts.append(diag1.count(user_symbol))
            
        # Top-right to bottom-left
        for i in range(3):
            if i == 0:
                diag2 = [board.state[0][4], board.state[1][3], board.state[2][2], board.state[3][1], board.state[4][0]]
                if user_symbol not in diag2:
                    diagonal_counts.append(diag2.count(ai_symbol))
                else:
                    user_diagonal_counts.append(diag1.count(user_symbol))
            if i == 1:
                diag2 = [board.state[0][5], board.state[1][4], board.state[2][3], board.state[3][2], board.state[4][1], board.state[5][0]]
                if user_symbol in diag2[1:5]:
                    user_diagonal_counts.append(diag2.count(user_symbol))
                elif user_symbol == diag2[0] and user_symbol == diag2[5] :
                    pass
                else:
                    diagonal_counts.append(diag2.count(ai_symbol))
            if i == 2:
                diag2 = [board.state[1][5], board.state[2][4], board.state[3][3], board.state[4][2], board.state[5][1]]
                if user_symbol not in diag2:
                    diagonal_counts.append(diag2.count(ai_symbol))
                else:
                    user_diagonal_counts.append(diag1.count(user_symbol))

    max_row_count = max(row_counts) ** 2
    max_col_count = max(col_counts) ** 2
    max_diagonal_count = max(diagonal_counts) ** 2

    ai_score += max(max_row_count, max_col_count, max_diagonal_count)

    # Problem somewhere down here!!! 
    # Weight center points of the board
    if ai_score < 10:
        center_positions = [(2, 2), (2, 3), (3, 2), (3, 3)]
        for row, col in center_positions:
            if board.state[row][col] == ai_symbol:
                ai_score += 1
            elif board.state[row][col] == user_symbol:
                user_score += 1

    # Weight center points of segments
    if max(max_row_count, max_col_count, max_diagonal_count) < 3:
        center_positions = [(1, 1), (1, 4), (4, 1), (4, 4)]
        for row, col in center_positions:
            if board.state[row][col] == ai_symbol:
                ai_score += ai_score + 10
            elif board.state[row][col] == user_symbol:
                user_score += 10

    max_user_row_count = max(user_row_counts)
    max_user_col_count = max(user_col_counts)
    max_user_diagonal_count = max(user_diagonal_counts)

    user_score += max(max_user_row_count, max_user_col_count, max_user_diagonal_count)

    #print("AI:", ai_score, "User:", user_score)
    return ai_score - user_score

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
