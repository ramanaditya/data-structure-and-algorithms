"""
## Questions
Medium
### 24. [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

## Solutions

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """Using Recursion"""

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        if not head.next.next:
            temp = head
            head = head.next
            head.next = temp
            head.next.next = None
            return head

        def swap(head1, slow, fast, prev):
            if slow and not slow.next:
                return head1
            slow.next = fast.next
            fast.next = slow
            if prev is None:
                head1 = fast
            else:
                prev.next = fast
            if slow and slow.next:
                prev = slow
                slow = slow.next
                fast = slow.next
                swap(head1, slow, fast, prev)
                return head1

        return swap(None, head, head.next, None)


# Runtime: 24 ms, faster than 91.57% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 6.06% of Python3 online submissions


class Solution:
    """
    Iterative Solution
    Time Complexity: O( n )
    Space Complexity: O( 1 )
    """

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        head_ref = head
        prev = None

        while head and head.next:
            fast = head.next
            slow = head

            slow.next = head.next.next
            fast.next = slow

            if prev:
                prev.next = fast
                prev = slow
            else:
                prev = slow
                head_ref = fast

            head = head.next
        return head_ref


# Runtime: 20 ms, faster than 97.86% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 6.06% of Python3 online submissions


# Definition for singly-linked list.
class Solution:
    """
    Time Complexity: O( n )
    Space Complexity: O( 1 )
    """

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Add None node in the start of head
        head_ref = ListNode(None)
        head_ref.next = head
        head = head_ref

        while head and head.next and head.next.next:
            slow = head.next
            fast = slow.next

            slow.next = fast.next
            fast.next = slow

            head.next = fast
            head = slow

        return head_ref.next


# Runtime: 24 ms, faster than 96.70% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 37.66% of Python3 online submissions
