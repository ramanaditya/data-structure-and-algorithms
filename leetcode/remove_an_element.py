class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        x = len(nums)
        if x == 1:
            if nums[0] == val:
                nums.remove(val)
                return len(nums)
        while i < x :
            if nums[i] == val:
                nums.remove(nums[i])
                x = len(nums)
                if x == 1:
                    if nums[0] == val:
                        nums.remove(val)
                        return len(nums)
                i = 0
            else:
                i = i + 1
        return len(nums)

# Runtime: 28 ms
# Memory Usage: 13.1 MB
