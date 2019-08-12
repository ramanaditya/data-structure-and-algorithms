'''
## Question

### 4. [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''

## Solutions

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        k = len(nums1)
        l = len(nums2)
        new_array = []
        while i < k and j < l:
            if nums1[i] > nums2[j]:
                new_array.append(nums2[j])
                j = j+1
            else:
                new_array.append(nums1[i])
                i = i + 1
        while i < k:
            new_array.append(nums1[i])
            i = i + 1
        while j < l:
            new_array.append(nums2[j])
            j = j + 1
        i = len(new_array)
        if i%2 == 0:
            median = new_array[int(i/2)-1] + new_array[int(i/2)]
            return median/2.0
        else:
            return new_array[int(i/2)]/1.0

# Runtime: 60 ms
# Memory Usage: 13.3 MB
