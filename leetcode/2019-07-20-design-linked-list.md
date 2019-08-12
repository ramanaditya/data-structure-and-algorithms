---
layout: page
title: "707. Design Linked List"
subtitle: 
description: ""
author: "aditya"
comments: true
image: assets/images/code_pic.png
meta_image: assets/images/code_pic_meta.png
categories: [code,leetcode]
tags: [python,linked-list,easy]
extra_tags: 
leetcode_slno: 707
featured: false
excerpt: ""
hidden: true
permalink: /:categories/:title

---

## Questions

### 707. [Design Linked List](https://leetcode.com/problems/design-linked-list/)

Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: ```val``` and ```next```. ```val``` is the value of the current node, and ```next``` is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute ```prev``` to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

- get(index) : Get the value of the ```index```-th node in the linked list. If the index is invalid, return ```-1```.
- addAtHead(val) : Add a node of value ```val``` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- addAtTail(val) : Append a node of value ```val``` to the last element of the linked list.
- addAtIndex(index, val) : Add a node of value ```val``` before the ```index```-th node in the linked list. If ```index``` equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. If index is negative, the node will be inserted at the head of the list.
- deleteAtIndex(index) : Delete the ```index```-th node in the linked list, if the index is valid.

**Example:**

```
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3
```

**Note:**

- All values will be in the range of [1, 1000].
- The number of operations will be in the range of [1, 1000].
- Please do not use the built-in LinkedList library.

## Solutions

{% highlight python %}

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head
        count = 0
        if self.head is None:
            return -1
        if index == 0:
            return self.head.data
        while curr:
            if count == index:
                return curr.data
            count += 1
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        temp = self.head
        if self.head is None:
            self.head = new_node
        while temp.next:
            temp = temp.next
        temp.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        new_node = Node(val)
        curr = self.head
        if index < 1:
            self.head = new_node
            return
        count = 0
        prev = self.head
        while curr:
            count += 1
            if count == index:
                new_node.next = prev.next
                prev.next = new_node
                break
            prev = curr.next
            curr = curr.next
            
        if count == index:
            curr.next = new_node
        else:
            return -1
        
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.head == None:
            return -1
        curr = self.head
        if index == 0:
            self.head = curr.next
            return
        if index < 0:
            return -1
        for i in range(index - 1):
            curr = curr.next
            if curr is None:
                break
        if curr is None:
            return -1
        if curr.next is None:
            return -1
        
        next = curr.next.next
        curr.next = None
        curr.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

# Runtime: 336 ms
# Memory Usage: 14.5 MB

{% endhighlight %}