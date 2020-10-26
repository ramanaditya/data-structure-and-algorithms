"""
## Questions: MEDIUM

### 143. [Reorder List](https://leetcode.com/problems/reorder-list/)

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.

Example 2:
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
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

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Base Case
        if not head:
            return None

        # Find the middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Separate two lists
        next = slow.next
        slow.next = None
        slow = next

        # Reverse second list
        l1, l2 = head, None
        while slow:
            next = slow.next
            slow.next = l2
            l2 = slow
            slow = next

        # Merge two lists
        while l1 and l2:
            next1 = l1.next
            next2 = l2.next
            l1.next = l2
            l2.next = next1
            l1 = next1
            l2 = next2


# Runtime: 72 ms, faster than 100.00% of Python3 online submissions
# Memory Usage: 23.1 MB, less than 79.26% of Python3 online submissions
