class PentagoBoard:
    def __init__(self):
        self.state = [["_" for _ in range(6)] for _ in range(6)]
        self.is_terminal = False
        self.legal_moves = []

    def print_board(self):
        for row in self.state:
            print(' '.join(map(str, row)))
        print()

    def make_move(self, row, col, quadrant, player, direction): 
        if self.state[row][col] == "_":
            self.state[row][col] = "O" if player == 1 else "X"
        else:
            print("Position occupied!")
            return
        if 0 <= quadrant < 4:
            if direction == "CW":
                self.rotate_clockwise(quadrant)
            elif direction == "CCW":
                self.rotate_counterclockwise(quadrant)

    def rotate_clockwise(self, quadrant):
        row_start = (quadrant // 2) * 3
        col_start = (quadrant % 2) * 3
        rotated_segment = [list(row) for row in zip(*self.state[row_start:row_start + 3][::-1])]
        for i in range(3):
            for j in range(3):
                self.state[row_start + i][col_start + j] = rotated_segment[i][j]

    def rotate_counterclockwise(self, quadrant):
        row_start = (quadrant // 2) * 3
        col_start = (quadrant % 2) * 3
        rotated_segment = [list(row) for row in zip(*self.state[row_start:row_start + 3])]
        for i in range(3):
            for j in range(3):
                self.state[row_start + i][col_start + j] = rotated_segment[j][i]

    def copy(self):
        new_board = PentagoBoard()
        new_board.state = [row[:] for row in self.state]
        return new_board


