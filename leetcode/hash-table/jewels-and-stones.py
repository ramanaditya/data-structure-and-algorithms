"""
EASY
[771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each
character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a"
is considered a different type of stone from "A".

Example 1:
Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:
Input: J = "z", S = "ZZ"
Output: 0

Note:
S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""

## Solutions


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        letters = {}
        for i in S:
            letters[i] = letters.get(i, 0) + 1
        count = 0

        for char in J:
            if char in letters:
                count += letters[char]

        return count


# Runtime: 20 ms, faster than 97.79% of Python3 online submissions
# Memory Usage: 14 MB, less than 5.39% of Python3 online submissions
