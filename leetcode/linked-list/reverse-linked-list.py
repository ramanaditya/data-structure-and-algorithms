"""
## Questions

### 206. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
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

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Pointer to track the reversed list
        prev = None

        while head:
            # Storing next value
            temp = head.next

            # Reverse
            head.next = prev
            prev = head

            # Increment head
            head = temp

        return prev


# Runtime: 28 ms, faster than 97.79% of Python3 online submissions
# Memory Usage: 15.1 MB, less than 93.46% of Python3 online submissions
