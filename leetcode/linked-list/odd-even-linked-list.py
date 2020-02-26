"""
## Questions
### [328. Odd Even Linked List](https://leetcode.com/problems/odd-even-linked-list/)
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""

## Solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        odd_head = odd = ListNode(0)
        even_head = even = ListNode(0)
        count = 1
        while head is not None:
            if count & 1:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            count += 1
            head = head.next
        even.next = None
        odd.next = even_head.next
        return odd_head.next


# Runtime: 36 ms, faster than 93.81% of Python3 online submissions
# Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions
