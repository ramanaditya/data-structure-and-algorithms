"""
Medium
## Questions
### [528. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which
randomly picks an index in proportion to its weight.

Note:
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

Example 1:
Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

Example 2:
Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]

Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument,
the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""


# Solutions


class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sum = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        if not self.prefix_sum:
            return 0
        rand = random.randint(0, self.prefix_sum[-1] - 1)
        return bisect.bisect_right(self.prefix_sum, rand)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


# Runtime: 232 ms, faster than 91.15% of Python3 online submissions
# Memory Usage: 18.2 MB, less than 81.65% of Python3 online submissions
