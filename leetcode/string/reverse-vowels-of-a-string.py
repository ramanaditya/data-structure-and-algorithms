"""
## Questions

### 345. [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
"""

## Solutions


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        i = 0
        j = len(s) - 1
        s = list(s)
        while i < j:
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)


# Runtime: 68 ms, faster than 33.51% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions
