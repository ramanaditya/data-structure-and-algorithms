# cook your dish here
import sys
import math

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = data[0]
    i = 1
    while T > 0:
        N,K = data[i:i+2]
        if K < N:
            print(-1)
        elif K == N:
            print(2)
        T -= 1
        i += 2
