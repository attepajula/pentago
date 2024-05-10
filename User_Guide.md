# Pentago User Guide and Rules

## Starting the game:

<code>$ Python3 src/index.py</code>

If case of you are using Poetry:
<code>$ poetry run invoke play</code>

## Rules:

Pentago is played on a 6x6 grid divided into four 3x3 quadrants.
User marks moves with symbol "O" and the opponent marks its moves with symbol "X".
After placing a symbol, the player must then rotate one of the four quadrants by 90 degrees in either direction (clockwise or counterclockwise).
The game continues with players alternately placing symbols and rotating quadrants until one player achieves the objective. 
A player wins by placing five of their own symbols in a row horizontally, vertically, or diagonally.
The quadrants are numbered as followed:
1 | 2 | 
---|---|
**3**|**4**|
