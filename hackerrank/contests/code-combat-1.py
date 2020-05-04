"""
[Most Occuring Digit](https://www.hackerrank.com/contests/mentorshipkarona-webinar-by-vinit-shahdeo/challenges/code-combat-1)

Vinit & Vaibhaw are siblings. These days, they're at home due to the lockdown. One day Vinit's brother Vaibhaw got
angry with him for waking him in the morning, so he gave a tough task to Vinit to take the revenge.

The task is "Given a number, find the most occurring digit in it. If two or more digits occur same number of times,
then return the highest of them. Input integer is given as a string".

Vinit needs your help to complete this task as it is difficult for him to solve alone.

Input Format
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first
line of each test case contains the number N

Constraints
1<= T <=100
1<= N <=101000

Output Format
Print the most occurring digit in the number. If two or more digits occur same number of times, then print the highest
of them. Print the answer for each test case in a new line.

Sample Input 0
1
12234
Sample Output 0
2

Explanation 0
2 occurs maximum number of times in 12234
"""

T = int(input())
while T:
    N = int(input())
    d = dict()
    while N > 0:
        dig = N % 10
        d[dig] = d.get(dig, 0) + 1
        N = N // 10
    res = float("-inf")
    max_val = max(d.values())
    for k in d.keys():
        if d[k] == max_val and res < k:
            res = k
    print(res)

    T -= 1
