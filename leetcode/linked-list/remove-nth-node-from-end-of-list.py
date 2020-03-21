"""
## Questions

### 19. [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

Given a linked list, remove the n-th node from the end of list and return its head.

**Example:**

```
Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
```
**Note:**
- Given n will always be valid.

**Follow up:**
- Could you do this in one pass?
"""

## Solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    In one pass, optimized Solution
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or n < 1:
            return
        fast, slow = head, head
        for i in range(n):
            fast = fast.next
        if not fast:
            head = head.next
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


# Runtime: 28 ms, faster than 84.67%
# Memory Usage: 12.7 MB, less than 100.00%


class Solution:
    """
    Counting the elements in first pass then deleting the node at count - n -1
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return head
        head_ref1 = ListNode(None)
        head_ref1.next = head
        head_ref = ListNode(None)
        head_ref.next = head
        head_ref = head_ref.next
        count = 0
        while head_ref != None:
            count += 1
            head_ref = head_ref.next
        if n >= count:
            return head_ref1.next.next
        req = count - n - 1
        while req > 0:
            head = head.next
            req -= 1
        if head.next.next == None:
            head.next = None
        else:
            head.next = head.next.next
        return head_ref1.next


# Runtime: 40 ms
# Memory Usage: 13.7 MB


class Solution:
    """
    Using List, memory inefficient
    """

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a = []
        head1 = head
        l = ListNode(None)
        head_ref = l
        while head1:
            a.append(head1.val)
            head1 = head1.next
        try:
            a.pop(-n)
        except:
            return
        i = 0
        while i < len(a):
            new_node = ListNode(a[i])
            l.next = new_node
            l = l.next
            i += 1
        return head_ref.next


# Runtime: 44 ms
# Memory Usage: 13.9 MB
