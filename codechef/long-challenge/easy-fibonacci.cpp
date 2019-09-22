/*
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

*/

// Solution

// cook your dish here
#include <iostream>
#include <type_traits>
#include <bitset>
#include <math.h>
using namespace std;

long long get_pisano_period(long long m)
{
    long long a = 0, b = 1, c = a + b;
    for (int i = 0; i < m * m; i++)
    {
        c = (a + b) % m;
        a = b;
        b = c;
        if (a == 0 && b == 1)
            return i + 1;
    }
    return 0;
}

long long get_fibonacci_huge(long long n, long long m)
{
    long long remainder = n % get_pisano_period(m);

    long long first = 0;
    long long second = 1;

    long long res = remainder;

    for (int i = 1; i < remainder; i++)
    {
        res = (first + second) % m;
        first = second;
        second = res;
    }

    return res % m;
}

long long highestPowerof2(long long n)
{
    bitset<128> binary(n);
    long long x = 0;
    for (int i = 127; i >= 0; i--)
    {
        if (binary[i] == 1)
        {
            break;
        }
        x += 1;
    }
    return (long long)(128 - x - 1);
}

int main()
{
    long long T;
    cin >> T;
    string c;
    long long d;
    long long n;
    while (T--)
    {
        long long N;
        cin >> N;
        if (N == 1)
        {
            cout << 0 << '\n';
        }
        else
        {
            if (N % 2 != 0)
            {
                d = highestPowerof2(N - 1);
                n = (long long)(pow(2, d) + 0.5) - 1;
            }
            else
            {
                d = highestPowerof2(N);
                n = (long long)(pow(2, d) + 0.5) - 1;
            }
            cout << get_fibonacci_huge(n, 10) << '\n';
        }
    }
    return 0;
}

// Time : 0.19 s
