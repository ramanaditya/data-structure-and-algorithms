"""
## Questions: MEDIUM

### 142. [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the
linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow-up:
Can you solve it without using extra space?
"""


# Solutions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        track = dict()
        while head:
            if track.get(head):
                return head

            track[head] = head
            head = head.next

        return None


# Runtime: 40 ms, faster than 99.46% of Python3 online submissions
# Memory Usage: 16.7 MB, less than 90.57% of Python3 online submissions


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        # Two pointers
        tortoise, hare = head, head

        while True:
            # Condition when pointer reaches to end
            if not hare or not hare.next:
                return None

            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                break

        # Iterating over the ll to find
        tortoise = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next

        # Returning node where cycle was found
        return tortoise


# Runtime: 48 ms, faster than 91.52% of Python3 online submissions
# Memory Usage: 16.8 MB, less than 81.29% of Python3 online submissions
