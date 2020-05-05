"""
EASY
[387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""

## Solutions


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = dict()

        for i in range(len(s)):
            if s[i] in chars.keys():
                chars[s[i]] = None
                pass
            chars[s[i]] = chars.get(s[i], i)

        for k, v in chars.items():
            if v is not None:
                return v

        return -1


# Runtime: 240 ms, faster than 13.02% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 6.52% of Python3 online submissions


# Solution using Counter


from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = Counter(s)

        for index, char in enumerate(s):
            if chars[char] == 1:
                return index

        return -1


# Runtime: 88 ms, faster than 89.55% of Python3 online submissions
# Memory Usage: 14 MB, less than 6.52% of Python3 online submissions
