import unittest
from unittest.mock import patch
import io
from pentago import your_turn, play
from board import PentagoBoard

class TestPentagoGame(unittest.TestCase):
    def setUp(self):
        self.board = PentagoBoard()

    @patch('builtins.input', side_effect=['1', '1', '1', 'CW'])
    def test_your_turn_valid_input(self, mock_input):
        expected_output = [0, 0, 0, 1]
        self.assertEqual(your_turn(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, null, expected_output, mock_stdout):
        with patch('builtins.input', side_effect=null):
            play()
            self.assertEqual(mock_stdout.getvalue(), expected_output)
            
if __name__ == "__main__":
    unittest.main()

if __name__ == '__main__':
    unittest.main(buffer=False)
