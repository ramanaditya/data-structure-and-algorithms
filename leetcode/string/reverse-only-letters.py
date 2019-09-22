'''
## Questions

### 917. [Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/)

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"

Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Note:

- S.length <= 100
- 33 <= S[i].ASCIIcode <= 122 
- S doesn't contain \ or "

'''

## Solutions

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        i = 0
        j = len(S) - 1
        a = list(S)
        while i < j:
            if a[i].isalpha() and a[j].isalpha():
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
            elif a[i].isalpha() and not a[j].isalpha():
                j -= 1
            elif not a[i].isalpha() and a[j].isalpha():
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(a)

# Runtime: 36 ms
# Memory Usage: 13.9 MB
