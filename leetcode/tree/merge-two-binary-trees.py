"""
[617. Merge Two Binary Trees](https://leetcode.com/problems/merge-two-binary-trees/)
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are
overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as
the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:

Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.
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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode):
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        elif t1:
            return t1
        elif t2:
            return t2
        else:
            return


# Runtime: 96 ms, faster than 34.60% of Python3 online submissions
# Memory Usage: 14.1 MB, less than 20.00%  of Python3 online submissions
