"""
10.1-2
Explain how to implement two stacks in one array A[1..n􏰀] in such a way that neither stack overflows unless the total
number of elements in both stacks together is n. The PUSH and POP operations should run in O(1) time.
"""

N = 10
S = []
S1 = []
S2 = []

S = [-1] * N


class Stack:
    def __init__(self):
        self.top1 = -1
        self.top2 = 10

    def push(self, st, ele):
        if st == "S1":
            if self.top1 + 1 == self.top2:
                print("Overflow for ", ele)
                return
            else:
                self.top1 += 1
                S[self.top1] = ele
                return
        else:
            if self.top2 - 1 == self.top1:
                print("Overflow for ", ele)
                return
            else:
                self.top2 -= 1
                S[self.top2] = ele
                return

    def pop(self, st):
        if st == "S1":
            if self.top1 == -1:
                print("Underflow")
                return
            else:
                S[self.top1] = -1
                self.top1 -= 1
                return
        else:
            if self.top2 == N - 1:
                print("Underflow")
                return
            else:
                S[self.top2] = -1
                self.top2 += 1
                return

    def display(self):
        print("")
        if self.top1 == -1:
            print("Stack 1 is empty", end="")
        else:
            print("S1 Bottom => ", end="")
            for i in range(self.top1 + 1):
                print(S[i], end=" -> ")
            print(" <= S1 top", end="")
        if self.top1 != self.top2:
            for i in range(self.top1 + 1, self.top2):
                print(" - ", end="")
        if self.top2 == 10:
            print("Stack 2 is empty", end="")
        else:
            print("S2 Top => ", end="")
            for i in range(self.top2, N):
                print(S[i], end=" -> ")
            print(" <= S2 Bottom")


if __name__ == "__main__":
    stack = Stack()
    stack.push("S1", 1)
    stack.push("S1", 2)
    stack.push("S1", 3)
    stack.push("S1", 4)
    stack.push("S1", 5)
    stack.push("S1", 6)
    stack.push("S1", 7)
    stack.display()
    stack.push("S2", 8)
    stack.push("S2", 9)
    stack.push("S2", 10)
    stack.push("S2", 11)
    stack.push("S2", 12)
    stack.display()
    stack.pop("S1")
    stack.pop("S1")
    stack.pop("S1")
    stack.pop("S1")
    stack.pop("S1")
    stack.display()
    stack.pop("S2")
    stack.pop("S2")
    stack.display()


"""
Solution:

S1 Bottom => 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 ->  <= S1 top -  -  - Stack 2 is emptyOverflow for  11
Overflow for  12

S1 Bottom => 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 ->  <= S1 topS2 Top => 10 -> 9 -> 8 ->  <= S2 Bottom

S1 Bottom => 1 -> 2 ->  <= S1 top -  -  -  -  - S2 Top => 10 -> 9 -> 8 ->  <= S2 Bottom

S1 Bottom => 1 -> 2 ->  <= S1 top -  -  -  -  -  -  - S2 Top => 8 ->  <= S2 Bottom

"""
