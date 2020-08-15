"""
Medium
[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

# Solutions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    """
    Iterative Solution
    Time Complexity: O( n )
    Space Complexity: O( n )
    """

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return

        queue = deque([(root, 0)])
        res = []

        while queue:
            root, level = queue.popleft()
            if len(res) > level:
                res[level].append(root.val)
            else:
                res.append([root.val])

            if root.left:
                queue.append((root.left, level + 1))
            if root.right:
                queue.append((root.right, level + 1))

        return res


# Runtime: 28 ms, faster than 96.16% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 96.51% of Python3 online submissions
