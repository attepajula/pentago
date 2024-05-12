class PentagoBoard:
    """
    This class represents a simple Pentago Board.

    Methods:
        print_board(self): Prints the board.
        make_move(self, row, col, quadrant, player, direction): Makes a move on a board state.
        rotate(self, quadrant, counterclockwise): Rotates a quadrant in a board state.
        copy(self): Copies board with all attributes.
        is_terminal(self): Determinates if the board is in terminal state.
    """
    def __init__(self):
        """Initializes a new instance of PentagoBoard.

        Attributes:
            state (list): Optional. Initial state of the board. Defaults to an empty 6x6 grid.
            terminal (int): Optional. Terminal state indicator. Defaults to 0.
        """
        self.state = [[0 for _ in range(6)] for _ in range(6)]
        self.terminal = 0

    def print_board(self):
        """Prints the current state of the board.

        Each cell is represented by "X" for AI (player 2),
        "O" for user (player 1), and "_" for an empty cell.
        """
        horizontal_line = "+---------+"
        print(horizontal_line)
        for row in self.state:
            row = " ".join(["X" if cell == 2 else "O" if cell == 1 else "_" for cell in row])
            print(row)
        print(horizontal_line)

    def make_move(self, row, col, quadrant, player, direction):
        """Makes a move on the board.

        Args:
            row (int): The row index of the cell to place the move (0 - 5).
            col (int): The column index of the cell to place the move (0 - 5).
            quadrant (int): The quadrant to rotate after placing the move (0 to 3).
            player (int): The player making the move (1 for user, 2 for the AI).
            direction (int): The direction of rotation (1 for clockwise, -1 for counterclockwise).

        Returns:
            bool: True if the move was successfully made, False otherwise (Position full or invalid input/inputs).
        """
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
        """Rotates a quadrant of the board.

        Args:
            quadrant (int): The quadrant to rotate (0 to 3).
            counterclockwise (bool): Whether to rotate counterclockwise (True) or clockwise (False).
        """
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
        """Copies the board.

        Returns:
            class (self): Copied board.
        """
        new_board = PentagoBoard()
        new_board.state = [row[:] for row in self.state]
        return new_board

    def is_terminal(self):
        """Determinates if the board (self) is in terminal state.
        Returns:
            int: self.terminal, 0 if not terminal, 1 if user wins, 2 if AI wins
            and 3 in case of board full or draw.
        """
        terminal_temp = [False, False, False]
        for i in range(6):
            for j in range(2):
                if self.state[i][j] == 1 and self.state[i][j] == self.state[i][j+1] == self.state[i][j+2] == self.state[i][j+3] == self.state[i][j+4]:
                    terminal_temp[1] = True
                if self.state[i][j] == 2 and self.state[i][j] == self.state[i][j+1] == self.state[i][j+2] == self.state[i][j+3] == self.state[i][j+4]:
                    terminal_temp[2] = True

        for i in range(2):
            for j in range(6):
                if self.state[i][j] == 1 and self.state[i][j] == self.state[i+1][j] == self.state[i+2][j] == self.state[i+3][j] == self.state[i+4][j]:
                    terminal_temp[1] = True
                if self.state[i][j] == 2 and self.state[i][j] == self.state[i+1][j] == self.state[i+2][j] == self.state[i+3][j] == self.state[i+4][j]:
                    terminal_temp[2] = True

        for i in range(2):
            for j in range(2):
                if self.state[i][j] == 1 and self.state[i][j] == self.state[i+1][j+1] == self.state[i+2][j+2] == self.state[i+3][j+3] == self.state[i+4][j+4]:
                    terminal_temp[1] = True
                if self.state[i][5-j] == 1 and self.state[i][5-j] == self.state[i+1][4-j] == self.state[i+2][3-j] == self.state[i+3][2-j] == self.state[i+4][1-j]:
                    terminal_temp[1] = True
                if self.state[i][j] == 2 and self.state[i][j] == self.state[i+1][j+1] == self.state[i+2][j+2] == self.state[i+3][j+3] == self.state[i+4][j+4]:
                    terminal_temp[2] = True
                if self.state[i][5-j] == 2 and self.state[i][5-j] == self.state[i+1][4-j] == self.state[i+2][3-j] == self.state[i+3][2-j] == self.state[i+4][1-j]:
                    terminal_temp[2] = True

        if 0 not in [symbol for row in self.state for symbol in row]:
            terminal_temp[0] = True
            self.terminal = 3

        if terminal_temp[1] == True:
            self.terminal = 1
        elif terminal_temp[2] == True:
            self.terminal = 2
        
        if terminal_temp[1] == True and terminal_temp[2] == True:
            self.terminal = 3

        return self.terminal
