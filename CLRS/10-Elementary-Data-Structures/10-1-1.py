"""
10.1-1
Using Figure 10.1 as a model, illustrate the result of each operation in the sequence PUSH(S,4), PUSH(S,1), PUSH(S,3),
POP(S), PUSH(S,8), and POP(S) on an initially empty stack S stored in array S[1..6􏰀].
"""


def push(S, ele):
    if len(S) >= N:
        print("Overflow")
        return
    S.append(ele)
    return


def pop(S):
    if len(S) <= 0:
        print("Underflow")
        return
    S.pop()
    return


def display(S):
    print("Bottom -> ", end="")
    for i in S:
        print(i, end=" -> ")
    print(" Top")
    return


if __name__ == "__main__":
    S = []
    global N
    N = 6
    display(S)
    push(S, 4)
    display(S)
    push(S, 1)
    display(S)
    push(S, 3)
    display(S)
    pop(S)
    display(S)
    push(S, 8)
    display(S)
    pop(S)
    display(S)

"""
Output :

Bottom ->  Top
Bottom -> 4 ->  Top
Bottom -> 4 -> 1 ->  Top
Bottom -> 4 -> 1 -> 3 ->  Top
Bottom -> 4 -> 1 ->  Top
Bottom -> 4 -> 1 -> 8 ->  Top
Bottom -> 4 -> 1 ->  Top

"""
