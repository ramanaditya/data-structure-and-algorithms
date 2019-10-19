'''
## Questions
### 61. [Rotate List](https://leetcode.com/problems/rotate-list/)
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
'''

## Solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        if k == 0:
            return head
        head1 = head
        count = 0
        while head:
            count += 1
            head = head.next
        index = count - (k % count)
        count = 1
        temp = ListNode(-1)
        head = head1
        while head1:
            if count == index:
                temp.next = head1.next
                head1.next = None
                break
            count += 1
            head1 = head1.next
        if temp.next == None:
            return head
        head2 = temp.next    
        while temp.next != None:
            temp = temp.next
        temp.next = head
        return head2

# Runtime: 36 ms
# Memory Usage: 13.9 MB
