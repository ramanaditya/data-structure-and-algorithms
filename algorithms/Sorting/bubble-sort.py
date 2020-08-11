"""
Bubble Sort:
Runtime:
    Worst: O(n^2)
    Average: O(n^2)
    Best: O(n)
Memory: O(1)
"""
import sys


class bubbleSort:
    def bubble_sort(self, data):
        for i in range(len(data) - 1):
            for j in range(0, len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        print(data)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    bubbleSort().bubble_sort(data)
