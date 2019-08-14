'''
## Questions

### 21. [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example 1:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

## Solutions


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def __init__(self): 
        self.head = None
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        if not l1:
            return l2
        if not l2:
            return l1
        l3 = ListNode(None)
        head.next = l3
        while l1 and l2:
            if l1.val > l2.val :
                l3.next = l2
                l3 = l3.next
                l2 = l2.next
                
            else:
                l3.next = l1
                l3 = l3.next
                l1 = l1.next
        while l1:
            l3.next = l1
            l3 = l3.next
            l1 = l1.next
            
        while l2:
            l3.next = l2
            l3 = l3.next
            l2 = l2.next 
        head = head.next.next
        return head

# Runtime: 40 ms
# Memory Usage: 13.9 MB
