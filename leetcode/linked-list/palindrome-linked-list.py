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
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


class Solution:
    """
    Uses 2 pass for reverse
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing Second Half
        temp = None
        while slow:
            next_node = slow.next
            slow.next = temp
            temp = slow
            slow = next_node

        # Check Palindrome
        while temp:
            if temp.val != head.val:
                return False
            head = head.next
            temp = temp.next
        return True


# Runtime: 64 ms, faster than 89.80% of Python3 online submissions
# Memory Usage: 22.7 MB, less than 100.00% of Python3 online submissions


class Solution:
    """
    Use 1 pass for reverse
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def isPalindrome(self, head: ListNode) -> bool:
        # Base Cases
        if not head:
            return False
        if not head.next:
            return True

        # Reverse First Half, in one pass
        slow = fast = head
        odd = False
        prev = None
        while fast:
            if not fast.next:
                odd = True
                break
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Move one ahead if odd nodes
        if odd:
            slow = slow.next

        # Return if slow is None
        if not slow:
            return False

        l1 = prev
        l2 = slow

        # Check Palindrome
        while l1:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return True


# Runtime: 660 ms, faster than 50.16% of Python3 online submissions
# Memory Usage: 31.3 MB, less than 55.65% of Python3 online submissions
