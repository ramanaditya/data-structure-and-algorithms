Stack
======

.. important::
    Stack is a data structure where we store data with the rule **Last In First Out (LIFO)**.

    * Used in recursion.
    * Valid Parenthesis.


.. warning::
    In python stack is implemented using list, the stack class here is just to tell about the implementation.


Complexity
-----------

+---------------+---------------+
|               | Time          |
+===============+===============+
| Insertion     | O(1)          |
+---------------+---------------+
| Deletion      | O(1)          |
+---------------+---------------+

Stack Operations
------------------

.. automodule:: stack.stack
   :members:
   :undoc-members:
   :private-members:
   :inherited-members:
   :show-inheritance:

.. code-block:: python

    class Stack:
        def __init__(self, size):
            self.stack = []
            self.size = size
            self.top = -1

        def push(self, ele) -> None:
            if not self.overflow():
                self.top += 1
                self.stack[self.top] = ele
            else:
                print("Stack Overflow")

        def pop(self) -> int:
            if not self.underflow():
                self.top -= 1
                return self.stack.pop()
            else:
                print("Stack Underflow")
                return -1

        def underflow(self) -> bool:
            if len(self.stack) == 0:
                return True
            return False

        def overflow(self):
            if len(self.stack) == self.size:
                return True
            return False


Important Problems
-------------------

.. role:: green
.. role:: orange
.. role:: red
