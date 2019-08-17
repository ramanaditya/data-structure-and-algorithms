'''
## Questions

### 23. [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

**Example:**

```
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

## Solutions


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        length = len(lists)
        a = []
        i = 0
        for i in range(length):
            j = 0
            temp_head = lists[i]
            while temp_head:
                a.append(temp_head.val)
                temp_head = temp_head.next
        a.sort()
        l = ListNode(None)
        head = l
        i = 0
        j = len(a)
        while i < j:
            new_node = ListNode(a[i])
            l.next = new_node
            l = l.next
            i += 1
        l = head.next
        return l

# Runtime: 100 ms
# Memory Usage: 18 MB