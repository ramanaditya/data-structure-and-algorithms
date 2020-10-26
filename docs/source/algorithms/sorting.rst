Sorting
==========

..  list-table:: Sorting Algorithms
    :widths: 5, 20, 15, 15, 15, 15, 15
    :header-rows: 1
    :stub-columns: 2
    :align: center

    *   - Sl No.
        - Algorithm
        - Worst Time
        - Average Time
        - Best Time
        - Memory
        - Stability
    *   - 1
        - Bubble Sort
        - .. math:: n^2
        - .. math:: n^2
        - .. math:: n
        - .. math:: 1
        - Stable
    *   - 2
        - Selection Sort
        - .. math:: n^2
        - .. math:: n^2
        - .. math:: n^2
        - .. math:: 1
        - Unstable
    *   - 3
        - Insertion Sort
        - .. math:: n^2
        - .. math:: n^2
        - .. math:: n^2
        - .. math:: 1
        - Stable
    *   - 4
        - Merge Sort
        - .. math:: n * log(n)
        - .. math:: n * log(n)
        - .. math:: n * log(n)
        - .. math:: n
        - Stable
    *   - 5
        - Quick Sort
        - .. math:: n * log(n)
        - .. math:: n * log(n)
        - .. math:: n^2
        - .. math:: n * log(n)
        - Unstable

.. note::
    * **Stable** : Relative position of equal elements after sorting remains same.
    * **In-place Sorting** : Sorting Input elements without having backup, thus unsorted form is lost.

.. Section for Bubble Sort

Bubble Sort
------------------------------------

.. automodule:: Sorting.bubble_sort
   :members:
   :undoc-members:
   :private-members:
   :inherited-members:
   :show-inheritance:

Description
````````````


.. important::
    TIme Complexity
        * Worst Case: :math:`n^2`
        * Average Case: :math:`n^2`
        * Best Case: :math:`n`

    | **Space Complexity**: :math:`O(1)`
    | **In Place Sorting**
    | **Stable Sorting**


Python
````````

.. code-block:: python

    def bubble_sort(data):
        for i in range(len(data) - 1):
            for j in range(0, len(data) - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

Implementation
````````````````
.. role:: green
.. role:: orange
.. role:: red



.. Section for Selection Sort

Selection Sort
------------------------------------
.. automodule:: Sorting.selection_sort
   :members:
   :undoc-members:
   :private-members:
   :inherited-members:
   :show-inheritance:


Description
````````````


..  important::
    TIme Complexity
        * Worst Case: :math:`n^2`
        * Average Case: :math:`n^2`
        * Best Case: :math:`n^2`

    | **Space Complexity**: :math:`O(1)`
    | **In Place Sorting**
    | **Unstable Sorting**


Python
````````

.. code-block:: python

    def selection_sort(data):
        for i in range(len(data)):
            min_index = i
            for j in range(i + 1, len(data)):
                if data[min_index] > data[j]:
                    min_index = j
            data[i], data[min_index] = data[min_index], data[i]
        return data

Implementation
````````````````

.. Section for Insertion Sort

Insertion Sort
------------------------------------
.. automodule:: Sorting.insertion_sort
   :members:
   :undoc-members:
   :private-members:
   :inherited-members:
   :show-inheritance:


Description
````````````

..  tip::
        * Insertion sort is used when number of elements is small.
        * It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.

..  important::
    TIme Complexity
        * Worst Case: :math:`n^2`
        * Average Case: :math:`n^2`
        * Best Case: :math:`n^2`

    | **Space Complexity**: :math:`O(1)`
    | **In Place Sorting**
    | **Stable Sorting**

Python
````````

.. code-block:: python

    def insertion_sort(data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

Implementation
````````````````

.. Section for Merge Sort

Merge Sort
------------------------------------
.. automodule:: Sorting.merge_sort
   :members:
   :undoc-members:
   :private-members:
   :inherited-members:
   :show-inheritance:


Description
````````````


..  important::
    TIme Complexity
        * Worst Case: :math:`n * log(n)`
        * Average Case: :math:`n * log(n)`
        * Best Case: :math:`n * log(n)`

    | **Space Complexity**: :math:`O(n)`
    | **In Place Sorting**
    | **Stable Sorting**

Python
````````

.. code-block:: python

    def merge_sort(data):
        if len(data) > 1:
            mid = len(data) // 2
            left = data[:mid]
            right = data[mid:]

            merge_sort(left)
            merge_sort(right)

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


Implementation
````````````````

.. Section for Quick Sort

Quick Sort
------------------------------------
.. automodule:: Sorting.quick_sort
   :members:
   :undoc-members:
   :private-members:
   :inherited-members:
   :show-inheritance:


Description
````````````


..  important::
    TIme Complexity
        * Worst Case: :math:`n * log(n)`
        * Average Case: :math:`n * log(n)`
        * Best Case: :math:`n^2`

    | **Space Complexity**: :math:`O(n * log(n))`
    | **In Place Sorting**
    | **Unstable Sorting**

Python
````````

Algorithm for partition
''''''''''''''''''''''''

.. code-block:: python

    def partition(data, low, high):
        pivot = data[high]
        i = low  # To keep the index of element smaller than pivot
        j = low  # To keep the index of element greater than pivot

        while j < high:
            if data[j] < pivot:
                data[j], data[i] = data[i], data[j]
                i += 1
            j += 1

        data[i], data[high] = data[high], data[i]

        return i

Recursive Algorithm for quicksort
'''''''''''''''''''''''''''''''''''

.. code-block:: python

    def quick_sort(data, low, high):
        if low < high:
            pivot = partition(data, low, high)
            quick_sort(data, low, pivot - 1)
            quick_sort(data, pivot + 1, high)

Implementation
````````````````


