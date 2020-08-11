"""
Merge Sort:
Runtime:
    Worst: O(n log(n) )
    Average: O(n log(n) )
    Best: O(n log(n) )
Memory: O(1)

In place Sorting
"""
import sys


class MergeSort:
    def merge_sort(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left = data[:mid]
            right = data[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                data[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                data[k] = right[j]
                j += 1
                k += 1


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    MergeSort().merge_sort(data)
    print(data)
