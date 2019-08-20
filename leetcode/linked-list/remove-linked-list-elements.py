'''
203. [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
'''

# Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        head_ref = ListNode(None)
        new_pointer = head_ref
        while head:
            if head.val != val:
                new_node = ListNode(head.val)
                head_ref.next = new_node
                head_ref = head_ref.next
            head = head.next
        head = None
        head_ref = None
        return new_pointer.next

# Runtime: 84 ms
# Memory Usage: 18.5 MB


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        head_ref = ListNode(None)
        head_ref.next = head
        new_pointer = head_ref
        while head_ref:
            
            if head_ref.val == val:
                temp = head_ref.next
                head_ref = prev
                head_ref.next = temp
            else:
                prev = head_ref
                head_ref = head_ref.next

        return new_pointer.next


# Runtime: 76 ms
# Memory Usage: 16.9 MB