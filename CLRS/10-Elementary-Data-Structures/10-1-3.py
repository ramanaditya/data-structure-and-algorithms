"""
10.1-3
Using Figure 10.2 as a model, illustrate the result of each operation in the sequence ENQUEUE(Q,4), ENQUEUE(Q,1),
ENQUEUE(Q,3), DEQUEUE(Q), ENQUEUE(Q,8), and DEQUEUE(Q) on an initially empty queue Q stored in array Q[1..6]􏰀.
"""


class Queue:
    def __init__(self, N):
        self.N = N

    def enqueue(self, Q, ele):
        if len(Q) == self.N:
            print("Queue Overflow")
            return
        Q.append(ele)

    def dequeue(self, Q):
        try:
            Q.pop(0)
        except IndexError:
            print("Queue is empty")

    def display(self, Q):
        print(Q)


if __name__ == "__main__":
    Q = []
    N = 6
    q = Queue(N)
    q.enqueue(Q, 4)
    q.enqueue(Q, 1)
    q.enqueue(Q, 3)
    q.display(Q)
    q.dequeue(Q)
    q.display(Q)
    q.enqueue(Q, 8)
    q.dequeue(Q)
    q.display(Q)

"""
Solution :

[4, 1, 3]
[1, 3]
[3, 8]

"""
