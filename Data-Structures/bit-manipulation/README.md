# Bit Manipulation

## AND
| A | B | AND (A & B) |
| :---: | :---: | :---: |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

## OR
| A | B | AND (A \| B) |
| :---: | :---: | :---: |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

## NOT
| A | NOT ( ~A ) |
| :---: | :---: |
| 0 | 1 |
| 1 | 0 |

## XOR
| A | B | AND (A ^ B) |
| :---: | :---: | :---: |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## Finding bit length of any number
```python
def bit_length_of_binary(n: int) -> int:
    return n.bit_length()
```

## Converting any decimal to binary and vice-versa
```python
def convert_to_binary(n: int) -> str:
    return bin(n)[2:]

def convert_to_decimal(s: str) -> int:
    return int(s,2)
```

## Check for even or odd
```python
def check_even(n: int) -> int:
    return True if n & 1 == 0 else False
```

## Check for unique number from a list of duplicates
```python
def find_unique(arr: list) -> int:
    xor = arr[0]
    for i in range(1,len(arr)):
        xor ^= arr[i]
    return xor
``` 

## Finding Complement of a number
```python
def complement(n: int) -> int:
    """
    xor with a binary number 1...1(m times), where m is the bit length 
    of the number will give complement of that number
    """
    return ((1 << n.bit_length()) - 1) ^ n
```
