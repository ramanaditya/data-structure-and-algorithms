Stack
======

.. important::
    Stack is a data structure where we store data with the rule Last In First Out (LIFO).

Complexity
-----------

+---------------+---------------+
|               | Time          |
+===============+===============+
| Insertion     | O(1)          |
+---------------+---------------+
| Deletion      | O(1)          |
+---------------+---------------+

Array Operations
------------------

.. automodule:: Array.Array
   :members:
   :undoc-members:
   :private-members:
   :inherited-members:
   :show-inheritance:

.. code-block:: python

    class array_operation:
    """All the operations associated with Array"""

        def __init__(self):
            self.array = []

        def get(self, index):
            if index < len(self.array):
                return self.array[index]
            return -1

        def insert_at_end(self, ele):
            self.array.append(ele)
            return

        def insert_at_index(self, ele, index):
            self.array.insert(index, ele)
            return

        def delete_at_end(self):
            if len(self.array) > 0:
                return self.array.pop()
            return -1

        def delete_ele(self, ele):
            res = self.search(ele)
            if res == -1:
                return res
            self.array.remove(ele)
            return res

        def delete_at_index(self, index):
            if index < len(self.array):
                return self.array.pop(index)
            return -1

        def search(self, key):
            for i in range(len(self.array)):
                if self.array[i] == key:
                    return i
            return -1

        def display(self):
            for i in range(len(self.array)):
                print("{0} ".format(self.array[i]), end=" ")
            print()


Important Problems
-------------------

.. role:: green
.. role:: orange
.. role:: red
