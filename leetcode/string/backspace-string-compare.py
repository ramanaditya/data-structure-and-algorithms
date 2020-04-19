"""
## Questions : EASY
### 844. [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace
character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

Follow up:
Can you solve it in O(N) time and O(1) space?
"""

## Solutions


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        str_S = ""
        str_T = ""
        count_back = 0
        i = len(S) - 1
        while i >= 0:
            if count_back == 0 and S[i] != "#":
                str_S += S[i]
            elif S[i] == "#":
                count_back += 1
            elif S[i] != "#" and count_back > 0:
                count_back -= 1
            i -= 1
        count_back = 0
        i = len(T) - 1
        while i >= 0:
            if count_back == 0 and T[i] != "#":
                str_T += T[i]
            elif T[i] == "#":
                count_back += 1
            elif T[i] != "#" and count_back > 0:
                count_back -= 1
            i -= 1
        return str_S == str_T


# Runtime: 32 ms, faster than 41.02% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 8.00% of Python3 online submissions
