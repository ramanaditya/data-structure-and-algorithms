Linked List
============

Floyd's Tortoise and Hare
---------------------------

.. automodule:: LinkedList.floyds_tortoise_and_hare
   :members:
   :private-members:
   :inherited-members:

Description
````````````

Floyd's cycle-finding algorithm is a pointer algorithm that uses only two pointers, which move through the sequence at
different speeds. It is also called the **tortoise and the hare algorithm**

Checking the existence of the cycle in the linked-list. We can also find the node with which linked-list is linked

.. important::
    * Linear TIme
    * Constant Space

.. seealso::
    Reference : `wiki <https://en.wikipedia.org/wiki/Cycle_detection>`__

Python
````````

Check For Cycle
..................

.. code-block:: python

        def check_cycle(self, head):
            """
            Return True is cycle is present else False
            :param head:
            :return:
            """
            # Two pointers
            tortoise, hare = head, head

            # Base Case
            while hare and hare.next:
                tortoise = tortoise.next
                hare = hare.next.next

                # Condition for cycle
                if tortoise == hare:
                    return True

            # Condition when there is no cycle
            return False

Get the Node where cycle exists
.................................

.. code-block:: python

    def cycle_node(self, head):
        """
        Finding the node where cycle exists
        :param head:
        :return:
        """
        # Two pointers
        tortoise, hare = head, head

        while True:
            # Condition when pointer reaches to end
            if not hare or not hare.next:
                return None

            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                break

        # Iterating over the ll to find
        tortoise = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next

        # Returning node where cycle was found
        return tortoise

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

   * - 141
     - :green:`Easy`
     - `Linked List Cycle <https://leetcode.com/problems/linked-list-cycle/>`__
     - `Python <https://github.com/ramanaditya/data-structure-and-algorithms/blob/master/leetcode/array/majority-element.py>`__
     - Two Pointers

   * - 142
     - :orange:`Medium`
     - `Linked List Cycle II <https://leetcode.com/problems/linked-list-cycle-ii/>`__
     - `Python <https://github.com/ramanaditya/data-structure-and-algorithms/tree/master/leetcode/linked-list/linked-list-cycle-ii.py>`__
     - Hash-Table, Two Pointers
