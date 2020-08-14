""""""
"""
Selection Sort:
Runtime:
    Worst: O(n^2)
    Average: O(n^2)
    Best: O(n^2)
Memory: O(1)
"""


import sys


class selectionSort:
    def selection_sort(self, data):
        for i in range(len(data)):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[min_index] > data[j]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        print(data)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    selectionSort().selection_sort(data)
