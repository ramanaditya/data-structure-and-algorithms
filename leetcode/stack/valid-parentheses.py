"""
## Questions

### 20. [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""

# Solutions


class Solution:
    def isValid(self, s: str) -> bool:
        d = {"#": 0, "(": -1, ")": 1, "[": -2, "]": 2, "{": -3, "}": 3}
        stack = [0]
        start, end = 0, len(s)
        while start < end:
            if stack[-1] == -d[s[start]]:
                stack.pop()
            else:
                stack.append(d[s[start]])
            start += 1

        if stack[-1] == 0:
            return True

        return False


# Runtime: 24 ms, faster than 95.20% of Python3 online submissions
# Memory Usage: 14 MB, less than 24.76% of Python3 online submissions
