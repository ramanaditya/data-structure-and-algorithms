"""
## Questions

### 445. [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:

- What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
"""


# Solutions

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time Complexity: O( max(n, m) )
    Space Complexity: O( max(n, m) )
    Converting List to Array
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        total = 0
        head = None

        while stack1 or stack2 or total:
            total += 0 if not len(stack1) else stack1.pop()
            total += 0 if not len(stack2) else stack2.pop()

            temp = ListNode(total % 10)
            temp.next = head
            head = temp

            total //= 10

        return head


# Runtime: 76 ms, faster than 78.28% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 83.45% of Python3 online submissions


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Time Complexity: O( max(n, m) )
    Space Complexity: O( max(n, m) )
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        num1 = 0
        num2 = 0

        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next

        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next

        total = num1 + num2

        if total == 0:
            new_node = ListNode(total)
            return new_node

        l3 = None

        while total != 0:
            new_node = ListNode(total % 10)
            new_node.next = l3
            l3 = new_node
            total //= 10

        return l3


# Runtime: 68 ms, faster than 96.35% of Python3 online submissions
# Memory Usage: 13.6 MB, less than 93.79% of Python3 online submissions
