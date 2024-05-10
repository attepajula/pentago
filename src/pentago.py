from board import *
from algo import *
from random import randint
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep

class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)


def your_turn():
    # Your turn
    row = int(input("Choose row (1-6): ")) - 1
    col = int(input("Choose column (1-6): ")) - 1
    quadrant = int(input("Choose quarter (1-4): ")) - 1
    directionInput = input("Choose direction (CW or CCW): ").upper()
    if directionInput == "CW":
        direction = 1
    elif directionInput == "CCW":
        direction = -1
    else:
        direction = None

    return [row, col, quadrant, direction]

def play():
    board = PentagoBoard()
    current_player = randint(1, 2)

    print("Welcome playing Pentago!\n")
    board.print_board()

    # Main loop
    while board.terminal == 0:
        if current_player == 1:
            print("Your turn:")
            while True:
                # Your turn
                try:
                    moves = your_turn()
                    if board.make_move(moves[0], moves[1], moves[2], current_player, moves[3]):
                        break
                except(ValueError):
                    print("Invalid input!")

        if current_player == 2:
            print("Machine makes a move:")
            loader = Loader("Making move...", "").start()
            best_move = minimax(board, depth=0, max_depth=2, maximizingPlayer=True)[0]
            if best_move:
                board = best_move
            loader.stop()
        board.is_terminal()
        board.print_board()

        # Change turns
        current_player = 2 if current_player == 1 else 1

    print("Game over!")