"""
Bubble Sort:
Runtime:
    Worst: O(n^2)
    Average: O(n^2)
Memory: O(1)
"""
import sys


class bubbleSort:
    def bubble_sort(self, data):
        for i in range(len(data)):
            for j in range(i + 1, len(data) - 1):
                if data[j] < data[i]:
                    data[j], data[i] = data[i], data[j]
        print(data)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    bubbleSort().bubble_sort(data)
