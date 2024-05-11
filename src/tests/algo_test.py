import unittest
from algo import minimax, generate_legal_moves, evaluate, evaluate_line
from board import PentagoBoard

class TestPentagoGame(unittest.TestCase):
    def setUp(self):
        self.board = PentagoBoard()

    def test_generate_legal_moves(self):
        legal_moves = generate_legal_moves(self.board, True)
        self.assertTrue(legal_moves)

    def test_minimax(self):
        best_move = minimax(self.board, depth=0, max_depth=2, maximizingPlayer=True)
        self.assertTrue(best_move)

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
        assert evaluate_line([2, 2, 2, 0, 0, 0]) == 9
        assert evaluate_line([1, 1, 1, 0, 0]) == -10  # User has 3 in a row
        assert evaluate_line([1, 1, 1, 1, 1, 0]) == -10  # User has 5 in a row
        assert evaluate_line([1, 2, 1, 0, 0]) == -1  # Invalid move for AI
        assert evaluate_line([2, 2, 0, 0, 0]) == 4  # AI has two in a row
        assert evaluate_line([1, 1, 2, 0, 0]) == -1 # Wrong move
        assert evaluate_line([0, 0, 2, 1, 0]) == -1 # Wrong move
        assert evaluate_line([2, 2, 0, 0, 0]) == 4  # AI has two in a row
        assert evaluate_line([1, 2, 2, 0, 0, 0]) == 4  # AI has two in a row
        assert evaluate_line([0, 2, 2, 0, 0, 1]) == 4  # AI has two in a row
        assert evaluate_line([0, 2, 2, 0, 0, 1]) == 4  # AI has two in a row
        assert evaluate_line([0, 2, 2, 0, 1, 1]) == -1  # Wrong move
        assert evaluate_line([0, 0, 0, 0, 0]) == 0  # Empty line

if __name__ == '__main__':
    unittest.main()
