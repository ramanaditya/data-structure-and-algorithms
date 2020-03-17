"""
[1022. Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the
most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary,
which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.



Example 1:
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22


Note:
The number of nodes in the tree is between 1 and 1000.
node.val is 0 or 1.
The answer will not exceed 2^31 - 1.
"""


# Solutions

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.temp = []
        self.res = 0

    def sumRootToLeaf(self, root: TreeNode, level=0) -> List[str]:
        if root is None:
            return
        while len(self.temp) > level:
            self.temp.pop()
        self.temp.append(root.val)
        level += 1
        if not root.left and not root.right:
            string = "".join([str(i) for i in self.temp])
            self.res += int(string, 2)
        else:
            self.sumRootToLeaf(root.left, level)
            self.sumRootToLeaf(root.right, level)
        return self.res


# Runtime: 32 ms, faster than 85.95% of Python3 online submissions
# Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions
