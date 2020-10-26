""""""
"""
# Floyd's Tortoise and Hare
[Reference : wiki](https://en.wikipedia.org/wiki/Cycle_detection)

## Description 
Floyd's cycle-finding algorithm is a pointer algorithm that uses only two pointers, which move through the sequence at 
different speeds. It is also called the "tortoise and the hare algorithm"

Checking the existence of the cycle in the linked-list. We can also find the node with which linked-list is linked

Linear TIme
Constant Space
"""


class Node:
    """
    Node for the linked-list
    """

    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class FloydTortoiseAndHare:
    """
    Implementation of Floyd's Tortoise and Hare Algorithm
    """

    def check_cycle(self, head):
        """
        Return True if cycle is present else False
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


class FormLinkedList:
    """
    Class to form linked-list with cycle
    """

    def __init__(self, array, ind):
        """
        Initialization
        :param array: array of data of linked list
        :param ind: Tail linked to the index ind,
            if no cycle, then ind = -1
        """
        self.head = None
        self.array = array
        self.ind = ind

    def createll(self):
        """
        Function to create linked-list with cycle
        :return:
        """
        node_at_cycle = None
        self.head = temp = Node(None)

        for index, ele in enumerate(self.array):
            new_node = Node(ele)
            temp.next = new_node

            # Keeping track of the node where tail will be linked
            if index == self.ind:
                node_at_cycle = temp

            temp = temp.next

        # linking tail to the node of given index
        temp.next = node_at_cycle

        return self.head.next


if __name__ == "__main__":
    print(f"Enter space separated integers")
    array = list(map(int, input().split()))
    print(f"Enter the index where tail is linked")
    ind = int(input())

    formll = FormLinkedList(array, ind)
    head = formll.createll()

    floyd = FloydTortoiseAndHare()
    cycle = floyd.check_cycle(head)
    print(f"Cycle is {'' if cycle else 'not '}present")

    if cycle:
        node = floyd.cycle_node(head)
        print(f"Tail connects to node {node.data}")


"""
### Implementation
| Problem No. | Level | Problems | Solutions |
| :--- | :---: | :--- | :---|
| 141. | Easy | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | [Python](https://github.com/ramanaditya/data-structure-and-algorithms/tree/master/leetcode/linked-list/linked-list-cycle.py) |
| 142. | Medium | [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | [Python](https://github.com/ramanaditya/data-structure-and-algorithms/tree/master/leetcode/linked-list/linked-list-cycle-ii.py) |
 
"""
