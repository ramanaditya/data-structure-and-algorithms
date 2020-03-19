import sys


class LinearSearch:
    def linear_search(self, array, key):
        print(array)
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
        print("Unable to find key")
    else:
        print("Key is found at position : {}".format(found))
