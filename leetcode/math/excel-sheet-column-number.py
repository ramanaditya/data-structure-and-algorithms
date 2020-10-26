"""
## Questions: EASY

### 171. [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701

Constraints:
1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""

# Solutions


class Solution:
    """
    Time Complexity: O( n )
    Space Complexity: O( 1 )
    """

    def titleToNumber(self, s: str) -> int:
        char = {
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,
            "K": 11,
            "L": 12,
            "M": 13,
            "N": 14,
            "O": 15,
            "P": 16,
            "Q": 17,
            "R": 18,
            "S": 19,
            "T": 20,
            "U": 21,
            "V": 22,
            "W": 23,
            "X": 24,
            "Y": 25,
            "Z": 26,
        }

        length = len(s)
        start = 0
        res = 0

        while start < length:
            res += char[s[-1 - start]] * 26 ** start
            start += 1

        return res


# Runtime: 28 ms, faster than 92.18% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 66.41% of Python3 online submissions
