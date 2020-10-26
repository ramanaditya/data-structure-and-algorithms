""""""
"""
==============
Binary Search
==============

TIme Complexity
    Worst Case : O( log(n) )
    Average Case : O( log(n) )
    Best Case : O(1)
Space Complexity : O(1)

Binary Search is a sorting algorithm in which we select the mid element and compare key to the mid element if key is
smaller then we search before mid else after mid. If key is found we return the index of key else -1.
"""

import sys


class BinarySearch:
    def binary_search(self, array, key):
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


if __name__ == "__main__":
    print(
        """
    ==============
    Binary Search
    ==============
    
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
