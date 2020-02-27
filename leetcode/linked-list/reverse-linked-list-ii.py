"""
## Questions
### [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

## Solutions

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m > n:
            return
        count = 0
        head_ref = start = ListNode(0)
        mid_ref = ListNode(0)
        while count < m - 1 and head:
            start.next = head
            start = start.next
            count += 1
            head = head.next
        start.next = None
        mid_ref = mid_ref.next
        while count < n and head:
            temp = head.next
            head.next = mid_ref
            mid_ref = head
            count += 1
            head = temp
        mid = mid_ref
        while mid.next:
            mid = mid.next
        mid.next = head
        start.next = mid_ref
        return head_ref.next


# Runtime: 16 ms, faster than 99.96% of Python3 online submissions
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions
