'''
## Questions
### 66. [Plus One](https://leetcode.com/problems/plus-one/)
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''
## Solutions

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits) - 1
        carry = 1
        value = 0
        while j >= 0:
            value = digits[j] + carry
            if value <= 9:
                digits[j] = value
                carry = 0
                break
            else:
                digits[j] = value % 10
                carry = value // 10
                j -= 1
        if carry > 0:
            digits.insert(0,carry)
        return digits

# Runtime: 24 ms, faster than 99.93% of Python3 online submissions 
# Memory Usage: 13.7 MB,
