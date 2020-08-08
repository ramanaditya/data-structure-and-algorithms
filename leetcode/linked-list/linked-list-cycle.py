"""
## Questions

### 141. [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the
linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?
"""


# Solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Time Complexity: O( n )
    Space Complexity: O( 1 )
    """

    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return head

        # Initializing two pointers
        fast, slow = head, head

        while fast and fast.next:

            # Iterations
            fast = fast.next.next
            slow = slow.next

            # If cycle then fast and slow will intersect
            if fast == slow:
                return True

        # If linked-list comes at the end
        return False


# Runtime: 36 ms, faster than 99.72% of Python3 online submissions
# Memory Usage: 16.9 MB, less than 55.80% of Python3 online submissions
