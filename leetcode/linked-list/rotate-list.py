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
	
	# If list is empty or has only one element it doesn't matter the number of times you rotate
        if not head or not head.next:
            return head
		
	# If number of rotation is zero, the list will be same
        if k == 0:
            return head
		
	# Copying head to another variable because we have to iterate over head
        head1 = head
		
	# to count the no. of nodes
	count = 0    
        while head:
            count += 1
            head = head.next
		
	# Getting the index from which the list will split
	# Actual index woul dbe k % count from the right, but 
	# we have to get the index from left so we have to subtract this from count
        index = count - (k % count)
		
	# Here count=1 because the index value we got started from 1
	# Alternatively we can subtract 1 from index and start count from 0
        count = 1
		
	# Another list to store one part of the list
        temp = ListNode(-1)
		
	# Again copying the head because previous iteration took head to the last node
        head = head1
        while head1:
            if count == index:
		# You can also put return statement while just running the code below head1.next to check what actually both temp and head stores
                temp.next = head1.next    # temp will store the first part of the resulting list
                head1.next = None     # As head1 will be the last part of the list so last node must point to NULL value
		# return temp
		# return head
                break
            count += 1
            head1 = head1.next
		
	# If one of the part doesn't contain any nodes
        if temp.next == None:
            return head
		
	# If both temp and head have some nodes
        head2 = temp.next    
		
        while temp.next != None:
            temp = temp.next
        temp.next = head
        return head2

# Runtime: 36 ms
# Memory Usage: 13.9 MB
