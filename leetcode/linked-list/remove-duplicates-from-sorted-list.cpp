/*
## Questions

### 83. [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

Given a sorted linked list, delete all duplicates such that each element appear only once.

**Example 1:**

```
Input: 1->1->2
Output: 1->2
```

**Example 2:**

```
Input: 1->1->2->3->3
Output: 1->2->3
```
*/

// Solutions

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode* head_ref = head;
    if(head == NULL){
        return head;
    }
    while(head->next != NULL){
        if(head->val == head->next->val){
            head -> next = head -> next -> next;
        }
        else{
            head = head -> next;
        }
    }
    return head_ref;
}

// Runtime: 4 ms
// Memory Usage: 7.7 MB
