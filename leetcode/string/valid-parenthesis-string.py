"""
## Questions : EASY
### 678. [Valid Parenthesis String](https://leetcode.com/problems/valid-parenthesis-string/)

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this
string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].
"""

## Solutions


class Solution:
    def checkValidString(self, s: str) -> bool:
        le = len(s)
        L = R = S = 0
        LL = RR = SS = 0
        for i in range(0, le):
            if s[i] == "(":
                L += 1
            if s[i] == ")":
                R += 1
            if s[i] == "*":
                S += 1

            if s[le - 1 - i] == "(":
                LL += 1
            if s[le - 1 - i] == ")":
                RR += 1
            if s[le - 1 - i] == "*":
                SS += 1

            if R > L + S:
                return False
            if LL > RR + SS:
                return False

        return True


# Runtime: 28 ms, faster than 72.38% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 14.29% of Python3 online submissions
