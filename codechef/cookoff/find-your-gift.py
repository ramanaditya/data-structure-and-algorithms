"""
[Find Your Gift](https://www.codechef.com/COOK116B/problems/GIFTSRC)

Problem Code: GIFTSRC

Today is Chef's birthday and he is looking forward to his gift. As usual, the gift is hidden and Chef has to follow a sequence of N instructions to reach it.

Initially, Chef is standing in the cell (0,0) of a two-dimensional grid. The sequence of instructions is given as a string S. If we denote Chef's current cell by (x,y), each character of S corresponds to an instruction as follows:

'L' means to go left, i.e. to the cell (x−1,y)
'R' means to go right, i.e. to the cell (x+1,y)
'U' means to go up, i.e. to the cell (x,y+1)
'D' means to go down, i.e. to the cell (x,y−1)
In addition, Chef should never perform multiple consecutive moves along the same axis of the grid. If there are multiple consecutive instructions to move along the same axis (left/right or up/down), he should perform only the first of these moves.

Find the cell (xg,yg) which contains the hidden gift.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains a single string S with length N.
Output
For each test case, print a single line containing two space-separated integers xg and yg.

Constraints
1≤T≤100
1≤N≤1,000
S contains only characters 'L', 'R', 'U' and 'D'
Example Input
3
5
LLLUR
7
LLLRUUD
8
LRULLUDU
Example Output
0 1
-1 1
-2 2
Explanation
Example case 1: Chef's path is (0,0)→(−1,0)→(−1,0)→(−1,0)→(−1,1)→(0,1).
"""

# Solution

# cook your dish here
import sys


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(str, input.split()))
    T = int(data[0])
    it = 1
    while T > 0:
        n = int(data[it])
        dir = data[it + 1]
        flag = dir[0]
        if flag == "L" or flag == "R":
            flag = "U"
        else:
            flag = "L"
        x = 0
        y = 0
        for i in dir:
            if flag == "U" or flag == "D":
                if i == "L":
                    x -= 1
                if i == "R":
                    x += 1
                flag = i
            if flag == "L" or flag == "R":
                if i == "U":
                    y += 1
                if i == "D":
                    y -= 1
                flag = i
            else:
                continue
        print(x, y)

        it += 2
        T -= 1

# Time : 0.04 s
# Memory: 17.7 M
