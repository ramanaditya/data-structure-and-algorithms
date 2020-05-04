"""
[Vinit and his Special Number](https://www.hackerrank.com/contests/mentorshipkarona-webinar-by-vinit-shahdeo/challenges/vinit-and-his-special-number)

Vinit is a coach at Rails Girls Summer Of Code. He is very fond of numbers. Recently he has coined a term for numbers :
Special Number.

According to him, a number is known as special number if its binary representation contains atleast two consecutive 1's
or set bits. For example 7 with binary representation 111 is a special bit number. Similarly 3(11) is also a special
bit number as it contains atleast two consecutive set bits or ones.

Now the problem is, You are given an Array of N integers and Q queries. Each query is defined by two integers L, R .
You have to output the count of special bit numbers in the range L to R.

Input Format
First line contains integer N, no of Array elements and Q - Total Number of Queries.

Next line contains N integers A[i] defining Array elements.

Next Q lines contains Queries of the type 1<=L<=R<=N.

Constraints
0<=A[i]<=109
1<=N<=105
1<=Q<=105

Output Format
Output Q lines containing answer for the ith Query.

Sample Input 0
5 3
3 5 1 12 7
1 3
2 3
1 5
Sample Output 0
1
0
3
"""

N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))
d = dict()
for i in range(N):
    if "11" in bin(A[i])[2:]:
        d[A[i]] = True
    else:
        d[A[i]] = False
while Q:
    L, R = list(map(int, input().split()))
    count = 0
    for i in range(L - 1, R):
        if d[A[i]] == True:
            count += 1
    print(count)

    Q -= 1
