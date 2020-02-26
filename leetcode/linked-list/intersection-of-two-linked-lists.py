"""
## Questions

### [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
begin to intersect at node c1.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:
Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

## Solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return
        countA = 0
        countB = 0
        res = 0
        fastA = headA
        fastB = headB
        while fastA and fastA.next and fastB and fastB.next:
            countA += 1
            countB += 1
            fastA = fastA.next.next
            fastB = fastB.next.next
        countA *= 2
        countB *= 2
        while fastA:
            countA += 1
            fastA = fastA.next
        while fastB:
            countB += 1
            fastB = fastB.next
        diff = abs(countA - countB) or 0
        i = 0

        while i < diff and countA < countB:
            headB = headB.next
            i += 1

        while i < diff and countB < countA:
            headA = headA.next
            i += 1

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None


# Runtime: 164 ms, faster than 74.75% of Python3 online submissions
# Memory Usage: 28 MB, less than 100.00% of Python3 online submissions


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        carry = 0
        l3 = ListNode(None)
        head_ref = l3
        while l1 and l2:
            c = l1.val + l2.val + carry
            if c < 9:
                new_node = ListNode(c)
                l3.next = new_node
                carry = 0
            else:
                new_node = ListNode(c % 10)
                l3.next = new_node
                carry = c // 10
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            c = l1.val + carry
            if c < 9:
                new_node = ListNode(c)
                l3.next = new_node
                carry = 0
            else:
                new_node = ListNode(c % 10)
                l3.next = new_node
                carry = c // 10
            l3 = l3.next
            l1 = l1.next
        while l2:
            c = l2.val + carry
            if c < 9:
                new_node = ListNode(c)
                l3.next = new_node
                carry = 0
            else:
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
