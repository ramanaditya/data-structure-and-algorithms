class Heap:
    def PARENT(self, i):
        return (i - 1) >> 1

    def LEFT(self, i):
        return (i << 1) + 1

    def RIGHT(self, i):
        return (i << 1) + 2

    def insert(self, arr, ele):
        arr.append(ele)
        for i in range((len(arr) // 2) - 1, -1, -1):
            self.max_heapify(arr, i)

        return arr

    def delete(self, arr, ele):
        index = arr.index(ele)
        arr[index], arr[-1] = arr[-1], arr[index]
        arr.pop()
        for i in range((len(arr) // 2) - 1, -1, -1):
            self.max_heapify(arr, i)
        return arr

    def build_max_heap(self, arr):
        for i in range((len(arr) // 2) - 1, -1, -1):
            self.max_heapify(arr, i)
        return arr

    def max_heapify(self, arr, ind):
        largest = self.PARENT(ind)
        l = self.LEFT(ind)
        r = self.RIGHT(ind)
        if l < len(arr) and arr[l] > arr[ind]:
            largest = l
        else:
            largest = ind
        if r < len(arr) and arr[r] > arr[largest]:
            largest = r
        if largest != ind:
            arr[ind], arr[largest] = arr[largest], arr[ind]
            self.max_heapify(arr, largest)


if __name__ == "__main__":
    heap = Heap()
    max_heap = []
    array = []
    while True:
        print(
            "1. Insert Array\n2. Insert Element\n3. Delete Element\n4. Print Max Heap"
        )
        choice = int(input())
        if choice == 1:
            print("Enter the array")
            array.extend(list(map(int, input().split())))
            max_heap = heap.build_max_heap(array)
        if choice == 2:
            print("Enter the element")
            ele = int(input())
            max_heap = heap.insert(array, ele)
        if choice == 3:
            print("Enter the element to be deleted")
            ele = int(input())
            max_heap = heap.delete(array, ele)
        if choice == 4:
            print(max_heap)
