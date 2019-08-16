/*
## Questions

### 234. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

Given a singly linked list, determine if it is a palindrome.

**Example 1:**

```
Input: 1->2
Output: false
```

**Example 2:**

```
Input: 1->2->2->1
Output: true
```

**Follow up:**
Could you do it in O(n) time and O(1) space?

*/

// Solutions

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        struct ListNode *head_ref = head;
        int count = 0;
        if(head == NULL){
            return true;
        }
        while(head!=NULL){
            count += 1;
            head = head -> next;
        }
        int a[count];
        int i = 0,j;
        while(head_ref != NULL){
            a[i] = head_ref -> val;
            i += 1;
            head_ref = head_ref -> next;
        }
        j = count;
        i = 0;
        while(i<j){
            if(a[i] != a[j - 1]){
                return false;
            }
            i += 1;
            j -= 1;
        }
        return true;
    }
};

// Runtime: 20 ms
// Memory Usage: 13.1 MB
