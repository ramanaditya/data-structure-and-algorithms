"""
Medium
[107. Binary Tree Level Order Traversal II](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/)
Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values.
(i.e., from left to right, level by level from leaf to root).

Example 1:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
"""

# Solutions

from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = deque()

        nodes = deque([(root, 0)])

        while nodes:
            node, level = nodes.popleft()
            if level < len(result):
                result[- (level + 1)].append(node.val)
            else:
                result.appendleft([node.val])
            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))

        return result


# Runtime: 45 ms, faster than 74.48% of Python3 online submissions
# Memory Usage: 14.2 MB, less than 83.57% of Python3 online submissions


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = deque()

        def dfs(node, level):
            if not node:
                return

            if level < len(result):
                result[-(level + 1)].append(node.val)
            else:
                result.appendleft([node.val])

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)

        return result


# Runtime       : 74 ms, faster than 10.56% of Python3 online submissions
# Memory Usage  : 15 MB, less than 7.86% of Python3 online submissions
