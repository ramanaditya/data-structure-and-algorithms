"""
## Questions

### 65. [Valid Number](https://leetcode.com/problems/valid-number/)

A valid number can be split up into these components (in order):
    1. A decimal number or an integer.
    2. (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
    1. (Optional) A sign character (either '+' or '-').
    2. One of the following formats:
        1. At least one digit, followed by a dot '.'.
        2. At least one digit, followed by a dot '.', followed by at least one digit.
        3. A dot '.', followed by at least one digit.

An integer can be split up into these components (in order):
    1. (Optional) A sign character (either '+' or '-').
    2. At least one digit.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7",
"+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5",
"--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
"""


# Solutions


class Solution:
    """
    Solution is from: Heqing Norman Ya (aynamron),
    https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
    """
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        # DFA State Transition Table
        state = [
            {},
            {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
            {'digit': 3, '.': 4},
            {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
            {'digit': 5},
            {'digit': 5, 'e': 6, 'blank': 9},
            {'sign': 7, 'digit': 8},
            {'digit': 8},
            {'digit': 8, 'blank': 9},
            {'blank': 9}
        ]
        final_state = [3, 5, 8, 9]
        current_state = 1
        for char in s:
            if '0' <= char <= '9':
                char = 'digit'
            if char == ' ':
                char = 'blank'
            if char in ['+', '-']:
                char = 'sign'
            if char not in state[current_state]:
                return False
            current_state = state[current_state][char]

        if current_state not in final_state:
            return False

        return True


# Runtime       : 36 ms, faster than 58.20% of Python3 online submissions
# Memory Usage  : 14.2 MB, less than 61.27% of Python3 online submissions
