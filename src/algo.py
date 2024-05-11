from math import inf
from board import PentagoBoard

def minimax(board, depth, max_depth, maximizingPlayer, alpha=float('-inf'), beta=float('inf'),):
    """Uses the minimax algorithm with alpha-beta pruning to determine the best move for the AI on a given board/future move.

    Args:
        board (Board): At first call the current game board, then a move from a list.
        depth (int): Current depth in the search tree.
        max_depth (int): Maximum depth to search.
        maximizingPlayer (bool): Indicates whether the AI is maximizing or minimizing.
        alpha (float, optional): The best value that the maximizing player currently can guarantee at this level or above.
                                 Defaults to negative infinity.
        beta (float, optional): The best value that the minimizing player currently can guarantee at this level or above.
                                Defaults to positive infinity.
    
    Returns:
        tuple: A tuple containing the best move (a board state) and its corresponding value.
    """
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
    """Evaluates the value of a move for the given board state.

    Args:
        board (Board): The game board/future move.

    Returns:
        int: The evaluation score of the move for the AI player.
    """
    ai_symbol = 2
    user_symbol = 1
    ai_score = 0
    user_score = 0
    row_counts = [(0, 0)]
    col_counts = [(0, 0)]
    diagonal_counts = [(0, 0)]

    diagsL = [[board.state[1][0], board.state[2][1], board.state[3][2], board.state[4][3], board.state[5][4]],
            [board.state[0][0], board.state[1][1], board.state[2][2], board.state[3][3], board.state[4][4], board.state[5][5]],
            [board.state[0][1], board.state[1][2], board.state[2][3], board.state[3][4], board.state[4][5]]]
    
    diagsR = [[board.state[0][4], board.state[1][3], board.state[2][2], board.state[3][1], board.state[4][0]],
            [board.state[0][5], board.state[1][4], board.state[2][3], board.state[3][2], board.state[4][1], board.state[5][0]],
            [board.state[1][5], board.state[2][4], board.state[3][3], board.state[4][2], board.state[5][1]]]
    
    for row in board.state:
        row_counts.append(evaluate_line(row))

    for col in zip(*board.state):
        col_counts.append(evaluate_line(col))

    for diag in diagsL:
        diagonal_counts.append(evaluate_line(diag))

    for diag in diagsR:
        diagonal_counts.append(evaluate_line(diag))

    max_row_count = max(t[0] for t in row_counts)
    max_col_count = max(t[0] for t in col_counts)
    max_diagonal_count = max(t[0] for t in diagonal_counts)
    ai_score += max(max_row_count, max_col_count, max_diagonal_count)

    max_row_count_user = max(t[1] for t in row_counts)
    max_col_count_user = max(t[1] for t in col_counts)
    max_diagonal_count_user = max(t[1] for t in diagonal_counts)
    user_score += max(max_row_count_user, max_col_count_user, max_diagonal_count_user)

    if board.is_terminal() == user_symbol: # User is winning
        return -100000
    
    if board.is_terminal() == ai_symbol:
        ai_score += 10000
    
    # Weight center points of segments
    if max(max_row_count, max_col_count, max_diagonal_count) < 3:
        center_positions = [(1, 1), (1, 4), (4, 1), (4, 4)]
        for row, col in center_positions:
            if board.state[row][col] == ai_symbol:
                ai_score += ai_score + 10
            elif board.state[row][col] == user_symbol:
                user_score += 10

    return ai_score - user_score

def evaluate_line(line):
    """Evaluates the counts of AI and user symbols in a line. The line is interrupted, 
    if the five same symbols can't occur uninterrupted.

    Args:
        line (list): A list representing a row, column, or diagonal in the game board.

    Returns:
        tuple: A tuple containing the squared (weighted) uninterrupted counts of AI and user symbols in line.
    """
    ai_symbol = 2
    user_symbol = 1
    ai_counter = 0
    user_counter = 0

    if len(line) == 6:
        if user_symbol not in line:
            ai_counter = line.count(ai_symbol)
        elif user_symbol == line[0] and user_symbol not in line[1:]:
            ai_counter = line.count(ai_symbol)
        elif user_symbol == line[5] and user_symbol not in line[:5]:
            ai_counter = line.count(ai_symbol)

        if ai_symbol not in line:
            user_counter = line.count(user_symbol)
        elif ai_symbol == line[0] and ai_symbol not in line[1:]:
            user_counter = line.count(user_symbol)
        elif ai_symbol == line[5] and ai_symbol not in line[:5]:
            user_counter = line.count(user_symbol)

    else: # line lenght == 5:
        if user_symbol not in line:
            ai_counter = line.count(ai_symbol)
        elif ai_symbol not in line:
            user_counter =  line.count(user_symbol)
        
    return (ai_counter ** 2, user_counter ** 2)

def generate_legal_moves(board, maximizingPlayer):
    """Generates all legal moves for the AI (maximizingPlayer or not) on the given board.

    Args:
        board (Board): The game board/future move.
        maximizingPlayer (bool): Indicates whether the AI is maximizing or minimizing.

    Returns:
        list: A list of legal moves, each represented as a tuple containing the row, column, quadrant, player, and direction.
    """
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
