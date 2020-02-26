"""
[589. N-ary Tree Preorder Traversal](https://leetcode.com/problems/n-ary-tree-preorder-traversal/)
Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated
by the null value (See examples).



Follow up:
Recursive solution is trivial, could you do it iteratively?

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]


Constraints:
The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def __init__(self):
        self.res = []

    def preorder(self, root: "Node") -> List[int]:
        if not root:
            return None
        else:
            self.res.append(root.val)
            for i in range(len(root.children)):
                self.preorder(root.children[i])
        return self.res


# Runtime: 48 ms, faster than 83.24% of Python3 online submissions
# Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions
