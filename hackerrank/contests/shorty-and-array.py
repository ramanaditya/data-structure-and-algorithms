"""
[Shorty and Array](https://www.hackerrank.com/contests/mentorshipkarona-webinar-by-vinit-shahdeo/challenges/shorty-and-array)

Vinit keeps irritating Shreya by calling her Chhotu. As she is already irritated being inside home since one month due
to COVID-19 lockdown, one day he decided that he will stop calling her Chhotu if she would be able to find the number
which is present odd number of times in a given array of numbers of size (2*n+1). It is guaranteed that only one such
number exists.

Can you help Shreya in finding the number which is present odd number of times?

Input Format
First line contains value of n.
Second line contains (2*n+1) array elements.

Constraints
1≤ n ≤ 105
1≤ a[i] ≤ 109

Output Format
Print the required number.

Sample Input 0
2
1 2 3 2 1

Sample Output 0
3

Sample Input 1
3
1 2 2 1 3 6 3

Sample Output 1
6
"""


n = int(input())
a = list(map(int, input().split()))
odd = a[0]
for i in range(1, (2 * n) + 1):
    odd = odd ^ a[i]
print(odd)
