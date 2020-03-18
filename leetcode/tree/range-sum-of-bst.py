"""
[938. Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst/)
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:
The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""


# Solutions

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Simple Recursive Solution
"""


class Solution:
    def __init__(self):
        self.total = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return
        if root:
            if R >= root.val >= L:
                self.total += root.val
            self.rangeSumBST(root.left, L, R)
            self.rangeSumBST(root.right, L, R)
            return self.total


# Runtime: 284 ms, faster than 34.52% of Python3 online submissions
# Memory Usage: 21 MB, less than 100.00% of Python3 online submissions

"""
Bounded Recursive Solution
"""


class Solution:
    def __init__(self):
        self.total = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0
        if root:
            if R >= root.val >= L:
                self.total += root.val
            if root.val > L:
                self.rangeSumBST(root.left, L, R)
            if root.val < R:
                self.rangeSumBST(root.right, L, R)
            return self.total


# Runtime: 224 ms, faster than 75.81% of Python3 online submissions
# Memory Usage: 21 MB, less than 100.00% of Python3 online submissions
