Array
======

Static Array
-------------

.. important::
    A static array is a fixed length container containing n elements indexable from the range [0 , n-1]

Complexity
-----------

+---------------+---------------+---------------+
|               | Static Array  | Dynamic Array |
+===============+===============+===============+
| Access        | O(1)          | O(1)          |
+---------------+---------------+---------------+
| Search        | O(n)          | O(n)          |
+---------------+---------------+---------------+
| Insertion     | NA            | O(n)          |
+---------------+---------------+---------------+
| Appending     | NA            | O(1)          |
+---------------+---------------+---------------+
| Deletion      | NA            | O(n)          |
+---------------+---------------+---------------+

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
