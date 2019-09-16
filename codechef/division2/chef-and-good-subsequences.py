'''
[Chef and Interesting Subsequences ](https://www.codechef.com/SEPT19B/problems/CHEFINSQ)

Problem Code: CHEFINSQ

Chef has a sequence A1,A2,…,AN. This sequence has exactly 2N subsequences. Chef considers a subsequence of A interesting if its size is exactly K and the sum of all its elements is minimum possible, i.e. there is no subsequence with size K which has a smaller sum.

Help Chef find the number of interesting subsequences of the sequence A.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains N space-separated integers A1,A2,…,AN.The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and K.
The second line contains N space-separated integers A1,A2,…,AN.

Output
For each test case, print a single line containing one integer ― the number of interesting subsequences.

Constraints
1 ≤ T ≤ 10
1 ≤ K ≤ N ≤ 50
1 ≤ Ai ≤ 100 for each valid i

Subtasks
Subtask #1 (30 points):

1≤N≤20

Subtask #2 (70 points): original constraints

Example 
Input
    1
    4 2
    1 2 3 4
Output
    1

Explanation
Example case 1: There are six subsequences with length 2: (1,2), (1,3), (1,4), (2,3), (2,4) and (3,4). The minimum sum is 3 and the only subsequence with this sum is (1,2).

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
