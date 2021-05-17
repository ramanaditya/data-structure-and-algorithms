"""
[Modular Equation](https://www.codechef.com/MAY21C/problems/MODEQ)

Given integers N and M, find the number of ordered pairs (a,b)
such that 1≤a<b≤N and ((M mod a) mod b)=((M mod b) mod a).

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
The only line of each test case contains two integers N, M.

Output
For each testcase, output in a single line the answer to the problem.

Constraints
1≤T≤1000
2≤N≤106
1≤M≤5⋅105
The sum of N over all test cases does not exceed 106.
Note: Multiplier for JAVA for this problem is reduced to 1.25 instead of usual 2.

Subtasks
Subtask #1 (10 points):
1≤T≤10
2≤N≤103
1≤M≤105

Subtask #2 (40 points):
1≤T≤100
2≤N≤105
1≤M≤105
The sum of N over all test cases does not exceed 106.
Subtask #3 (50 points): Original Constraints

Sample Input
3
3 5
3 6
3 10

Sample Output
2
3
2

Explanation
Test Case 1: The valid pairs are {(1,2),(1,3)}.

Test Case 2: The valid pairs are {(1,2),(1,3),(2,3)}.

Test Case 3: The valid pairs are {(1,2),(1,3)}.
"""

import sys

# Brute Force
"""
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = data[0]
    idx = 1
    while T > 0:
        N, M = data[idx: idx + 2]

        res = 0
        for i in range(1, N):
            for j in range(i + 1, N + 1):
                if (M % i) % j == (M % j) % i:
                    res += 1

        print(res)

        T -= 1
        idx += 2

# Time : 0.58s
"""

if __name__ == '__main__':
    T = int(input())
    idx = 1
    while T > 0:
        N, M = list(map(int, input().split()))

        res = 0
        mod = dict()
        for a in range(2, N+1):
            mod_with_a = M % a
            res += mod.get(mod_with_a, 1)
            for b in range(mod_with_a, N+1, a):
                mod[b] = mod.get(b, 1) + 1

        print(res)

        T -= 1

# Time : 4.92s
