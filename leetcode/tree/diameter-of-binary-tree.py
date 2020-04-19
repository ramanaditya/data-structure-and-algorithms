"""
# Question: Easy
## 543. [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the
length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Solutions

# Recursive Solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0  # edge case

        def check(root):
            if not root:
                return (0, 0)
            l1, d1 = check(root.left)
            l2, d2 = check(root.right)
            return 1 + max(l1, l2), max(d1, d2, l1 + l2)

        return check(root)[1]


# Runtime:  40 ms, faster than 89.13% of Python3 online submissions
# Memory Usage: 15.9 MB, less than 51.72% of Python3 online submissions
