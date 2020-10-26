"""
## Questions: EASY

### 409. [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can
be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

# Solutions


from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Time Complexity: O( n )
        Space Complexity: O( 1 )
        """
        freq = Counter(s)
        odd = 0
        count = 0

        for val in freq.values():
            if val & 1 == 0:
                count += val
            else:
                count += val - 1
                odd = 1

        return count + odd


# Runtime: 32 ms, faster than 76.65% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 90.77% of Python3 online submissions
