# List: Some useful pieces of Code during programming

## Sorting a list os lists based upon 2nd index or other
```python
def sort_it(arr: list) -> list:
    """
    sorted takes 3 arguments
    - iterable : list/tuple/string
    - key(optional) the key on which you want to sort
    - reverse(optional) default is False, make it True for reverse sorting 
    
    return a sorted list
    """
    return sorted(arr, key = lambda ele: ele[1], reverse = False)
    
```