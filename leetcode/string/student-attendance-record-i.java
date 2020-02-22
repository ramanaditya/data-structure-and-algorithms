/*
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
*/

// Solutions


class Solution {
    public boolean checkRecord(String s) {
        int A = 0, L = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i) == 'A'){
                A += 1;
            }
            if(A>1){
                return false;
            }
            if(s.charAt(i) == 'L'){
                try{
                    if(s.charAt(i+1) == 'L' && s.charAt(i+2) == 'L'){
                        L += 1;
                    }
                }
                catch (Exception e){
                    if(L > 0){
                        return false;
                    }
                }
            }
            if(L > 0){
                return false;
            }
        }
        return true;
    }
}


// Runtime: 20 ms, faster than 100.00% of Java online submissions
// Memory Usage: 37.6 MB, less than 5.26% of Java online submissions
