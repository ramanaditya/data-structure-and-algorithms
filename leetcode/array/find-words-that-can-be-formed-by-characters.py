'''
## Questions
# 1160. [Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/)
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
'''

# Solutions

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = {}
        for i in chars:
            chars_dict[i] = chars_dict.get(i,0)+1
        b = []
        for i in words:
            words_dict = {}
            for j in i:
                words_dict[j] = words_dict.get(j,0)+1
            b.append(words_dict)
        count = 0
        for i in range(len(b)):
            flag = 0
            for k,v in b[i].items():
                if not k in chars_dict or chars_dict[k] < v:
                    flag = 1
            if flag == 0:
                count += len(words[i])
            
        return count     

# Runtime: 316 ms
# Memory Usage: 14.7 MB
