"""
[Golf](https://www.codechef.com/MAY21C/problems/LKDNGOLF)

It's a lockdown. You’re bored in your house and are playing golf in the hallway.

The hallway has N+2 tiles numbered from 0 to N+1 from left to right. There is a hole on tile number x. You hit the ball
standing on tile 0. When you hit the ball, it bounces at lengths of k, i.e. the tiles covered by it are 0,k,2k,…, and
so on until the ball passes tile N+1.

If the ball doesn't enter the hole in the first trial, you try again but this time standing on the tile N+1. When you
hit the ball, it bounces at lengths of k, i.e. the tiles covered by it are (N+1),(N+1−k),(N+1−2k),…, and so on until
the ball passes tile 0.

Find if the ball will enter the hole, either in its forward journey or backward journey.

Note: The input and output of this problem are large, so prefer using fast input/output methods.

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
The only line of each test case contains three integers N,x,k.

Output
Output in a single line, the answer, which should be "YES" if the ball enters the hole either in the forward or
backward journey and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and
"YES" will all be treated as identical).

Constraints
1≤T≤105
1≤x,k≤N≤109

Subtasks
Subtask #1 (10 points): N≤102
Subtask #2 (90 points): original constraints

Sample Input
3
5 4 2
5 3 2
5 5 2

Sample Output
YES
NO
NO

Explanation
In each test case, the tiles covered by the ball for N=5 and k=2 are {0,2,4,6} in the forward journey and {6,4,2,0} in
the backward journey.

Therefore, the answer for the first test case is "YES" since the ball falls in the position of the hole at tile 4. But
the answer for test cases 2 and 3 is "NO" since the ball does not fall in the position of the hole.
"""


import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = data[0]
    idx = 1
    while T > 0:
        N, x, k = data[idx:idx+3]
        N += 1

        if x % k == 0:
            print("YES")
        elif (N - x) % k == 0:
            print("YES")
        else:
            print("NO")

        T -= 1
        idx += 3

# Time : 0.14s
