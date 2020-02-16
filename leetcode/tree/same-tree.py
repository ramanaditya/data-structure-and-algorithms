"""
[100. Same Tree](https://leetcode.com/problems/same-tree/)

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]
Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]
Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]
Output: false
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = True

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            if p.val != q.val:
                self.ans = False
            self.isSameTree(p.left, q.left)
            self.isSameTree(p.right, q.right)
        elif p and not q:
            self.ans = False
            return self.ans
        elif not p and q:
            self.ans = False
            return self.ans
        return self.ans


# Runtime: 28 ms, faster than 70.58% of Python3 online submissions
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
