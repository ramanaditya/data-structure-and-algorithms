"""
[Isolation Centers](https://www.codechef.com/MAY20B/problems/CORUS)
As a health expert, Vinay is keeping a close watch on the ongoing pandemic of coronavirus disease (COVID-19). He
thought of a different situation where there are 26 types of viruses, named "aorona", "borona", "corona", …, "zorona".

You are given a string S with length N. There are N people (numbered 1 through N) and for each valid i, the i-th person
is infected by exactly one type of virus named Siorona (i.e. "corona" with the first letter replaced by the i-th
character of S).

You should answer Q queries. In each query:

You are given an integer C denoting the number of available isolation centers.
Each isolation center has an infinite capacity, but with the restriction that two people infected with the same type of
virus cannot stay in the same isolation center.
There is also a pending queue with an infinite capacity and there are no restrictions on which people can be in the
pending queue.
Initially, the isolation centers and pending queue are empty.
Each of the N people should be placed in either the pending queue or one of the isolation centers.
Since Vinay is busy finding a vaccine, he asks Swapnil to find a way to place the people in the pending queue and
isolation centers such that the number of people in the pending queue is the smallest possible.
Help Swapnil find the size of the pending queue in that case.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test
cases follows.
The first line of each test case contains two space-separated integers N and Q.
The second line contains a single string S.
Each of the following Q lines contains a single integer C describing a query.

Output
For each query, print a single line containing one integer ― the minimum size of the pending queue.

Constraints
1≤T,N,Q≤105
0≤C≤109
|S|=N
S contains only lowercase English letters
the sum of N over all test cases does not exceed 105
the sum of Q over all test cases does not exceed 105
Subtasks
Subtask #1 (20 points): T,N,Q,C≤10
Subtask #2 (80 points): original constraints

Example Input
1
20 2
stayinghomesaveslife
1
3

Example Output
6
0

Explanation
Example case 1: In the pending queue for the first query, there should be 2 people with "eorona", 2 with "sorona",
1 with "aorona" and 1 with "iorona".
"""

from collections import Counter

if __name__ == "__main__":
    T = int(input())
    while T:
        N, Q = list(map(int, input().split()))
        S = input()
        d = Counter(S)
        while Q:
            C = int(input())
            count = 0
            for k, v in d.items():
                if d[k] > C:
                    count += d[k] - C
            print(count)
            Q -= 1
        T -= 1
