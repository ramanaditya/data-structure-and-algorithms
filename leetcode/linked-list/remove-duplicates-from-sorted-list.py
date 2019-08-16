'''
## Questions

### 83. [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

Given a sorted linked list, delete all duplicates such that each element appear only once.

**Example 1:**

```
Input: 1->1->2
Output: 1->2
```

**Example 2:**

```
Input: 1->1->2->3->3
Output: 1->2->3
```
'''

## Solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        head_ref = head
        if not head:
            return head_ref
        while head.next != None:
            if head.val == head.next.val:
                head.next = head.next.next
            else:  
                head = head.next
        return head_ref

# Runtime: 48 ms
# Memory Usage: 14 MB