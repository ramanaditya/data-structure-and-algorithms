Searching
==========

Linear Search
------------------------------------

.. automodule:: searching.linear_search
   :members:
   :undoc-members:
   :private-members:
   :inherited-members:
   :show-inheritance:

Description
````````````

This is a search algorithm that iterates over each element to find the key element

If key is found it will return the position
else -1

.. important::
   TIme Complexity
     * Worst Case: O(n)
     * Average Case: O(n)
     * Best Case: O(1)

   **Space Complexity**: O(1)


Python
````````

.. code-block:: python

    class LinearSearch:
        def linear_search(self, array, key):
            for i in range(len(array)):
                if array[i] == key:
                    return i
            return -1

Implementation
````````````````
.. role:: green
.. role:: orange
.. role:: red



.. Section for Binary Search


Binary Search
------------------------------------

.. automodule:: searching.binary_search
   :members:
   :undoc-members:
   :private-members:
   :inherited-members:
   :show-inheritance:

Description
````````````

Binary Search is a sorting algorithm in which we select the mid element and compare key to the mid element if key is
smaller then we search before mid else after mid. If key is found we return the index of key else -1.

.. important::
    TIme Complexity
        * Worst Case: O( log(n) )
        * Average Case: O( log(n) )
        * Best Case: O(1)

    **Space Complexity**: O(1)


Python
````````

.. code-block:: python

    class BinarySearch:
        def binary_search(self, array, key):
            low = 0
            high = len(array) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if array[mid] == key:
                    return mid
                elif array[mid] < key:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

Implementation
````````````````
.. role:: green
.. role:: orange
.. role:: red


