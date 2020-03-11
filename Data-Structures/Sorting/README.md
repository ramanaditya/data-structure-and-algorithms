# Sorting

| Sl No. | Algorithm | Worst Time | Average Time | Best Time | Memory | Solution |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 1. | Bubble Sort | O(n^2) | O(n^2) | O(n) | O(1) | [Python](https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/Data-Structures/Sorting/bubble-sort.py) |



## Heapsort

```
- Running Time : O(n log n)
- In Place Sorting
```

### Heaps
The (binary) heap data structure is an array object that we can view as a nearly complete binary tree

#### Calculating indices 
> For index with starting with 1
```
PARENT(i)
    return int(i/2)

LEFT(i)
    return 2i

RIGHT(i)
    return 2i + 1
```

> For index with starting with 0
```
PARENT(i)
    return int(i/2)

LEFT(i)
    return 2i + 1

RIGHT(i)
    return 2i + 2
```

There are two kinds of binary heaps: 
- max-heaps 
- min-heaps. 

In both kinds, the values in the nodes satisfy a heap property, the specifics of which depend on the kind of heap. 

In a max-heap, the max-heap property is that for every node i other than the root, ```A[PARENT(i)]􏰃 >= A[􏰀i]```
that is, the value of a node is at most the value of its parent. Thus, the largest element in a max-heap is stored at 
the root, and the subtree rooted at a node contains values no larger than that contained at the node itself.

A min-heap is organized in the opposite way; the min-heap property is that for every node i other than the root,
```A[PARENT(i)] <= A[􏰀i]``` The smallest element in a min-heap is at the root.