"""
Easy
[111. Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""

# Solutions

import math
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        nodes = [(root, 0)]
        depth = math.inf
        while nodes:
            node, level = nodes.pop()
            if not node.left and not node.right:
                depth = min(level, depth)
            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))

        return depth + 1


# Runtime: 732 ms, faster than 69.57% of Python3 online submissions
# Memory Usage: 48.6 MB, less than 97.72% of Python3 online submissions


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        if not root.left or not root.right:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# Runtime       : 766 ms, faster than 64.61% of Python3 online submissions
# Memory Usage  : 54.6 MB, less than 54.01% of Python3 online submissions
