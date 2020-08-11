"""
Insertion Sort:
Runtime:
    Worst: O(n^2)
    Average: O(n^2)
    Best: O(n)
Memory: O(1)

It takes maximum time if list is sorted in reverse order and minimum when list is sorted
"""
import sys


class insertionSort:
    def insertion_sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        print(data)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    insertionSort().insertion_sort(data)
