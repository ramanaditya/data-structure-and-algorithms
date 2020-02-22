"""
## Questions

### 551. [Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i/)

You are given a string representing an attendance record for a student. The record only contains the following
 three characters:

'A' : Absent.
'L' : Late.
'P' : Present.

A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two
 continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False
"""

## Solutions


class Solution:
    def checkRecord(self, s: str) -> bool:
        A = 0
        L = -1
        if s == "":
            return True
        try:
            A = s.count("A")
        except:
            pass
        if A > 1:
            return False
        try:
            L = s.find("LLL")
        except:
            pass
        if L != -1:
            return False
        return True


# Runtime: 28 ms, faster than 64.72% of Python3 online submissions
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
