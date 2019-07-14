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
            median = float(new_array[int(i/2)-1] + new_array[int(i/2)])
            return median/2
        else:
            return float(new_array[int(i/2)])

# Runtime: 76 ms
# Memory Usage: 13.5 MB
