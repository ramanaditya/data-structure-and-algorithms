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
    """Bottom up Approach : Recursive"""

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# Runtime: 40 ms, faster than 68.76% of Python3 online submissions
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions


class Solution:
    """Top Down Approach : Recursive"""

    def __init__(self):
        self.count = 0

    def maxDepth(self, root: TreeNode) -> int:
        def helper(root, depth):
            if not root:
                return
            if not root.left and not root.right:
                self.count = max(self.count, depth)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 1)
        return self.count


# Runtime: 40 ms, faster than 67.72% of Python3 online submissions
# Memory Usage: 15 MB, less than 90.62% of Python3 online submissions


class Solution:
    """DFS : Iterative"""

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = 0
        while stack:
            root, depth = stack.pop()
            if root.left:
                stack.append((root.left, depth + 1))
            if root.right:
                stack.append((root.right, depth + 1))
            res = max(res, depth)
        return res


# Runtime: 36 ms, faster than 88.83% of Python3 online submissions
# Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions
