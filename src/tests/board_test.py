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

    def test_is_terminal_user(self):
        self.board.state = [
            [2, 2, 2, 2, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.board.is_terminal()
        assert self.board.terminal == 1

    def test_is_terminal_ai(self):
        self.board.state = [
            [2, 2, 2, 2, 2, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        self.board.is_terminal()
        assert self.board.terminal == 2

    def test_is_terminal_full(self):
        self.board.state = [
            [2, 1, 2, 2, 1, 2],
            [1, 2, 1, 1, 2, 1],
            [2, 1, 2, 2, 1, 2],
            [1, 2, 1, 1, 2, 1],
            [2, 1, 2, 2, 1, 2],
            [1, 2, 1, 1, 2, 1]
        ]
        self.board.is_terminal()
        assert self.board.terminal == 3

    def test_is_terminal_user_all_rows(self):
        for i in range(6):
            for j in range(2):
                self.board.state[i][j] = 1 
                self.board.state[i][j+1] = 1
                self.board.state[i][j+2] = 1
                self.board.state[i][j+3] = 1
                self.board.state[i][j+4] = 1

            self.board.is_terminal()
            assert self.board.terminal == 1
            
            for h in range(6):
                self.board.state[i][h] = 0

    def test_is_terminal_ai_all_rows(self):
        for i in range(6):
            for j in range(2):
                self.board.state[i][j] = 2
                self.board.state[i][j+1] = 2
                self.board.state[i][j+2] = 2
                self.board.state[i][j+3] = 2
                self.board.state[i][j+4] = 2

            self.board.is_terminal()
            assert self.board.terminal == 2
            
            for h in range(6):
                self.board.state[i][h] = 0

    def test_is_terminal_user_all_cols(self):
        for i in range(2):
            for j in range(6):
                self.board.state[i][j] = 1
                self.board.state[i+1][j] = 1
                self.board.state[i+2][j] = 1
                self.board.state[i+3][j] = 1
                self.board.state[i+4][j] = 1

            self.board.is_terminal()
            assert self.board.terminal == 1
            
            for h in range(6):
                self.board.state[i][h] = 0

    def test_is_terminal_ai_all_cols(self):
        for i in range(2):
            for j in range(6):
                self.board.state[i][j] = 2
                self.board.state[i+1][j] = 2
                self.board.state[i+2][j] = 2
                self.board.state[i+3][j] = 2
                self.board.state[i+4][j] = 2

            self.board.is_terminal()
            assert self.board.terminal == 2
            
            for h in range(6):
                self.board.state[i][h] = 0

    def test_is_terminal_user_all_diags(self):
        for i in range(2):
            for j in range(2):
                self.board.state[i][j] = 1
                self.board.state[i+1][j+1] = 1
                self.board.state[i+2][j+2] = 1
                self.board.state[i+3][j+3] = 1
                self.board.state[i+4][j+4] = 1

            self.board.is_terminal()
            assert self.board.terminal == 1
            
            for g in range(6):
                for h in range(6):
                    self.board.state[i][h] = 0

            for j in range(2):
                self.board.state[i][j-5] = 1
                self.board.state[i+1][j-4] = 1
                self.board.state[i+2][j-3] = 1
                self.board.state[i+3][j-2] = 1
                self.board.state[i+4][j-1] = 1

            self.board.is_terminal()
            assert self.board.terminal == 1

            for g in range(6):
                for h in range(6):
                    self.board.state[i][h] = 0

    def test_is_terminal_ai_all_diags(self):
        for i in range(2):
            for j in range(2):
                self.board.state[i][j] = 2
                self.board.state[i+1][j+1] = 2
                self.board.state[i+2][j+2] = 2
                self.board.state[i+3][j+3] = 2
                self.board.state[i+4][j+4] = 2

            self.board.is_terminal()
            assert self.board.terminal == 2
            
            for g in range(6):
                for h in range(6):
                    self.board.state[i][h] = 0

            for j in range(2):
                self.board.state[i][j-5] = 2
                self.board.state[i+1][j-4] = 2
                self.board.state[i+2][j-3] = 2
                self.board.state[i+3][j-2] = 2
                self.board.state[i+4][j-1] = 2

            self.board.is_terminal()
            assert self.board.terminal == 2

            for g in range(6):
                for h in range(6):
                    self.board.state[i][h] = 0
                
if __name__ == '__main__':
    unittest.main()
