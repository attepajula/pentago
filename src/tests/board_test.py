import unittest
from board import PentagoBoard

class TestPentagoBoard(unittest.TestCase):
    def setUp(self):
        self.board = PentagoBoard()

    def test_initial_state(self):
        self.assertEqual(len(self.board.state), 6)
        for row in self.board.state:
            self.assertEqual(len(row), 6)
            self.assertTrue(all(cell == '_' for cell in row))

    def test_make_move(self):
        self.assertTrue(self.board.make_move(0, 0, 0, 1, "cw"))
        self.assertEqual(self.board.state[0][0], "O")
        self.assertTrue(self.board.make_move(0, 1, 1, 2, "ccw"))
        self.assertEqual(self.board.state[0][1], "X")

    def test_rotate_clockwise(self):
        self.board.state = [
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '0', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_']
        ]
        self.board.rotate(0, counterclockwise=False)
        expected_state = [
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['0', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_']
        ]
        self.assertEqual(self.board.state, expected_state)

    def test_rotate_counterclockwise(self):
        self.board.state = [
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['0', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_']
        ]
        self.board.rotate(0, counterclockwise=True)
        expected_state = [
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '0', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_'], 
            ['_', '_', '_', '_', '_', '_']
        ]
        self.assertEqual(self.board.state, expected_state)

if __name__ == '__main__':
    unittest.main()
