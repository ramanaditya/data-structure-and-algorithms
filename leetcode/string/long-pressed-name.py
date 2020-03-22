"""
## Questions

### 925. [Long Pressed Name](https://leetcode.com/problems/long-pressed-name/)

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed,
and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with
some characters (possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:
Input: name = "leelee", typed = "lleeelee"
Output: true

Example 4:
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.


Note:
name.length <= 1000
typed.length <= 1000
The characters of name and typed are lowercase letters.
"""

## Solutions


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        stack1 = []
        stack2 = []
        for i in name:
            stack1.append(i)
        for j in typed:
            stack2.append(j)
        if len(stack1) > len(stack2):
            return False
        while stack1 and stack2:
            if stack1[-1] != stack2[-1]:
                return False
            pop1 = stack1[-1]
            count1 = 0
            count2 = 0
            while stack1[-1] == pop1:
                count1 += 1
                stack1.pop()
                if not stack1:
                    break
            while stack2[-1] == pop1:
                count2 += 1
                stack2.pop()
                if not stack2:
                    break
            if count1 > count2:
                return False
        if stack1 or stack2:
            return False
        return True


# Runtime: 24 ms, faster than 94.05% of Python3 online submissions
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        m = len(name)
        n = len(typed)
        while i < m and j < n:
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if typed[j] != typed[j - 1]:
                    return False
                else:
                    j += 1
        return i == m


# Runtime: 28 ms, faster than 78.00% of Python3 online submissions
# Memory Usage: 13 MB, less than 100.00% of Python3 online submissions
