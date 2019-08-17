'''
## Questions

### 445. [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:

- What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
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
        a = a[::-1]
        b = b[::-1]
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
        print(a,b)
        res = []
        carry = 0
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            c = a[i] + b[j] + carry
            if c < 9:
                res.append(c)
                carry = 0
                i += 1
                j += 1
            else:
                res.append(c%10)
                carry = c // 10
                i += 1
                j += 1
        if carry > 0:
            res.append(carry)
        res = res[::-1]
        i = len(res) - 1
        new_node = ListNode(None)
        while i >= 0:
            new_node = ListNode(res[i])
            new_node.next = self.head
            self.head = new_node
            i -= 1
        return new_node

# Runtime: 88 ms
# Memory Usage: 14 MB


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = 0
        if not l1:
            return l2
        if not l2:
            return l1
        while l1:
            a = a * 10 + l1.val
            l1 = l1.next
        b = 0
        while l2:
            b = b * 10 + l2.val
            l2 = l2.next
        c = a + b
        if c == 0:
            new_node = ListNode(c)
            return new_node
        l3 = None
        while c != 0:
            q = c % 10
            new_node = ListNode(q)
            new_node.next = l3
            l3 = new_node
            c = c//10
        return l3
            
# Runtime: 72 ms
# Memory Usage: 13.9 MB