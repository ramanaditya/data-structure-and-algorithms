'''

## Questions

### 1189. [Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:

Input: text = "nlaebolko"
Output: 1

Example 2:

Input: text = "loonbalxballpoon"
Output: 2

Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
'''

## Solutions

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text = text.lower()
        char_count = lambda text, char: text.count(char)
        dict_num = dict( [ ( char, char_count(text, char) ) for char in text]  )
        print(dict_num)
        try:
            b_num = dict_num['b']
            a_num = dict_num['a']
            l_num = dict_num['l']//2
            o_num = dict_num['o']//2
            n_num = dict_num['n']
        except:
            return 0
        
        min_num = min(b_num,a_num,l_num,o_num,n_num)
        
        if min_num <= b_num and min_num <= a_num and min_num <= l_num and min_num <= o_num and min_num <= n_num:
            return min_num
        return 0

# Runtime: 628 ms
# Memory Usage: 14.4 MB
