from board import PentagoBoard
from math import inf

def minimax(board, depth, maximizingPlayer):
    if depth == 0 or board.is_terminal:
        return evaluate(board)

    if maximizingPlayer:
        maxEval = -inf
        for move in generate_legal_moves(board):
            eva = minimax(move, depth - 1, False)
            maxEval = max(maxEval, eva)
        return maxEval
    else:
        minEval = inf
        for move in generate_legal_moves(board):
            eva = minimax(move, depth - 1, True)
            minEval = min(minEval, eva)
        return minEval
    
def evaluate(board):
    player_symbol = "O"
    opponent_symbol = "X"
    player_score = 0
    opponent_score = 0

    for i in range(6):
        row = ''.join(board.state[i])
        col = ''.join([board.state[j][i] for j in range(6)])
        player_score += row.count(player_symbol) + col.count(player_symbol)
        opponent_score += row.count(opponent_symbol) + col.count(opponent_symbol)

    for i in range(-2, 4):
        diag1 = ''.join([board.state[i + j][j] for j in range(max(0, -i), min(6, 6 - i))])
        diag2 = ''.join([board.state[j][i + j] for j in range(max(0, -i), min(6, 6 - i))])
        diag3 = ''.join([board.state[5 - j][i + j] for j in range(max(0, -i), min(6, 6 - i))])
        diag4 = ''.join([board.state[5 - i - j][j] for j in range(max(0, -i), min(6, 6 - i))])
        player_score += diag1.count(player_symbol) + diag2.count(player_symbol) + diag3.count(player_symbol) + diag4.count(player_symbol)
        opponent_score += diag1.count(opponent_symbol) + diag2.count(opponent_symbol) + diag3.count(opponent_symbol) + diag4.count(opponent_symbol)

    return player_score - opponent_score


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
