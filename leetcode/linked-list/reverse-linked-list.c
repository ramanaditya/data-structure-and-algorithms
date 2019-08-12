/*
## Questions

### 206. [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

Reverse a singly linked list.

**Example:**

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

**Follow up:**

A linked list can be reversed either iteratively or recursively. Could you implement both?
*/

// Solutions

/*
 *
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
*/

struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *prev = NULL;
    struct ListNode *nextnode = NULL;
    while(head != NULL){
        nextnode = head->next;
        head->next = prev;
        prev = head;
        head = nextnode;
    }
    return prev;
}

// Runtime: 4 ms
// Memory Usage: 7.7 MB
