"""
Question : Medium
[338. Counting Bits](https://leetcode.com/problems/counting-bits/)
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in
their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]

Follow up:
- It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n)
/possibly in a single pass?
- Space complexity should be O(n).
- Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""


class Solution:
    def countBits(self, num: int) -> List[int]:
        a = []
        for i in range(num + 1):
            a.append(bin(i)[2:].count("1"))
        return a


# Runtime: 100 ms, faster than 29.50% of Python3 online submissions
# Memory Usage: 20.8 MB, less than 5.00% of Python3 online submissions


class Solution:
    def countBits(self, num: int) -> List[int]:
        a = [0]
        for i in range(1, num + 1):
            if i & 1:
                a.append(a[i >> 1] + 1)
            else:
                a.append(a[i >> 1])
        return a


# Runtime: 80 ms, faster than 83.42% of Python3 online submissions
# Memory Usage: 20.5 MB, less than 5.00% of Python3 online submissions


class Solution:
    """Condensed form of the above solution"""

    def countBits(self, num: int) -> List[int]:
        res = [0]
        for i in range(1, num + 1):
            res.append(res[i >> 1] + 1 if i & 1 else res[i >> 1])
        return res


# Runtime: 80 ms, faster than 83.42% of Python3 online submissions
# Memory Usage: 20.5 MB, less than 5.00% of Python3 online submissions
