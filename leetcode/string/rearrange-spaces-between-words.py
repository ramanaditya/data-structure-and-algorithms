"""
## Questions : EASY
### 1592. [Rearrange Spaces Between Words](https://leetcode.com/problems/rearrange-spaces-between-words/)

You are given a string text of words that are placed among some number of spaces. Each word consists of one or more
lowercase English letters and are separated by at least one space. It's guaranteed that text contains at least one word.

Rearrange the spaces so that there is an equal number of spaces between every pair of adjacent words and that number is
maximized. If you cannot redistribute all the spaces equally, place the extra spaces at the end, meaning the returned
string should be the same length as text.

Return the string after rearranging the spaces.

Example 1:
Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.

Example 2:
Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.

Example 3:
Input: text = "hello   world"
Output: "hello   world"

Example 4:
Input: text = "  walks  udp package   into  bar a"
Output: "walks  udp  package  into  bar  a "

Example 5:
Input: text = "a"
Output: "a"

Constraints:
1 <= text.length <= 100
text consists of lowercase English letters and ' '.
text contains at least one word.
"""

# Solutions


class Solution:
    def reorderSpaces(self, text: str) -> str:
        if not text:
            return ""
        text_list = []
        spaces = 0
        temp = ""
        for char in text:
            if char == " ":
                spaces += 1
                if temp:
                    text_list.append(temp)
                    temp = ""
            else:
                temp += char
        if temp:
            text_list.append(temp)

        if len(text_list) == 0:
            return " " * spaces

        distribute = (spaces // (len(text_list) - 1)) if len(text_list) != 1 else 0
        last = (spaces % (len(text_list) - 1)) if len(text_list) != 1 else spaces

        res = []
        for word in text_list:
            if word:
                res.append(word)

        ret = (" " * distribute).join(res)
        ret += " " * last if last else ""
        if ret.count(" ") != spaces:
            ret += " " * distribute

        return ret


# Runtime: 28 ms, faster than 60.00% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 40.00% of Python3 online submissions
