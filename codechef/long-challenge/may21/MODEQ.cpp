/*
[Modular Equation](https://www.codechef.com/MAY21C/problems/MODEQ)

Given integers N and M, find the number of ordered pairs (a,b)
such that 1≤a<b≤N and ((M mod a) mod b)=((M mod b) mod a).

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
The only line of each test case contains two integers N, M.

Output
For each testcase, output in a single line the answer to the problem.

Constraints
1≤T≤1000
2≤N≤106
1≤M≤5⋅105
The sum of N over all test cases does not exceed 106.
Note: Multiplier for JAVA for this problem is reduced to 1.25 instead of usual 2.

Subtasks
Subtask #1 (10 points):
1≤T≤10
2≤N≤103
1≤M≤105

Subtask #2 (40 points):
1≤T≤100
2≤N≤105
1≤M≤105
The sum of N over all test cases does not exceed 106.
Subtask #3 (50 points): Original Constraints

Sample Input
3
3 5
3 6
3 10

Sample Output
2
3
2

Explanation
Test Case 1: The valid pairs are {(1,2),(1,3)}.

Test Case 2: The valid pairs are {(1,2),(1,3),(2,3)}.

Test Case 3: The valid pairs are {(1,2),(1,3)}.
*/


#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long int T;
    cin >> T;
    while(T--) {
        long long int M, N;
        cin >> N >> M;
        long long int res=0;
        vector<long long> mod(N+1,1);
        for (long long int i = 2; i <= N; i++){
            long long int mod_val = M % i;
            res += mod[mod_val];
            for(long long int j = mod_val; j <= N; j += i){
                mod[j]++;
            }
        }

        cout << res << endl;
    }

    return 0;
}

// Time: 0.04s