"""
[Xor Equality](https://www.codechef.com/MAY21C/problems/XOREQUAL)

For a given N, find the number of ways to choose an integer x from the range [0,2N−1] such that x⊕(x+1)=(x+2)⊕(x+3),
where ⊕ denotes the bitwise XOR operator.

Since the number of valid x can be large, output it modulo 109+7.

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
The only line of each test case contains a single integer N.

Output
For each test case, output in a single line the answer to the problem modulo 109+7.

Constraints
1≤T≤105
1≤N≤105

Subtasks
Subtask #1 (100 points): Original Constraints

Sample Input
2
1
2

Sample Output
1
2

Explanation
Test Case 1: The possible values of x are {0}.
Test Case 2: The possible values of x are {0,2}.
"""


import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = data[0]
    idx = 1
    while T > 0:
        N = data[idx] - 1
        mod = 1000000007

        x, res = 2, 1
        while N > 0:
            if N & 1:
                res = (res * x) % mod
            x = (x * x) % mod
            N = N >> 1
        print(res)

        T -= 1
        idx += 1

# Time : 0.58s
