"""
## Questions

### 125. [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Note :** For the purpose of this problem, we define empty string as valid palindrome.


**Example 1:**

```
Input: "A man, a plan, a canal: Panama"
Output: true
```

**Example 2:**

```
Input: "race a car"
Output: false
```
"""

# Solutions


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1
        while start < end:
            if s[start].isalnum() and s[end].isalnum() and s[start] != s[end]:
                return False
            elif s[start].isalnum() and not s[end].isalnum():
                end -= 1
            elif not s[start].isalnum() and s[end].isalnum():
                start += 1
            else:
                start += 1
                end -= 1
        return True


# Runtime: 52 ms, faster than 67.33% of Python3 online submissions
# Memory Usage: 14.3 MB, less than 68.45% of Python3 online submissions
