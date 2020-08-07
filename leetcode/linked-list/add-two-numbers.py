"""
## Questions

### 2. [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order
and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    """
    Time Complexity: O( max(n, m) )
    Space Complexity: O( m + n + max(n, m) )
    Converting List to Array
    """

    def __init__(self):
        self.head = None

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = []
        b = []
        if not l1:
            return l2
        if not l2:
            return l1
        while l1 and l2:
            a.append(l1.val)
            b.append(l2.val)
            l1 = l1.next
            l2 = l2.next
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next

        if len(a) != len(b):
            k = len(a) - len(b)
            if k > 0:
                while k > 0:
                    b.append(0)
                    k -= 1
            else:
                k = k * (-1)
                while k > 0:
                    a.append(0)
                    k -= 1
        a = a[::-1]
        b = b[::-1]
        res = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 and j >= 0:
            c = a[i] + b[j] + carry
            if c < 9:
                res.append(c)
                carry = 0
                i -= 1
                j -= 1
            else:
                res.append(c % 10)
                carry = c // 10
                i -= 1
                j -= 1
        if carry > 0:
            res.append(carry)
        i = len(res) - 1
        new_node = ListNode(None)
        while i >= 0:
            new_node = ListNode(res[i])
            new_node.next = self.head
            self.head = new_node
            i -= 1
        return new_node


# Runtime: 84 ms
# Memory Usage: 14 MB


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time Complexity: O( max(n, m) )
    Space Complexity: O( max(n, m) )
    Single Pass Solution
    """

    def __init__(self):
        self.head = None

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        carry = 0
        head_ref = l3 = ListNode(None)

        while l1 and l2:
            c = l1.val + l2.val + carry
            new_node = ListNode(c % 10)
            l3.next = new_node
            carry = c // 10
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            c = l1.val + carry
            new_node = ListNode(c % 10)
            l3.next = new_node
            carry = c // 10
            l3 = l3.next
            l1 = l1.next

        while l2:
            c = l2.val + carry
            new_node = ListNode(c % 10)
            l3.next = new_node
            carry = c // 10
            l3 = l3.next
            l2 = l2.next

        if carry > 0:
            new_node = ListNode(carry)
            l3.next = new_node

        l3 = head_ref.next

        return l3


# Runtime: 72 ms, faster than 50.09% of Python3 online submissions
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time Complexity: O( max(n, m) )
    Space Complexity: O( max(n, m) )
    Single Pass Solution
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = temp = ListNode(None)
        total = 0

        while l1 or l2 or total:
            total += (0 if not l1 else l1.val) + (0 if not l2 else l2.val)
            temp.next = ListNode(total % 10)
            temp = temp.next

            total //= 10

            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next

        return head.next


# Runtime: 80 ms, faster than 53.20% of Python3 online submissions
# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions
