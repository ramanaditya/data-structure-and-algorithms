# Searching

| Sl No. | Algorithm | Worst Time | Average Time | Best Time | Memory |
| :---: | :--- | :---: | :---: | :---: | :---: 
| 1. | Linear Search | O(n) | O(n) | O(1) | O(1)|
| 2. | Binary Search | O( log(n) ) | O( log(n) ) | O(1) | O(1) |

## Linear Search
| [Python](https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/Data-Structures/searching/linear_search.py) |
```text
- TIme Complexity
    - Worst Case : O(n)
    - Average Case : O(n)
    - Best Case : O(1)
- Space Complexity : O(1)
```

```python
def linear_search(self, array, key):
    for i in range(len(array)):
        if array[i] == key:
            return i
    return -1
```

## Binary Search
| [Python](https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/Data-Structures/searching/binary_search.py) |
```text
- TIme Complexity
    - Worst Case : O( log(n) )
    - Average Case : O( log(n) )
    - Best Case : O(1)
- Space Complexity : O(1)
```

```python
def binary_search(array, key):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```