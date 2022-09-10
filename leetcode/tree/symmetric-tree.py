"""
[101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def is_symmetric(self, p, q):
        if not p and not q:
            return True

        if not p or not q:
            return False

        return (
                p.val == q.val
                and self.is_symmetric(p.left, q.right)
                and self.is_symmetric(p.right, q.left)
            )

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_symmetric(root.left, root.right)


# Runtime: 28 ms, faster than 89.63% of Python3 online submissions
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
