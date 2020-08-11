Linked List
============

.. important::
   A linked-list is a sequential list of nodes that hold data which point to other nodes also containing data


Where are they used
--------------------

* Used in many list, queue & stack implementation
* For creating Circular List
* Used in separate chaining, which is present certain hashtable implementations to deal with hashing collisions
* Often used in the implementation of the adjacency lists for graph

Pros and Cons
--------------

+--------------------+------------------------------+---------------------------------------+
|                    |             Pros             |                 Cons                  |
+====================+==============================+=======================================+
| Singly Linked List | * Uses Less Memory           | Can't easily access previous elements |
|                    | * Simpler Implementation     |                                       |
+--------------------+------------------------------+---------------------------------------+
| Doubly Linked List | Can be Traversed backwards   | Takes 2x memory                       |
+--------------------+------------------------------+---------------------------------------+

Complexity
-----------


+----------------------+-----------------------+----------------------+
|                      | Singly Linked List    | Doubly Linked List   |
+======================+=======================+======================+
| Search               |         O(n)          |         O(n)         |
+----------------------+-----------------------+----------------------+
| Insert at Head       |         O(1)          |         O(1)         |
+----------------------+-----------------------+----------------------+
| Insert at Tail       |         O(1)          |         O(1)         |
+----------------------+-----------------------+----------------------+
| Remove at Head       |         O(1)          |         O(1)         |
+----------------------+-----------------------+----------------------+
| Remove at Tail       |         O(n)          |         O(1)         |
+----------------------+-----------------------+----------------------+
| Remove in middle     |         O(n)          |         O(n)         |
+----------------------+-----------------------+----------------------+

.. automodule:: LinkedList.singlyll
   :members:
   :private-members:
   :inherited-members:
   :show-inheritance:


Node
-----

Defining the node for a Linked List
````````````````````````````````````

.. py:function:: Node(data: int)

.. code-block:: python

    def Node(data):
        data = data
        next = None

.. code-block:: python

    head = None

Search
-------

.. py:function:: search(data: int)

.. code-block:: python

    def search(data):
        """
        To search the given data in the Linked list and find it's first occurrence,
        if it is not present return -1
        """
        curr = head
        index = 0
        while curr:
            if curr.data == data:
                return index
            index += 1
            curr = curr.next
        return -1

Insert
-------

Insert at head
````````````````

.. py:function:: insert_at_head(data: int)

.. code-block:: python

    def insert_at_head(data):
        """Insert at head """
        new_node = Node(data)
        new_node.next = head
        head = new_node

Insert at Tail
````````````````

.. py:function:: insert_at_tail(data: int)

.. code-block:: python

    def insert_at_tail(data):
        """Insert at the tail"""
        new_node = Node(data)
        # If there is no element in the linked list then add it to the head
        if head is None:
            head = new_node
        else:
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = new_node

Insert at an Index
````````````````````

.. py:function:: insert_at_index(data: int)

.. code-block:: python

    def insert_at_index(data):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked
        list, the node will be appended to the end of linked list. If index is greater than the length, the node will
        not be inserted.
        """
        index -= 1
        new_node = Node(val)
        if not head:
            head = new_node
            return
        curr = head
        if index < 1:
            new_node.next = head
            head = new_node
            return
        else:
            count = 0
            prev = head
            while curr:
                count += 1
                if count == index:
                    new_node.next = curr.next
                    curr.next = new_node
                    return
                prev = curr
                curr = curr.next
            if count == index:
                curr.next = new_node
                return
            else:
                prev.next = new_node
                return

Delete
-------

Delete at head
```````````````

.. py:function:: delete_head()

.. code-block:: python

    def delete_head():
        if not head:
            return -1
        else:
            value = head.data
            temp = head.next
            head = None
            head = temp
            return value


Delete at Tail
```````````````

.. py:function:: delete_tail()

.. code-block:: python

    def delete_tail():
        if not head:
            return -1
        else:
            curr = head
            if not curr.next:
                value = curr.data
                head = None
                return value
            while curr.next.next:
                curr = curr.next
            value = curr.next.data
            curr.next = None
            return value

Delete at Index
````````````````

.. py:function:: delete_at_index(index: int)

.. code-block:: python

    def delete_at_index(index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        index -= 1
        if head is None:
            return -1
        curr = head
        if index == 0:
            value = curr.data
            head = curr.next
            return value
        elif index < 0:
            return -1
        else:
            for i in range(index - 1):
                curr = curr.next
                if curr is None:
                    break
            if curr is None:
                return -1
            if curr.next is None:
                return -1
        value = curr.data
        next = curr.next.next
        curr.next = None
        curr.next = next
        return value

Important Problems
-------------------

.. role:: green
.. role:: orange
.. role:: red

Leetcode Problems
```````````````````

.. list-table:: Linked List Cycle
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
     - `Python <https://github.com/ramanaditya/data-structure-and-algorithms/tree/master/leetcode/linked-list/linked-list-cycle.py>`__
     - Two Pointers

   * - 142
     - :orange:`Medium`
     - `Linked List Cycle II <https://leetcode.com/problems/linked-list-cycle-ii/>`__
     - `Python <https://github.com/ramanaditya/data-structure-and-algorithms/tree/master/leetcode/linked-list/linked-list-cycle-ii.py>`__
     - Hash Table
