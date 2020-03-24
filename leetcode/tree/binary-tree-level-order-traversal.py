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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return
        q = [(root, 0)]
        res = []
        while q:
            root, level = q.pop(0)
            if len(res) <= level:
                res.append([root.val])
            else:
                res[level].append(root.val)
            if root.left:
                q.append((root.left, level + 1))
            if root.right:
                q.append((root.right, level + 1))
        return res


# Runtime: 32 ms, faster than 73.53% of Python3 online submissions
# Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions
