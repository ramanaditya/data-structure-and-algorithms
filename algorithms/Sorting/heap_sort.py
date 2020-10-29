""""""
"""
Heap Sort:
Runtime:
    Worst: O(n log(n) )
    Average: O(n log(n) )
    Best: O(n log(n) )
Memory: O(1)
In place Sorting
"""

import sys
import math

class HeapSort:

    def heap_sort(self, data):
        hs = len(data)
        self.build_max_heap(data, hs)
        for i in range(len(data) - 1, 0, -1):
            data[0], data[i] = data[i], data[0]
            hs -= 1
            self.max_heapify(data, 0, hs)

    def build_max_heap(self, data, hs):
        for i in range(int(len(data)/2) - 1, -1, -1):
            self.max_heapify(data, i, hs)

    def max_heapify(self, data, i, hs):
        l = self.left(i)
        r = self.right(i)
        if ((l + 1) <= hs) and (data[l] > data[i]):
            largest = l
        else:
            largest = i
        if ((r + 1) <= hs) and (data[r] > data[largest]):
            largest = r
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            self.max_heapify(data, largest, hs)

    def left(self, i):
        return (2*i) + 1
    
    def right(self, i):
        return (2*i) + 2


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    HeapSort().heap_sort(data)
    print(data)