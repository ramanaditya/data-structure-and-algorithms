'''
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
'''


## Solutions

{% highlight python %}

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
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

{% endhighlight %}