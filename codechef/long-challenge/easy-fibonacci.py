'''
[Easy Fibonacci](https://www.codechef.com/SEPT19B/problems/FIBEASY)

Problem Code: FIBEASY

The Fibonacci sequence F0,F1,… is a special infinite sequence of non-negative integers, where F0=0, F1=1 and for each integer n≥2, Fn=Fn−1+Fn−2.

Consider the sequence D of the last decimal digits of the first N Fibonacci numbers, i.e. D=(F0%10,F1%10,…,FN−1%10). Now, you should perform the following process:

Let D=(D1,D2,…,Dl).
If l=1, the process ends.
Create a new sequence E=(D2,D4,…,D2⌊l/2⌋). In other words, E is the sequence created by removing all odd-indexed elements from D.
Change D to E.
When this process terminates, the sequence D contains only one number. You have to find this number.


Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single integer N.

Output
For each test case, print a single line containing one integer ― the last remaining number.

Constraints
1≤T≤10^5
1≤N≤10^18

Subtasks
Subtask #1 (20 points):

1≤T≤10^5
1≤N≤10^7

Subtask #2 (80 points): original constraints

Example 
Input
    1
    9
Output
    3

Explanation
Example case 1: The first N Fibonacci numbers are (0,1,1,2,3,5,8,13,21). The sequence D is (0,1,1,2,3,5,8,3,1)→(1,2,5,3)→(2,3)→(3).

'''

# Solution

# cook your dish here
import sys
import math
fib_matrix = [[1, 1],
              [1, 0]]


def matrix_square(A, mod):
    return mat_mult(A, A, mod)


def mat_mult(A, B, mod):
  if mod is not None:
    return [[(A[0][0]*B[0][0] + A[0][1]*B[1][0]) % mod, (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % mod],
            [(A[1][0]*B[0][0] + A[1][1]*B[1][0]) % mod, (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % mod]]


def matrix_pow(M, power, mod):
    #Special definition for power=0:
    if power <= 0:
      return M

    # Order is 1,2,4,8,16,...
    powers = list(
        reversed([True if i == "1" else False for i in bin(power)[2:]]))

    matrices = [None for _ in powers]
    matrices[0] = M

    for i in range(1, len(powers)):
        matrices[i] = matrix_square(matrices[i-1], mod)

    result = None

    for matrix, power in zip(matrices, powers):
        if power:
            if result is None:
                result = matrix
            else:
                result = mat_mult(result, matrix, mod)

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = data[0]
    N = data[1:]
    k = 0
    while T > 0:
        if N[k] == 1:
            print(0)
            T -= 1
            k += 1
        else:
            if N[k] % 2 != 0:
                c = bin(N[k] - 1)
                d = int(len(c[2:]) - 1)
                n = 2 ** d - 1
            else:
                c = bin(N[k])
                d = int(len(c[2:]) - 1)
                n = 2 ** d - 1
            print(matrix_pow(fib_matrix, n, 10)[1][0])
            T -= 1
            k += 1


# Time : 2.80 s
# Subtask 2 didn't pass
