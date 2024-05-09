from board import PentagoBoard
from math import inf

def minimax(board, depth, max_depth, maximizingPlayer, alpha=float('-inf'), beta=float('inf'),):
    if depth == max_depth or board.is_terminal():
        return None, evaluate(board)
    
    best_move = None
    best_value = float('-inf') if maximizingPlayer else float('inf')
    
    if maximizingPlayer:
        for i in generate_legal_moves(board, maximizingPlayer):
            row, col, quadrant, player, direction = i
            new_board = board.copy()
            new_board.make_move(row, col, quadrant, player, direction)
            _, value = minimax(new_board, depth + 1, max_depth, False, alpha, beta)
            if value > best_value:
                best_value = value
                best_move = new_board
            alpha = max(alpha, best_value)
            if best_value > alpha:
                break
    else:
        for i in generate_legal_moves(board, maximizingPlayer):
            row, col, quadrant, player, direction = i
            new_board = board.copy()
            new_board.make_move(row, col, quadrant, player, direction)
            _, value = minimax(new_board, depth + 1, max_depth, True, alpha, beta)
            if value < best_value:
                best_value = value
                best_move = new_board
            beta = min(beta, best_value)
            if best_value < alpha:
                break

    return best_move, best_value

def evaluate(board):
    ai_symbol = 2
    user_symbol = 1
    ai_score = 0
    user_score = 0
    row_counts = [0]
    col_counts = [0]
    diagonal_counts = [0]

    diagsL = [[board.state[1][0], board.state[2][1], board.state[3][2], board.state[4][3], board.state[5][4]],
            [board.state[0][0], board.state[1][1], board.state[2][2], board.state[3][3], board.state[4][4], board.state[5][5]],
            [board.state[0][1], board.state[1][2], board.state[2][3], board.state[3][4], board.state[4][5]]]
    
    diagsR = [[board.state[0][4], board.state[1][3], board.state[2][2], board.state[3][1], board.state[4][0]],
            [board.state[0][5], board.state[1][4], board.state[2][3], board.state[3][2], board.state[4][1], board.state[5][0]],
            [board.state[1][5], board.state[2][4], board.state[3][3], board.state[4][2], board.state[5][1]]]


    for row in board.state:
        temp = 0
        for i in row:
            if i == ai_symbol:
                temp += 1
            elif i == user_symbol:
                temp = 0
                break
        row_counts.append(temp)

    for col in zip(*board.state):
        temp = 0
        for i in col:
            if i == ai_symbol:
                temp += 1
            elif i == user_symbol:
                temp = 0
                break
        col_counts.append(temp)

    for diag in diagsL:
        temp = 0
        for i in diag:
            if i == ai_symbol:
                temp += 1
            elif i == user_symbol:
                temp = 0
                break
        diagonal_counts.append(temp)

    for diag in diagsR:
        temp = 0
        for i in diag:
            if i == ai_symbol:
                temp += 1
            elif i == user_symbol:
                temp = 0
                break
        diagonal_counts.append(temp)
 
    max_row_count = max(row_counts) ** 2
    max_col_count = max(col_counts) ** 2
    max_diagonal_count = max(diagonal_counts) ** 2

    ai_score += max(max_row_count, max_col_count, max_diagonal_count)
    if board.is_terminal() == user_symbol:
        user_score = 10000
        return ai_score - user_score
    
    if board.is_terminal() == ai_symbol:
        ai_score = 10000
        return ai_score - user_score

    # Weight center points of segments
    if max(max_row_count, max_col_count, max_diagonal_count) < 3:
        center_positions = [(1, 1), (1, 4), (4, 1), (4, 4)]
        for row, col in center_positions:
            if board.state[row][col] == ai_symbol:
                ai_score += ai_score + 10
            elif board.state[row][col] == user_symbol:
                user_score += 10

    return ai_score - user_score

def generate_legal_moves(board, maximizingPlayer):
    legal_moves = []
    seq = [4, 1, 2, 3, 0, 5]

    empty_squares = [(row, col) for row in seq for col in seq if board.state[row][col] == 0]

    if empty_squares:
        for row, col in empty_squares:
            for quadrant in range(4):
                for direction in [1, -1]:
                    if maximizingPlayer:
                        legal_moves.append((row, col, quadrant, 2, direction))
                    else:
                        legal_moves.append((row, col, quadrant, 1, direction))

    return legal_moves
