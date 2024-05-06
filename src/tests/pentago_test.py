import unittest
from unittest.mock import patch
from io import StringIO
from pentago import your_turn, play

class TestPentagoGame(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, moves, mock_stdout):
        with patch('builtins.input', side_effect=moves):
            play()
            self.assertNotEqual(mock_stdout.getvalue(), "")

    def assert_stdout(self, moves, expected_output):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', side_effect=moves):
                play()
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=['1', '1', '1', 'CW'])
    def test_your_turn_valid_input(self, mock_input):
        expected_output = [0, 0, 0, 'CW']
        self.assertEqual(your_turn(), expected_output)

if __name__ == '__main__':
    unittest.main()
