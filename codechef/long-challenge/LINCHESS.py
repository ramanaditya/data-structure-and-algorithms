"""
[Chef and Linear Chess](https://www.codechef.com/AUG20B/problems/LINCHESS)
Chef wants to play a game of linear chess on a one-dimensional board ― an infinite row of squares numbered by positive
integers. In this game, he has a pawn, which is initially at a square K. There are also N other people (numbered 1
through N); Chef can choose one of them to play against. For each valid i, the i-th player would play in the following
 way:

Take a pawn and place it on a square Pi.
Repeat the following move any number of times: move the pawn from its current square Pi squares forward, i.e. from a
square s, this player's pawn is moved to the square s+Pi.
If this player moves their pawn to the square with Chef's pawn, then Chef's pawn is captured and he loses the game.
Unfortunately, Chef cannot move his pawn during the game, making him an easy target for other players. Given the
starting positions of all N+1 players, find a player who can capture Chef's pawn in the smallest number of moves or
determine that no player can capture his pawn.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains N space-separated integers P1,P2,…,PN.

Output
For each test case, print a single line containing one integer ― the starting square of one player that can beat Chef in the smallest number of turns, or −1 if no player can beat him.

If there are multiple solutions, you may find any one.

Constraints
1≤T≤100
1≤N≤1,000
1≤K≤109
1≤Pi≤109 for each valid i
K,P1,P2,…,PN are pairwise distinct

Subtasks
Subtask #1 (100 points): original constraints

Example Input
2
4 6
4 3 2 8
4 7
4 3 2 8

Example Output
3
-1

Explanation
Example case 1: The player who starts at the position 2 can move to square 4 and then to square 6. The player who
starts at the position 3 can move to square 6. The player at position 2 can capture Chef's pawn in 2 turns, whereas
the player at position 3 can capture Chef's pawn in 1 turn. Therefore, the answer is 3.

Example case 2: No player can capture Chef's pawn.
"""
if __name__ == "__main__":
    T = int(input())
    while T:
        N, K = list(map(int, input().split()))
        P = list(map(int, input().split()))
        res = [float("inf"), -1]
        start = 0
        while start < N:
            if P[start] < K and K % P[start] == 0:
                if K // P[start] < res[0]:
                    res = [K // P[start], P[start]]
            start += 1
        print(res[1])
        T -= 1

# Time : 0.4s
