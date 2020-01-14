# Linked List

A linked-list is a sequential list of nodes that hold data which point to other nodes also containing data

### Where are they used

- Used in many list, queue & stack implementation
- For creating Circular List
- Used in separate chaining, which is present certain hashtable implementations to deal with hashing collisions
- Often used in the implementation of the adjacency lists for graph

### Pros and Cons
| | Pros | Cons |
| --- | --- | --- |
| Singly Linked List | - Uses Less Memory | Can't easily access previous elements |
| | - Simpler Implementation | |
| Doubly Linked List | - Can be Traversed backwards | Takes 2x memory |

### Complexity
| | Singly Linked List | Doubly Linked List |
| --- | --- | --- |
| Search | O(n) | O(n) |
| Insert at Head | O(1) | O(1) |
| Insert at Tail | O(1) | O(1) |
| Remove at Head | O(1) | O(1) |
| Remove at Tail | O(n) | O(1) |
| Remove in middle | O(n) | O(n) |