"""
10.1-4
Rewrite ENQUEUE and DEQUEUE to detect underflow and overflow of a queue.
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
