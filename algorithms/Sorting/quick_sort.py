""""""
"""
Quick Sort:
Runtime:
    Worst: O(n^2 )
    Average: O(n log(n) )
    Best: O(n log(n) )
Memory: O( log(n) )

In place Sorting
Unstable
"""

import sys


class QuickSort:
    def partition(self, data, low, high):
        pivot = data[high]
        i = low  # To keep the index of element smaller than pivot
        j = low  # To keep the index of element greater than pivot

        while j < high:
            if data[j] < pivot:
                data[j], data[i] = data[i], data[j]
                i += 1
            j += 1

        data[i], data[high] = data[high], data[i]

        print("pivot", pivot, end=" -> ")
        print(data)

        return i

    def quick_sort(self, data, low, high):
        if low < high:
            pivot = self.partition(data, low, high)
            self.quick_sort(data, low, pivot - 1)
            self.quick_sort(data, pivot + 1, high)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    low = 0
    high = len(data) - 1
    print("Input array is : ", data)
    QuickSort().quick_sort(data, low, high)
    print("Sorted Array is : ", data)
