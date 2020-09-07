"""
EASY
290. [Word Pattern](https://leetcode.com/problems/word-pattern/)
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""


# Solutions


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern or not str:
            return False

        str_list = str.split(" ")
        if len(pattern) != len(str_list):
            return False

        if len(set(pattern)) != len(set(str_list)):
            return False

        track = dict()
        for ind, char in enumerate(pattern):
            track[char] = track.get(char, ind)

        for ind, word in enumerate(str_list):
            if word != str_list[track[pattern[ind]]]:
                return False
        return True


# Runtime       : 24 ms, faster than 94.56% of Python3 online submissions
# Memory Usage  : 14 MB, less than 7.79% of Python3 online submissions
