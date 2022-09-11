"""
[1302. Deepest Leaves Sum](https://leetcode.com/problems/deepest-leaves-sum/)
Given a binary tree, return the sum of values of its deepest leaves.

Example 1:

       1
      / \
     2   3
    / \   \
   4  5    6
  /         \
 7           8

Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15

Constraints:
The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""


# Solutions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        Here we are using a BFS approach to traverse the tree.
        We are using a queue to store the nodes and their level.
        Store the sum at each level and also level.
        At the end, return the sum of the deepest level.
        """
        last_sum, last_level = 0, 0
        nodes = deque([(root, 0)])

        while nodes:
            node, level = nodes.popleft()

            # If the level is greater than the last level, then we have reached a new level.
            if level == last_level:
                last_sum += node.val
                last_level = level
            else:
                last_sum = node.val
                last_level = level

            if node.left:
                nodes.append((node.left, level + 1))
            if node.right:
                nodes.append((node.right, level + 1))

        return last_sum

# Runtime: 655 ms, faster than 5.01% of Python3 online submissions
# Memory Usage: 17.8 MB, less than 29.16% of Python3 online submissions
