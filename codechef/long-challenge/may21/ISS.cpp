/*
[An Interesting Sequence](https://www.codechef.com/MAY21C/problems/ISS)

Zanka finds fun in everyday simple things. One fine day he got interested in a very trivial sequence. Given a natural
number k, he considers the sequence Ai=k+i2 so that the terms are

k+1,k+4,k+9,k+16,…
Now to make things more interesting, he considers the gcd of consecutive terms in the sequence, then takes the sum of
the first 2k values. More formally, he wants to compute

∑i=12kgcd(Ai,Ai+1)
Denote this sum by S. Zanka wants you to print the number S for each k.

Input
The first line contains an integer T, the number of test cases. Descriptions of test cases follow.
The only line of each test case contains a single integer k.

Output
For each test case, output a single line containing the sum S for the given k.

Constraints
1≤T≤106
1≤k≤106

Subtasks
Subtask #1 (20 points): t≤103,k≤103
Subtask #2 (80 points): Original Constraints

Sample Input
1
1

Sample output
6

Explanation
The first 2k+1 terms of the sequence A are 2,5,10.
So the answer is gcd(2,5)+gcd(5,10)=1+5=6
*/

#include <bits/stdc++.h>
#include <iostream>
#include <type_traits>
#include <bitset>
#include <math.h>

#define endl "\n"

using namespace std;

typedef long long int ll;

int main(){
    ll T, k, res;
    cin >> T;

    while (T--) {
        cin >> k;
        res = 0;
        for(ll i=1; i< 2*k + 1; i++){
            res += __gcd(k + i * i, k + (i + 1) * (i + 1));
        }
        cout << res << endl;
    }
    return 0;
}

// Partially Correct, Subtask 2: TLE
// Time : 0.11s
