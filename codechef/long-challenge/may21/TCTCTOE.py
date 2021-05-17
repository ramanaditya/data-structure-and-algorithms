"""
[Tic Tac Toe](https://www.codechef.com/MAY21C/problems/TCTCTOE)

Tic-tac-toe is a game played between two players on a 3×3 grid. In a turn, a player chooses an empty cell and places
their symbol on the cell. The players take alternating turns, where the player with the first turn uses the symbol X
and the other player uses the symbol O. The game continues until there is a row, column, or diagonal containing three
of the same symbol (X or O), and the player with that token is declared the winner. Otherwise if every cell of the grid
contains a symbol and nobody won, then the game ends and it is considered a draw.

You are given a tic-tac-toe board A after a certain number of moves, consisting of symbols O, X, and underscore(_).
Underscore signifies an empty cell.

Print
1: if the position is reachable, and the game has drawn or one of the players won.
2: if the position is reachable, and the game will continue for at least one more move.
3: if the position is not reachable.

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
Each test case contains 3 lines of input where each line contains a string describing the state of the game in ith row.

Output
For each test case, output in a single line 1, 2 or 3 as described in the problem.

Constraints
1≤T≤39
Aij∈{X,O,_}

Subtasks
Subtask #1 (100 points): Original Constraints

Sample Input
3
XOX
XXO
O_O
XXX
OOO
___
XOX
OX_
XO_

Sample Output
2
3
1

Explanation
Test Case 1: The board is reachable, and although no player can win from this position, still the game continues.

Test Case 2: There can't be multiple winners in the game.

Test Case 3: The first player is clearly a winner with one of the diagonals.
"""

import sys


def winner(board, player):
    # All winning Conditions
    if (board[0] == board[1] == board[2] == player) or \
            (board[3] == board[4] == board[5] == player) or \
            (board[6] == board[7] == board[8] == player) or \
            (board[0] == board[3] == board[6] == player) or \
            (board[1] == board[4] == board[7] == player) or \
            (board[2] == board[5] == board[8] == player) or \
            (board[0] == board[4] == board[8] == player) or \
            (board[2] == board[4] == board[6] == player):
        return True
    return False


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(str, input.split()))
    T = int(data[0])
    idx = 1
    while T > 0:
        boards = "".join(data[idx:idx + 3])

        # Count
        cross = boards.count("X")
        zero = boards.count("O")
        underscore = boards.count("_")

        x_stat = winner(boards, "X")  # won or loss
        o_stat = winner(boards, "O")  # won or loss

        if (x_stat and o_stat) or (cross < zero or cross > zero + 1):
            print("3")
        elif (x_stat and not o_stat and cross > zero) or \
                (not x_stat and o_stat and cross == zero) or \
                (not x_stat and not o_stat and underscore == 0):
            print("1")
        elif underscore == 9 or (not x_stat and not o_stat and underscore >= 0):
            print("2")
        else:
            print("3")

        T -= 1
        idx += 3

# Time : 0.06s
