"""
## Questions : EASY
### 520. [Detect Capital](https://leetcode.com/problems/detect-capital/)

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True

Example 2:
Input: "FlaG"
Output: False

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


# Solutions


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.capitalize() == word or word.upper() == word or word.lower() == word:
            return True
        return False


# Runtime: 44 ms, faster than 28.24% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 71.43% of Python3 online submissions
