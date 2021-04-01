"""
## Questions: EASY

### 567. [https://leetcode.com/problems/permutation-in-string/]

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one
of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Constraints:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

# Solutions


class Solution:
    """
    Time Complexity = O(n)
        finding length: n1 + n2
        forming dictionary: n1 + (n1 for s2_dict)
        Iteration: n2
            Comparing: min(n1, 26 when all alphabets are used)
        Total Time: 2n1 + 2n2 + min(n1, 26) * n2 = linear
    Space Complexity: O(n)
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        n1 = len(s1)
        n2 = len(s2)

        # Base Case
        if n1 > n2:
            return False

        s1_dict = Counter(s1)
        s2_dict = Counter(s2[0: n1 - 1])

        for it in range(n2 - n1 + 1):
            # Adding the next frame in the sliding window
            s2_dict[s2[it + n1 - 1]] = s2_dict.get(s2[it + n1 - 1], 0) + 1

            if s1_dict == s2_dict:
                return True

            # Removing the first frame
            if s2_dict.get(s2[it], 0) - 1 <= 0:
                del s2_dict[s2[it]]
            else:
                s2_dict[s2[it]] -= 1

        return False


# Runtime       : 68 ms, faster than 75.57% of Python3 online submissions
# Memory Usage  : 14.3 MB, less than 87.26% of Python3 online submissions


class Solution:
    """
    Time Complexity = O(n)
        finding length: n1 + n2
        forming dictionary: 26 + n1 + (n1 - 1 for s2_dict)
        Iteration: n2
            Comparing: 26
        Total Time: 2n1 + n2 + 26 + 26 * n2 = linear
    Space Complexity: O(n)
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        s1_dict, s2_dict = dict(), dict()
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        for char in alphabets:
            s1_dict[char] = 0
            s2_dict[char] = 0

        for char in s1:
            s1_dict[char] = s1_dict.get(char, 0) + 1

        for ind in range(n1 - 1):
            s2_dict[s2[ind]] = s2_dict.get(s2[ind], 0) + 1

        for it in range(n2 - n1 + 1):
            s2_dict[s2[it + n1 - 1]] = s2_dict.get(s2[it + n1 - 1], 0) + 1

            if s1_dict == s2_dict:
                return True

            s2_dict[s2[it]] = s2_dict.get(s2[it], 0) - 1

        return False


# Runtime       : 56 ms, faster than 95.45% of Python3 online submissions
# Memory Usage  : 14.2 MB, less than 96.57% of Python3 online submissions
