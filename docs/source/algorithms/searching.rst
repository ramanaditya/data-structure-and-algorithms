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

Binary Search is a sorting algorithm, applied on sorted array in which we select the mid element and compare key to the mid element if key is
smaller then we search before mid else after mid.

If key is found we return the index of key else -1.

.. tip::
    Finding problems associated with Binary Search
        * list/array is sorted
        * Have to find element within the sorted list
        * Can be used in case of binary values as well eg., [0,0,0,1,1,1,1]

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

.. list-table:: LeetCode
   :header-rows: 1
   :widths: 5, 5, 15, 15, 10

   * - Sl No
     - Level
     - Questions
     - Solutions
     - Tags

   * - 704
     - :green:`Easy`
     - `Binary Search <https://leetcode.com/problems/binary-search/>`__
     - `Python <https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/leetcode/binary-search/binary-search.py>`__
     -

   * - 367
     - :green:`Easy`
     - `Valid Perfect Square <https://leetcode.com/problems/valid-perfect-square/>`__
     - `Python <https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/leetcode/binary-search/valid-perfect-square.py>`__
     -

   * - 278
     - :green:`Easy`
     - `First Bad Version <https://leetcode.com/problems/first-bad-version/>`__
     - `Python <https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/leetcode/binary-search/first-bad-version.py>`__
     -

   * - 74
     - :orange:`Medium`
     - `Search a 2D Matrix <https://leetcode.com/problems/search-a-2d-matrix/>`__
     - `Python <https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/leetcode/binary-search/search-a-2d-matrix.py>`__
     -
