# Searching

| Sl No. | Algorithm | Worst Time | Average Time | Best Time | Memory |
| :---: | :--- | :---: | :---: | :---: | :---: 
| 1. | Linear Search | O(n) | O(n) | O(1) | O(1)|

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