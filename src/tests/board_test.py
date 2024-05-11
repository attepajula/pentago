import unittest
from board import PentagoBoard

class TestPentagoBoard(unittest.TestCase):
    def setUp(self):
        self.board = PentagoBoard()

    def test_initial_state(self):
        self.assertEqual(len(self.board.state), 6)
        for row in self.board.state:
            self.assertEqual(len(row), 6)
            self.assertTrue(all(cell == 0 for cell in row))

    def test_make_move(self):
        self.assertTrue(self.board.make_move(0, 0, 2, 1, 1))
        self.assertEqual(self.board.state[0][0], 1)
        self.assertTrue(self.board.make_move(0, 1, 0, 2, -1))
        self.assertEqual(self.board.state[1][0], 2)

    def test_rotate_clockwise(self):
        self.board.state = [
            [2, 2, 2, 2, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 2, 0, 2, 2, 2],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.board.rotate(0, counterclockwise=False)
        self.board.rotate(1, counterclockwise=False)
        self.board.rotate(2, counterclockwise=False)
        self.board.rotate(3, counterclockwise=False)
        expected_state = [
            [0, 0, 2, 0, 0, 2],
            [0, 0, 2, 0, 0, 0],
            [0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 2],
            [0, 1, 2, 0, 0, 2],
            [0, 0, 0, 0, 0, 2]
        ]
        self.assertEqual(self.board.state, expected_state)

    def test_rotate_counterclockwise(self):
        self.board.state = [
            [2, 2, 2, 2, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.board.rotate(0, counterclockwise=True)
        self.board.rotate(1, counterclockwise=True)
        self.board.rotate(2, counterclockwise=True)
        self.board.rotate(3, counterclockwise=True)
        expected_state = [
            [2, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0],
            [2, 0, 0, 2, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(self.board.state, expected_state)

if __name__ == '__main__':
    unittest.main()
