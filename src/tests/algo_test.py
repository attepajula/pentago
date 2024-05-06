import unittest
from unittest.mock import patch
from io import StringIO
from algo import generate_legal_moves, minimax
from board import PentagoBoard
from pentago import play, your_turn

class TestPentagoGame(unittest.TestCase):
    def setUp(self):
        self.board = PentagoBoard()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, moves, expected_output, mock_stdout):
        with patch('builtins.input', side_effect=moves):
            play()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_generate_legal_moves(self):
        legal_moves = generate_legal_moves(self.board)
        self.assertTrue(legal_moves)

    def test_minimax(self):
        best_move = minimax(self.board, depth=2)
        self.assertTrue(best_move)

    def test_terminal_state(self):
        self.board.state = [['O', 'O', 'O', 'O', 'O', '_'],
                            ['_', '_', '_', '_', '_', '_'],
                            ['_', '_', '_', '_', '_', '_'],
                            ['_', '_', '_', '_', '_', '_'],
                            ['_', '_', '_', '_', '_', '_'],
                            ['_', '_', '_', '_', '_', '_']]
        self.assertTrue(self.board.is_terminal())


if __name__ == '__main__':
    unittest.main()

