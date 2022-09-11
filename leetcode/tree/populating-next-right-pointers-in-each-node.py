"""
Medium
[116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/)
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:

      1            1 -> NULL
     /  \        /  \
    2    3      2 -> 3 -> NULL
   / \  / \    / \  / \
  4  5 6   7  4->5->6->7 -> NULL

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point
to its next right node, just like in Figure B. The serialized output is in level order as connected by the next
pointers, with '#' signifying the end of each level.

Example 2:
Input: root = []
Output: []


Constraints:
The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000

Follow-up:
You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return

        root.next = None
        queue = deque([(root, 0)])
        root_node = root
        max_level = 0
        prev = None

        while queue:
            node, level = queue.popleft()
            if level > max_level:
                max_level = level
                prev = None
            node.next = prev
            prev = node
            if node.right:
                queue.append((node.right, level + 1))
            if node.left:
                queue.append((node.left, level + 1))

        return root_node

# Runtime       : 130 ms, faster than 18.39% of Python3 online submissions
# Memory Usage  : 16 MB, less than 5.47% of Python3 online submissions


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root


# Runtime       : 125 ms, faster than 22.40% of Python3 online submissions
# Memory Usage  : 15.5 MB, less than 96.81% of Python3 online submissions