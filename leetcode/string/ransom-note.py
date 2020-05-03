"""
EASY
[383. Ransom Note](https://leetcode.com/problems/ransom-note/)
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function
that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

# Solution


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = dict()

        for i in magazine:
            letters[i] = letters.get(i, 0) + 1

        for letter in ransomNote:
            if letter in letters:
                if letters[letter] <= 0:
                    return False
                letters[letter] -= 1
            else:
                return False

        return True


# Runtime: 84 ms, faster than 19.52% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 25.00% of Python3 online submissions
