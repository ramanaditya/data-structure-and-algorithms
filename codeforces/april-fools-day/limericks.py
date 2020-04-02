"""
[Limericks](https://codeforces.com/contest/1331/problem/B)
There was once young lass called Mary,
Whose jokes were occasionally scary.
On this April's Fool
Fixed limerick rules
Allowed her to trip the unwary.

Can she fill all the lines
To work at all times?
On juggling the words
Right around two-thirds
She nearly ran out of rhymes.

Input
The input contains a single integer 𝑎 (4≤𝑎≤998). Not every integer in the range is a valid input for the problem;
you are guaranteed that the input will be a valid integer.

Output
Output a single number.

Examples
input
35
output
57

input
57
output
319

input
391
output
1723
"""
import math

MAXN = 100001
spf = [0 for i in range(MAXN)]


def sieve():
    spf[1] = 1
    for i in range(2, MAXN):
        spf[i] = i
    for i in range(4, MAXN, 2):
        spf[i] = 2

    for i in range(3, math.ceil(math.sqrt(MAXN))):
        if spf[i] == i:
            for j in range(i * i, MAXN, i):
                if spf[j] == j:
                    spf[j] = i


def getFactorization(x):
    ret = list()
    while x != 1:
        ret.append(spf[x])
        x = x // spf[x]

    return ret


sieve()
x = int(input())
p = getFactorization(x)
for i in sorted(p):
    print(i, end="")
print()
