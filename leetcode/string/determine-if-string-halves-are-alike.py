"""
## Questions : EASY
### 1704. [Determine if String Halves Are Alike](https://leetcode.com/problems/determine-if-string-halves-are-alike/)

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first
half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice
that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

Example 3:
Input: s = "MerryChristmas"
Output: false

Example 4:
Input: s = "AbCdEfGh"
Output: true

Constraints:
2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
"""

# Solutions


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        n = len(s)
        first_half, second_half = 0, 0
        for i in range(n // 2):
            if s[i] in vowels:
                first_half += 1
        for j in range(n // 2, n):
            if s[j] in vowels:
                second_half += 1

        return first_half == second_half


# Runtime: 28 ms, faster than 93.34% of Python3 online submissions
# Memory Usage: 14.3 MB, less than 37.27% of Python3 online submissions
