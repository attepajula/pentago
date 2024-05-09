class PentagoBoard:
    def __init__(self):
        self.state = [[0 for _ in range(6)] for _ in range(6)]
        self.terminal = 0
        self.legal_moves = []

    def print_board(self):
        horizontal_line = "+---------+"
        print(horizontal_line)
        for row in self.state:
            row = " ".join(["X" if cell == 2 else "O" if cell == 1 else "_" for cell in row])
            print(row)
        print(horizontal_line)


    def make_move(self, row, col, quadrant, player, direction): 
        if not (0 <= row < 6 and 0 <= col < 6 and 0 <= quadrant <= 3):
            print("Invalid input!")
            return False
        if direction not in [1, -1]:
            print("Invalid input!")
            return False
        if self.state[row][col] == 0:
            self.state[row][col] = 1 if player == 1 else 2
        else:
            print("Position occupied!")
            return False
        if 0 <= quadrant < 4:
            if direction == 1:
                self.rotate(quadrant, counterclockwise=False)
            elif direction == -1:
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
    
    def is_terminal(self):
        for i in range(6):
            for j in range(2):
                if self.state[i][j] == 1 and self.state[i][j] == self.state[i][j+1] == self.state[i][j+2] == self.state[i][j+3] == self.state[i][j+4]:
                    self.terminal = 1
                if self.state[i][j] == 2 and self.state[i][j] == self.state[i][j+1] == self.state[i][j+2] == self.state[i][j+3] == self.state[i][j+4]:
                    self.terminal = 2

        for i in range(2):
            for j in range(6):
                if self.state[i][j] == 1 and self.state[i][j] == self.state[i+1][j] == self.state[i+2][j] == self.state[i+3][j] == self.state[i+4][j]:
                    self.terminal = 1
                if self.state[i][j] == 2 and self.state[i][j] == self.state[i+1][j] == self.state[i+2][j] == self.state[i+3][j] == self.state[i+4][j]:
                    self.terminal = 2

        for i in range(2):
            for j in range(2):
                if self.state[i][j] == 1 and self.state[i][j] == self.state[i+1][j+1] == self.state[i+2][j+2] == self.state[i+3][j+3] == self.state[i+4][j+4]:
                    self.terminal = 1
                if self.state[i][5-j] == 1 and self.state[i][5-j] == self.state[i+1][4-j] == self.state[i+2][3-j] == self.state[i+3][2-j] == self.state[i+4][1-j]:
                    self.terminal = 1
                if self.state[i][j] == 2 and self.state[i][j] == self.state[i+1][j+1] == self.state[i+2][j+2] == self.state[i+3][j+3] == self.state[i+4][j+4]:
                    self.terminal = 2
                if self.state[i][5-j] == 2 and self.state[i][5-j] == self.state[i+1][4-j] == self.state[i+2][3-j] == self.state[i+3][2-j] == self.state[i+4][1-j]:
                    self.terminal = 2

        if 0 not in [symbol for row in self.state for symbol in row]:
            self.terminal = 3

        return self.terminal