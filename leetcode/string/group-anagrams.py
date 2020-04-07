"""
## Questions : Medium

### 49. [Group Anagrams](https://leetcode.com/problems/group-anagrams/)

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""

## Solutions


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in anagrams:
                anagrams[sorted_str] = [str]
            else:
                anagrams[sorted_str].append(str)
        return anagrams.values()


# Runtime: 92 ms, faster than 95.79% of Python3 online submissions
# Memory Usage: 16.9 MB, less than 37.74% of Python3 online submissions
