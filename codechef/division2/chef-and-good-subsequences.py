'''
[Chef and Good Subsequences](https://www.codechef.com/SEPT19B/problems/GDSUB)

Problem Code: GDSUB

Chef is given a sequence of prime numbers A1,A2,…,AN. This sequence has exactly 2N subsequences. A subsequence of A is good if it does not contain any two identical numbers; in particular, the empty sequence is good.

Chef has to find the number of good subsequences which contain at most K numbers. Since he does not know much about subsequences, help him find the answer. This number could be very large, so compute it modulo 1,000,000,007.

Input
The first line of the input contains two space-separated integers N and K.
The second line contains N space-separated integers A1,A2,…,AN.

Output
Print a single line containing one integer ― the number of good subsequences with size at most K, modulo 1,000,000,007.

Constraints
1≤K≤N≤10^5
2≤Ai≤8,000 for each valid i

Subtasks
Subtask #1 (40 points): A1,A2,…,AN are pairwise distinct

Subtask #2 (60 points): original constraints

Example 
Input
    5 3
    2 2 3 3 5
Output
    18

Explanation
There is 1 good subsequence with length 0, 5 good subsequences with length 1, 8 good subsequences with length 2 and 4 good subsequences with length 3.

'''

# Solution

# cook your dish here
import sys
import math
from itertools import combinations

if __name__ == '__main__':
    N, K = map(int, input().split())
    A =[]
    A = list(map(int, input().split()))
    k = 0
    sum = 0
    while k <= K:
        for item in combinations(A, k):
            if len(list(item)) == len(set(item)):
                print(item)
                sum+=1 
        k += 1
    print(sum)

# Time : 0.9 s
#  TLE
