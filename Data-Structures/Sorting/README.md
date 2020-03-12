# Sorting

| Sl No. | Algorithm | Worst Time | Average Time | Best Time | Memory | Stability |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1. | Bubble Sort | O(n^2) | O(n^2) | O(n) | O(1) | Stable |
| 2. | Selection Sort | O(n^2) | O(n^2) | O(n^2) | O(1) | Unstable |
| 3. | Insertion Sort | O(n^2) | O(n^2) | O(n^2) | O(1) | Stable |

> **Stable** : Relative position of equal elements after sorting remains same.
>
> **In-place Sorting** : Sorting Input elements without having backup, thus unsorted form is lost.


## Bubble Sort
| [Python](https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/Data-Structures/Sorting/bubble-sort.py) |
```
- Running Time : O(n^2)
- Memory : O(1)
- In Place Sorting
- Stable Sorting
```

```python
def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(0, len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print(data)
```

## Selection Sort
| [Python](https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/Data-Structures/Sorting/selection-sort.py) |
```
- Running Time : O(n^2)
- Memory : O(1)
- In Place Sorting
- Unstable Sorting
```

```python
def selection_sort(data):
    for i in range(len(data)):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[min_index] > data[j]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    print(data)
```

## Insertion Sort
| [Python](https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/Data-Structures/Sorting/insertion-sort.py) |
```
- Running Time : O(n^2)
- Memory : O(1)
- In Place Sorting
- Stable Sorting
```

```python
def insertion_sort(self, data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    print(data)
```

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