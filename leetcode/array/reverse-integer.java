/*
## Questions :

### 7. [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**
Input: 123
Output: 321

Example 2:
<pre>
Input: -123
Output: -321
</pre>

Example 3:

Input: 120
Output: 21


Note:

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
*/

// Solutions
import java.util.Scanner;
class Solution {
    public int reverse(int x) {
        int flag = 0;
        long res = 0;
        if (x < Integer.MIN_VALUE || x > Integer.MAX_VALUE){
            return 0;
        }
        if (x < 0){
            flag = 1;
            x *= -1;
        }
        while(x>0){
            res = (res * 10 + x%10);
            x = x/10;
        }
        if(flag == 1){
            res *= -1;
            if (res > Integer.MIN_VALUE && res < Integer.MAX_VALUE){
                return (int)res;
            }
            return 0;
        }
        if (res > Integer.MIN_VALUE && res < Integer.MAX_VALUE){
            return (int)res;
        }
        return 0;
    }
}

class reverseInterger{
    public static void main(String[] args){
        Solution sol = new Solution();
        int x, res;
        System.out.println("Enter the value of x");
        Scanner sc = new Scanner(System.in);
        x = sc.nextInt();
        res = sol.reverse(x);
        System.out.println("Value of x : "+x);
        System.out.println("Reverse    : "+res);

    }
}

// Runtime: 1 ms, faster than 100.00% of Java online submissions
// Memory Usage: 36.7 MB, less than 5.55% of Java online submissions
