Array
======

Boyer–Moore majority vote algorithm
------------------------------------

.. automodule:: Array.boyer_moore_voting_algorithm
   :members:
   :undoc-members:
   :private-members:
   :special-members:
   :inherited-members:
   :show-inheritance:

Description
````````````

To find the majority element from the sequence, majority means the element should be present more than n/2
times the total length, n,  of the sequence.

If no such element occurs, then algorithm can return any arbitrary element, and is not guaranteed that this element
will be the mode or occurred maximum number of times.

.. important::
    * Linear TIme
    * Constant Space

.. seealso::
    Reference : `wiki <https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm>`__

Python
````````

.. code-block:: python

    def boyer_moore_voting_algorithm(arr: list) -> int:
        """
        :param arr: list
        :return: int
        """
        res = arr[0]  # Initialization
        counter = 0  # Counter

        for i in range(len(arr)):
            if counter == 0:
                res = arr[i]
                counter = 1
            elif res == arr[i]:
                counter += 1
            else:
                counter -= 1

        return res

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

   * - 169
     - :green:`Easy`
     - `Majority Element <https://leetcode.com/problems/majority-element/>`__
     - `Python <https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/leetcode/array/majority-element.py>`__
     -
