"""
[104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.left = 0
        self.right = 0

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# Runtime: 40 ms, faster than 68.76% of Python3 online submissions
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions
