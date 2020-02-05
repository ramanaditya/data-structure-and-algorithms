"""
[292. Nim Game](https://leetcode.com/problems/nim-game/)
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you
take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn
to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win
the game given the number of stones in the heap.

Example:
Input: 4
Output: false
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be
             removed by your friend.

"""


class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 3:
            return True
        if n % 4 != 0:
            return True
        return False


# or


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


# Runtime: 24 ms, faster than 85.12% of Python3 online submissions
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions
