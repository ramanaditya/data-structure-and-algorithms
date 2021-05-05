"""
## Questions

### 970. [Powerful Integers](https://leetcode.com/problems/powerful-integers/)

Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal
to bound.

An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.

Example 1:
Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 20 + 30
3 = 21 + 30
4 = 20 + 31
5 = 21 + 31
7 = 22 + 31
9 = 23 + 30
10 = 20 + 32

Example 2:
Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]

Constraints:
1 <= x, y <= 100
0 <= bound <= 106
"""


# Solutions
from math import log
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if bound < 2:
            return []

        x_, y_ = [1], [1]

        if x != 1:
            i = 1
            while x_[-1] <= bound:
                x_.append(x ** i)
                i += 1

        if y != 1:
            i = 1
            while y_[-1] <= bound:
                y_.append(y ** i)
                i += 1

        res = set()
        for x_bar in x_:
            for y_bar in y_:
                sum_ = x_bar + y_bar
                if sum_ <= bound:
                    res.add(sum_)
                else:
                    break

        return list(res)


# Runtime       : 24 ms, faster than 95.96% of Python3 online submissions
# Memory Usage  : 14 MB, less than 99.80% of Python3 online submissions


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        a = bound if x == 1 else int(log(bound, x))
        b = bound if y == 1 else int(log(bound, y))

        res = set()
        for i in range(a + 1):
            for j in range(b + 1):
                val = x ** i + y ** j
                if val <= bound:
                    res.add(val)

                if y == 1:
                    break

            if x == 1:
                break

        return list(res)


# Runtime       : 32 ms, faster than 60.65% of Python3 online submissions
# Memory Usage  : 14.1 MB, less than 95.89% of Python3 online submissions
