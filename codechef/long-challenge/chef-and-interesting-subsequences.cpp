/*
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

*/

// Solution

// cook your dish here
#include <bits/stdc++.h>
#include <iostream>
#include <type_traits>
#include <bitset>
#include <math.h>
using namespace std;
long comb(long n, long r){
    long res = 1;
    if (r > n - r)
        r = n - r;

    for (long i = 0; i < r; i++)
    {
        res *= (n - i);
        res /= (i + 1);
    }
    return res;
}

int main()
{
    long T;
    cin >> T;
    while (T--)
    {
        long N;
        cin >> N;
        long K;
        cin >> K;
        std::vector<long> A(N);
        long min_sum_array[51];
        for (long i = 0; i < N; i++)
        {
            cin >> A[i];
        }
        sort(A.begin(), A.end());
        long max_of_array = A[K-1];
        long count1 = 0;
        for(long i=0;i<K;i++){
            if(A[i] == max_of_array){
                count1 += 1;
            }
        }
        long count2 = 0;
        for(long i=K;i<N;i++){
            if(A[i] == max_of_array){
                count2 += 1;
            }
        }
        cout << comb(count1+count2,count1) << endl;
    }
    return 0;
}

// Time : 0.00 s
