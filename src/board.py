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
        if not (0 <= row < 6 and 0 <= col < 6 and 0 <= quadrant <= 3):
            print("Invalid input!")
            return False
        if direction.lower() not in ["cw", "ccw"]:
            print("Invalid input!")
            return False
        if self.state[row][col] == "_":
            self.state[row][col] = "O" if player == 1 else "X"
        else:
            print("Position occupied!")
            return False
        if 0 <= quadrant < 4:
            if direction == "CW":
                self.rotate(quadrant, counterclockwise=False)
            elif direction == "CCW":
                self.rotate(quadrant, counterclockwise=True)
        return True

    def rotate(self, quadrant, counterclockwise: bool):
        row_start = (quadrant // 2) * 3
        col_start = (quadrant % 2) * 3

        rotated_segment = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                if not counterclockwise:
                    rotated_segment[i][j] = self.state[row_start + (2 - j)][col_start + i]
                else:
                    rotated_segment[i][j] = self.state[row_start + j][col_start + (2 - i)]

        for i in range(3):
            for j in range(3):
                self.state[row_start + i][col_start + j] = rotated_segment[i][j]

    def copy(self):
        new_board = PentagoBoard()
        new_board.state = [row[:] for row in self.state]
        return new_board


