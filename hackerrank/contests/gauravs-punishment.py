"""
[Generate Primes](https://www.hackerrank.com/contests/mentorshipkarona-webinar-by-vinit-shahdeo/challenges/gauravs-punishment)

Vinit is really good at maths. Recently, he came to know about a problem on prime number. Amazed by the problem he got,
he asked Sharmishtha the same problem. Sharmishtha also being good at maths solved the problem within 5 minutes. Now,
its your time to solve the problem.

"You have to generate all prime numbers between two given numbers".

Input Format
The first line of the input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case consists of a single line containing two space separated integers m and n.

Constraints
1<=T<=60
1 <= m <= n <= 100000,
n - m <= 100000

Output Format
For every test case print all prime numbers p such that m <= p <= n, space separated. Separate the answers for each
test case by a new line.

Sample Input 0
2
1 10
3 5
Sample Output 0
2 3 5 7
3 5
"""


import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n > 2 and n & 1 == 0:
        return False
    root = math.floor(math.sqrt(n))
    for i in range(3, 1 + root, 2):
        if n % i == 0:
            return False
    return True


T = int(input())
while T:
    m, n = list(map(int, input().split()))
    for i in range(m, n + 1):
        if is_prime(i):
            print(i, end=" ")
    print()
    T -= 1
