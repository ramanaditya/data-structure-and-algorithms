""""""
"""
==============
Linear Search
==============

TIme Complexity
    Worst Case : O(n)
    Average Case : O(n)
    Best Case : O(1)
Space Complexity : O(1)

------------
This is a searching algorithm that iterates over each element to find the key element
If key is found it will return the position
else -1
------------

"""

import sys


class LinearSearch:
    def linear_search(self, array, key):
        for i in range(len(array)):
            if array[i] == key:
                return i
        return -1


if __name__ == "__main__":
    print(
        """
    Input format 
    first line contains space separated elements eg., 9 6 3 4 5 2 7 1
    Second line contains the key to be searched  eg., 7
    """
    )
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    array = data[:-1]
    key = data[-1]
    found = LinearSearch().linear_search(array, key)
    if found == -1:
        print("Key not found")
    else:
        print("Key is found at position : {}".format(found))
