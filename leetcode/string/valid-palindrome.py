'''
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
'''

## Solutions

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i] == s[j] :
                    i += 1
                    j -= 1
                    continue
                else:
                    return False
            elif s[i].isalnum() and not s[j].isalnum() :
                j -= 1
            elif not s[i].isalnum() and s[j].isalnum():
                i += 1
            else:
                i += 1
                j -= 1
        return True

# Runtime: 56 ms
# Memory Usage: 14 MB
