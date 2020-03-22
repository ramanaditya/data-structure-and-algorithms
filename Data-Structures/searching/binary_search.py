"""
==============
Binary Search
==============
"""
import sys


class BinarySearch:
    def binary_search(self, array, key):
        low = 0
        high = len(array)
        while low < high:
            mid = (low + high) // 2
            if array[mid] == key:
                return mid
            elif array[mid] < key:
                low = mid + 1
            else:
                high = mid
        return -1


if __name__ == "__main__":
    print(
        """
    Binary Search
    
    Input Format
    first line contains space separated sorted elements eg., 1 2 3 4 5 6 7 8 9
    Second line contains the key to be searched  eg., 7
    """
    )
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    array = data[:-1]
    key = data[-1]
    res = BinarySearch().binary_search(array, key)
    if res == -1:
        print("Key not found")
    else:
        print("Key : '{}' found at index : {}".format(key, res + 1))
