"""
## Questions: EASY
### [278. First Bad Version](https://leetcode.com/problems/first-bad-version/)

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following
ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find
the first bad version. You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. .
"""

# Solutions


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def binary_search(self, low, high):
        while low <= high:
            mid = low + (high - low) // 2
            get_ele = isBadVersion(mid)

            if get_ele == True and (mid == 1 or isBadVersion(mid - 1) == False):
                return mid
            elif get_ele == False:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return -1
        else:
            return self.binary_search(1, n)


# Runtime       : 24 ms, faster than 90.24% of Python3 online submissions
# Memory Usage  : 13.9 MB, less than 6.90% of Python3 online submissions


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    """Using Binary Search General Template"""

    def binary_search(self, low, high):
        while low < high:
            mid = low + (high - low) // 2

            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return -1
        else:
            return self.binary_search(1, n)


# Runtime       : 28 ms, faster than 79.70% of Python3 online submissions
# Memory Usage  : 13.8 MB, less than 61.61% of Python3 online submissions
