"""
## Questions

### 234. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

Given a singly linked list, determine if it is a palindrome.

**Example 1:**

```
Input: 1->2
Output: false
```

**Example 2:**

```
Input: 1->2->2->1
Output: true
```

**Follow up:**
Could you do it in O(n) time and O(1) space?
"""


## Solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        a = []
        while head != None:
            a.append(head.val)
            head = head.next
        i = 0
        j = len(a) - 1
        while i < j:
            if a[i] != a[j]:
                return False
            i += 1
            j -= 1
        return True


# Runtime: 76 ms
# Memory Usage: 24.7 MB


# Solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = None
        while slow:
            next_node = slow.next
            slow.next = temp
            temp = slow
            slow = next_node
        while temp:
            if temp.val != head.val:
                return False
            head = head.next
            temp = temp.next
        return True


# Runtime: 64 ms, faster than 89.80% of Python3 online submissions
# Memory Usage: 22.7 MB, less than 100.00% of Python3 online submissions
