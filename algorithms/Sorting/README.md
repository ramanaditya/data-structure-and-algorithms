# Sorting

| Sl No. | Algorithm | Worst Time | Average Time | Best Time | Memory | Stability |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| 1. | Bubble Sort | O(n^2) | O(n^2) | O(n) | O(1) | Stable |
| 2. | Selection Sort | O(n^2) | O(n^2) | O(n^2) | O(1) | Unstable |
| 3. | Insertion Sort | O(n^2) | O(n^2) | O(n^2) | O(1) | Stable |
| 3. | Merge Sort | O(n log(n) ) | O(n log(n) ) | O(n log(n) ) | O(n) | Stable |
| 4. | Quick Sort | O(n log(n) ) | O(n log(n) ) | O(n^2 ) ) | O( log(n) ) | Unstable |

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

> Insertion sort is used when number of elements is small. 
> It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.

## Merge Sort
| [Python](https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/Data-Structures/Sorting/merge-sort.py) |
```
- Running Time : O(n log(n) )
- Memory : O(1)
- In Place Sorting
- Stable Sorting
```

```python
def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

```

## Quick Sort
| [Python](https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/Data-Structures/Sorting/quick-sort.py) |
```
- Running Time : O( n^2 )
- Memory : O( log(n) )
- In Place Sorting
- Unstable Sorting
```

#### Algorithm for partition
```python
def partition(data, low, high):
    pivot = data[high]
    i = low  # To keep the index of element smaller than pivot
    j = low  # To keep the index of element greater than pivot

    while j < high:
        if data[j] < pivot:
            data[j], data[i] = data[i], data[j]
            i += 1
        j += 1

    data[i], data[high] = data[high], data[i]

    return i
```
#### Recursive Algorithm for quicksort
```python
def quick_sort(data, low, high):
    if low < high:
        pivot = partition(data, low, high)
        quick_sort(data, low, pivot - 1)
        quick_sort(data, pivot + 1, high)
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