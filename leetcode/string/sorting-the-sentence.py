"""
## Questions : EASY
### 1859. [Sorting the Sentence](https://leetcode.com/problems/sorting-the-sentence/)

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word
consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the
sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

Example 1:
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

Example 2:
Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.

Constraints:
2 <= s.length <= 200
s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
The number of words in s is between 1 and 9.
The words in s are separated by a single space.
s contains no leading or trailing spaces.
"""


# Solutions


class Solution:
    """
    Time Complexity
        len(s) ie., O(n) for splitting the sentence
        9 (at max) ie., constant for counting words, iterating over list, iterate for joining the words
        Time Complexity: O(n), n = len(s)
    Space Complexity: O(n), n = len(s)
    """
    def sortSentence(self, s: str) -> str:
        word_list = s.split()  # form a list of words
        n = len(word_list)  # total words in the list, at max 9

        # dict to make k, v pairs as there are at max 9 words in the array
        # key as position of word, value as word without position
        # because while joining, fetching from dict will take constant time
        # and we can just add values iterating over keys from 1 to 9 (including)
        index_dict = dict()
        for word in word_list:
            index_dict[int(word[-1])] = word[:-1]

        res = ""
        # iterate from 1 to n, and add up all the values
        for i in range(1, n+1):
            res += index_dict.get(i, "")
            res += " "

        # we can alse use, res[:-1], res.strip()
        return res.rstrip()  # right strip as " " is present at the end of the sentence


# Runtime       : 24 ms, faster than 100.00% of Python3 online submissions
# Memory Usage  : 14.2 MB, less than 50.00% of Python3 online submissions


class Solution:
    def sortSentence(self, s: str) -> str:
        # split the string and sort the words based upon the last letter
        word_list = sorted(s.split(), key=lambda word: word[-1], reverse=False)
        return " ".join([word[:-1] for word in word_list])  # join the words, after removing the last letter ie., digit

# Runtime       : 24 ms, faster than 100.00% of Python3 online submissions
# Memory Usage  : 14.2 MB, less than 50.00% of Python3 online submissions
