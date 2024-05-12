## Coverage report:
Name|Stmts|Miss|Branch|BrPart|Cover|Missing
---|---|---|---|---|---|---
src/algo.py  |     106   |  1 |  80  |   2  | 98% | 37, 174->183
src/board.py |     70    | 12 |  63  |   5  | 84% | 28-3349-50, 52-53, 57-58, 59->64, 62->64
src/pentago.py|    77    | 54 |  26  |   1  | 23% |20-26, 29-30, 33-37, 40, 43-46, 57-60, 65-106
TOTAL           |     265   |  79 |  173   |   8  |  73%
--------------------------------------------------------------

I have thoroughly tested Algo.py, setting the recursive depth to 2 (3) to ensure the alpha-beta pruning effectively improves the algorithm's efficiency. At this depth, the loop in maximazingPlayer condition never breaks, as expected. However, with deeper depths, the break occurs. Tests cover all of the algorithm. 

Additionaly, the game has been tested manually comprehensively. With newest version of the heuristic evaluation the AI hasn't lost once. I used print statements during gameplay to ensure the algorithm's performance and verify that the AI consistently wins with the latest version of the heuristic evaluation. While algo.py unit tests the simulated scenarios aren't the most representative, manual testing provides a more comprehensive understanding of the algorithm's behavior across various game states. Representative unit testing for *all scenarios* would require thousands of tested board states.

Tests regarding board.py skip trivial UI tests. Board tests cover all the possible terminal states.

Unit tests concerning pentago.py aren't very important. Pentago.py handles basic UI operation for the game. It's tested manually, and it works great.

Tests can be repeated with:
<code>invoke test</code> or <code>pytest</code>