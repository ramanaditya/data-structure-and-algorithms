'''
## Questions

### [Processing a string](https://www.codechef.com/problems/KOL15A)

All submissions for this problem are available.
Given an alphanumeric string made up of digits and lower case Latin characters only, find the sum of all the digit characters in the string.

Input

The first line of the input contains an integer T denoting the number of test cases. Then T test cases follow.
Each test case is described with a single line containing a string S, the alphanumeric string.

Output

For each test case, output a single line containing the sum of all the digit characters in that string.

Constraints
    1 ≤ T ≤ 1000
    1 ≤ |S| ≤ 1000, where |S| is the length of the string S.

Example 

Input
    1
    ab1231da

Output:
    7

Explanation

The digits in this string are 1, 2, 3 and 1. Hence, the sum of all of them is 7.
'''

## Solution

# cook your dish here
import sys
if __name__ == '__main__':
    T = int(input())
    while T:
        a = str(input())
        res = 0
        for i in a:
            try:
                res += int(i)
            except:
                continue
        print(res)
        T -= 1

# Time : 0.38 s