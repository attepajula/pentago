ChatGPT (3.5) was used for structure implementation idea and debugging.

The src/pentago.py defines a game of Pentago where the player faces an AI opponent. It imports a custom PentagoBoard class from board.py and a minimax algorithm from algo.py for the AI's decision-making. The game loop alternates between the player's and AI's turns until a terminal condition is reached. During the player's turn, they input their moves via the keyboard, while the AI's moves are determined using the minimax algorithm. The game's progress and the board state are displayed after each turn. The game ends when a player wins or the board reaches a draw condition.

The src/algo.py implements the Minimax algorithm with alpha-beta pruning for the game of Pentago. The minimax function recursively searches the game tree to determine the best move for the AI player. The evaluate function assigns a score to each potential move based on the current board state, favoring moves that maximize the AI's chances of winning. The evaluate_line function calculates the weighted counts of AI and user symbols in a line considering interruptions. The generate_legal_moves function generates all legal moves for the AI player on the given board/future recursive move.

Minimax is the most time-intense part of the app. It's time complexity with optimal pruning alpha-beta is $O(b^{(d/2)})$, where $b = {36 \cdot 4 \cdot 2}$ and $d = 3$. Additionaly, a time complexity of evaluation process is $O(n)$.

The evaluation function uses a quite aggressive defence tactic. Without the defence the algorithm can lose the game very quickly, if the user gets a row of four symbols in very beginning. This is due to a shallow recursive depth. If needed, some indeterminism can be applied by shuffling the list <code>seq</code> in generate_legal_moves function.

Credits for loading animation in the UI: https://stackoverflow.com/a/66558182