import unittest
from algo import minimax, generate_legal_moves, evaluate, evaluate_line
from board import PentagoBoard

class TestPentagoGame(unittest.TestCase):
    """This class contains unit tests for the Pentago game AI and board evaluation functions.

    The TestPentagoGame class includes test cases to ensure the correctness of the following functionalities:
    - Generating legal moves
    - Implementing the minimax algorithm for AI decision-making
    - Handling different board states, including empty, AI winning, and user winning states
    - Evaluating the board state and individual lines for heuristic scoring
    """
    def setUp(self):
        self.board = PentagoBoard()

    def test_generate_legal_moves(self):
        legal_moves = generate_legal_moves(self.board, True)
        self.assertTrue(legal_moves)

    def test_minimax(self):
        best_move = minimax(self.board, depth=0, max_depth=2, maximizingPlayer=True)
        self.assertTrue(best_move)

    def test_minimax_empty_board(self):
        self.board.state = [[0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]
        
        best_move = minimax(self.board, depth=0, max_depth=2, maximizingPlayer=True)
        assert best_move[1] == 1

    def test_minimax_ai_starts(self):
        self.board.state = [[0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 2, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]
        
        best_move = minimax(self.board, depth=0, max_depth=2, maximizingPlayer=True)
        assert best_move[1] > 0

    def test_minimax_never_wrong_move_rows(self):
        # The goal is not to get a row of five for the user
        # A row of four is allowed, when it can be blocked from both ends.
        for i in range(6):
            for j in range(4):
                self.board.state[i][j] = 1
                self.board.state[i][j+1] = 1
                self.board.state[i][j+2] = 1
                best_move = minimax(self.board, depth=0, max_depth=2, maximizingPlayer=True)
                assert best_move[1]  != -100000 # A row of five is always -100000

                self.board.state = [[0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0]]
                
    def test_minimax_never_wrong_move_cols(self):
        # The goal is not to get a row of five for the user
        # A row of four is allowed, when it can be blocked from both ends.
        for i in range(4):
            for j in range(6):
                self.board.state[i][j] = 1
                self.board.state[i+1][j] = 1
                self.board.state[i+2][j] = 1
                best_move = minimax(self.board, depth=0, max_depth=2, maximizingPlayer=True)
                assert best_move[1] != -100000 # A row of five is always -100000

                self.board.state = [[0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0]]

    def test_minimax_end_ai_turn(self):
        self.board.state = [[1, 1, 2, 1, 1, 2],
                            [2, 1, 2, 2, 2, 1],
                            [2, 1, 1, 1, 1, 2],
                            [1, 2, 2, 0, 2, 2],
                            [2, 1, 2, 1, 2, 1],
                            [1, 1, 1, 2, 2, 1]]
        
        best_move = minimax(self.board, depth=0, max_depth=2, maximizingPlayer=True)
        assert best_move[1] >= 25 # User's row of four declines total evaluation score by 10000

    def test_minimax_user_first(self):
        self.board.state = [[0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 1, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]
        
        best_move = minimax(self.board, depth=0, max_depth=2, maximizingPlayer=True)
        assert best_move[1] < 0

    def test_minimax_ai_in_trouble1(self):
        self.board.state = [[0, 0, 0, 0, 0, 0],
                            [2, 1, 0, 1, 0, 0],
                            [0, 0, 0, 1, 0, 0],
                            [0, 2, 0, 1, 0, 0],
                            [0, 2, 1, 1, 2, 0],
                            [0, 0, 0, 0, 0, 0]]
        
        best_move = minimax(self.board, depth=0, max_depth=2, maximizingPlayer=True)
        assert best_move[1] == -100000

    def test_minimax_ai_in_trouble2(self):
        self.board.state = [[0, 0, 0, 0, 0, 0],
                            [2, 1, 2, 0, 0, 0],
                            [0, 0, 0, 1, 0, 0],
                            [0, 2, 0, 1, 0, 0],
                            [0, 2, 1, 1, 2, 0],
                            [0, 0, 0, 0, 0, 0]]
        
        best_move = minimax(self.board, depth=0, max_depth=2, maximizingPlayer=True)
        assert best_move[1] < 0

    def test_minimax_ai_has_solved_the_problem(self):
        self.board.state = [[0, 0, 0, 0, 0, 0],
                            [2, 1, 0, 2, 0, 0],
                            [0, 0, 0, 1, 0, 0],
                            [0, 2, 0, 1, 0, 0],
                            [0, 2, 1, 1, 2, 0],
                            [0, 0, 0, 0, 0, 0]]
        
        best_move = minimax(self.board, depth=0, max_depth=2, maximizingPlayer=True)
        assert best_move[1] == -5

    def test_terminal_state(self):
        self.board.state = [[2, 2, 2, 2, 2, 2],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]
        self.assertTrue(self.board.is_terminal())

    def test_evaluate(self):
        # Test case 3: Empty board
        self.board.state = [[0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]
        assert evaluate(self.board) == 0

        # Test case 1: AI wins
        self.board.state = [[2, 2, 2, 2, 2, 2],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]
        assert evaluate(self.board) >= 10000

        # Test case 2: User wins
        self.board.state = [[1, 1, 1, 1, 1, 0],
                            [0, 2, 0, 0, 0, 2],
                            [0, 0, 2, 0, 2, 0],
                            [0, 0, 0, 2, 0, 0],
                            [0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0]]
        assert evaluate(self.board) == -100000

    def test_evaluate_line(self):
        assert evaluate_line([2, 2, 2, 0, 0, 0]) == (9, 0)
        assert evaluate_line([1, 1, 1, 0, 0]) == (0, 9) # User has 3 in a row
        assert evaluate_line([1, 1, 1, 1, 1, 0]) == (0, 25) # User has 5 in a row
        assert evaluate_line([1, 2, 1, 0, 0]) == (0, 0)  # Invalid move for AI
        assert evaluate_line([2, 2, 0, 0, 0]) == (4, 0)  # AI has two in a row
        assert evaluate_line([1, 1, 2, 0, 0]) == (0, 0) # Wrong move
        assert evaluate_line([0, 0, 2, 1, 0]) == (0, 0) # Wrong move
        assert evaluate_line([2, 2, 0, 0, 0]) == (4, 0)  # AI has two in a row
        assert evaluate_line([1, 2, 2, 0, 0, 0]) == (4, 0)  # AI has two in a row
        assert evaluate_line([0, 2, 2, 0, 0, 1]) == (4, 0)  # AI has two in a row
        assert evaluate_line([0, 2, 2, 0, 0, 1]) == (4, 0)  # AI has two in a row
        assert evaluate_line([0, 2, 2, 0, 1, 1]) == (0, 0)  # Wrong move
        assert evaluate_line([0, 0, 0, 0, 0]) == (0, 0)  # Empty line

if __name__ == '__main__':
    unittest.main()
