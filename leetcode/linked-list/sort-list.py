"""
## Questions: MEDIUM

### 148. [Sort List](https://leetcode.com/problems/sort-list/)

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Solutions


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        # Splitting the list into two parts
        def mergeSort(head):
            if not head or not head.next:
                return head

            slow, fast, prev = head, head, None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next

            prev.next = None

            left = mergeSort(head)
            right = mergeSort(slow)
            return merge(left, right)

        # Sorting the list
        def merge(left, right):
            head_ref = dummy = ListNode()
            while left and right:
                if left.val > right.val:
                    dummy.next = right
                    right = right.next

                else:
                    dummy.next = left
                    left = left.next

                dummy = dummy.next

            if left:
                dummy.next = left

            if right:
                dummy.next = right

            return head_ref.next

        return mergeSort(head)


# Runtime: 244 ms, faster than 65.16% of Python3 online submissions
# Memory Usage: 23 MB, less than 56.38% of Python3 online submissions
