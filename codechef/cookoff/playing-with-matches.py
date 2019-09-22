'''
[Playing with Matches](https://www.codechef.com/COOK110B/problems/MATCHES)

Problem Code: MATCHES

Chef's son Chefu found some matches in the kitchen and he immediately starting playing with them.

The first thing Chefu wanted to do was to calculate the result of his homework — the sum of A and B, and write it using matches. Help Chefu and tell him the number of matches needed to write the result.

Digits are formed using matches in the following way: 

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two space-separated integers A and B.
Output
For each test case, print a single line containing one integer — the number of matches needed to write the result (A+B).

Constraints
1≤T≤1,000
1≤A,B≤10^6

Example Input
3
123 234
10101 1010
4 4

Example Output
13
10
7

Explanation
Example case 1: The result is 357. We need 5 matches to write the digit 3, 5 matches to write the digit 5 and 3 matches to write the digit 7.

Example case 2: The result is 11111. We need 2 matches to write each digit 1, which is 2⋅5=10 matches in total.

'''

# Solution

# cook your dish here
import sys
import math
def check(a):
    if a == '0':
        return 6
    elif a == '1':
        return 2
    elif a == '2':
        return 5
    elif a == '3':
        return 5
    elif a == '4':
        return 4
    elif a == '5':
        return 5
    elif a == '6':
        return 6
    elif a == '7':
        return 3
    elif a == '8':
        return 7
    elif a == '9':
        return 6

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        A, B = map(int, input().split())
        sum_ = A + B
        total = 0
        str_sum = str(sum_)
        for i in str_sum:
            total = total + check(i)
        print(total)
        T -= 1

# Time : 0.02 s
# Memory: 17.6 M
