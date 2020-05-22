# Dictionary: Some useful piece of Code during programming

### Counting the occurrence of elements
```python
from collections import Counter
def occurrence(s: str) -> dict:
    """
    s can be list/string/tuple
    It will return a dictionary with key as elements and value as their 
    number of occurrences
    """
    d = Counter(s)  
    return d
```
