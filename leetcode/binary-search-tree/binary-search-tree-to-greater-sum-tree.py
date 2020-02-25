"""
[1038. Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)

Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to
the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:
Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
"""

# Solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.gsum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        else:
            self.bstToGst(root.right)
            self.gsum += root.val
            root.val = self.gsum
            self.bstToGst(root.left)
        return root


# Runtime: 28 ms, faster than 74.36% of Python3 online submissions
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
