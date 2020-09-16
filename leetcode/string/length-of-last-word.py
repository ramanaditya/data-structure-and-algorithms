"""
## Questions : EASY
### 58. [Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word
(last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
Input: "Hello World"
Output: 5
"""

# Solutions


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        word_len = 0
        flag = False

        while i >= 0:
            if flag and s[i] == " ":
                break
            elif s[i] != " ":
                word_len += 1
                flag = True
            i -= 1

        return word_len


# Runtime: 28 ms, faster than 78.09% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 88.14% of Python3 online submissions
