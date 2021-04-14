"""
[World Record](https://www.codechef.com/APRIL21C/problems/BOLT)

"Usain Bolt makes a new world record completing 100 m in 9.58 seconds".

This news headline has been echoing in Chef's mind since 2009 when he started his career in sprinting. This time in the
2021 Tokyo Olympics he is determined to make a new world record.

There are mainly 3 important factors that result in the variation in speed during practice and during competition.

The first factor is a difference in track material which results in variation in the speed at competition with respect
to practice by a factor of k1.

The second factor is wind speed which results in variation in the speed at competition with respect to practice by a
factor of k2.

The final factor is the maximum speed achieved during practice. If the maximum speed during practice is v m/s then in
competition it will be k3∗v m/s.

Given Chef's max speed v during practice and the factors k1,k2,k3, find whether he will be able to create a new world
record, i.e, can he complete 100 m in less than 9.58 seconds?

Note: The final time displayed by the Olympics clock is showing after rounding the original time to 2 places of decimal
and is the only measure of runners performance.

Input:
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, four integers k1,k2,k3,v.

Output:
Output in a single line, the answer, which should be "YES" if it's possible for Chef to create a new world record and
"NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and
"YES" will all be treated as identical).

Constraints
1≤T≤105
0<k1,k2<2
0<k3≤1
9<v<11
k1,k2,k3 contain 1 digit after decimal.
v contains 2 digits after decimal.

Subtasks
Subtask #1 (100 points): original constraints

Sample Input:
3
1.0 1.0 1.0 10.45
1.0 1.0 1.0 10.44
1.0 1.0 0.9 10.44
Sample Output:
YES
NO
NO
Explanation:
TestCase 1: Final speed of Chef after considering all the factors will be 1∗1∗1∗10.45=10.45 m / sec. So the time taken
to complete the race will be 100/10.45=9.569=9.57 sec after rounding to 2 places after decimal. Since the time is
strictly less than the world record time, therefore Chef can break the record.

TestCase 2: Final speed of Chef after considering all the factors will be 1∗1∗1∗10.44=10.44 m / sec. So the time taken
to complete the race will be 100/10.44=9.578=9.58 sec after rounding to 2 places after decimal. Since the time is equal
to the world record time, therefore Chef can't break the record.

TestCase 3: Final speed of Chef after considering all the factors will be 1∗1∗0.9∗10.44=9.396 m / sec. So the time
taken to complete the race will be 100/9.396=10.643=10.64 sec after rounding to 2 places after decimal. Since the time
is strictly more than the world record time, therefore Chef can't break the record.
"""


import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(float, input.split()))
    T = data[0]
    idx = 1
    while T > 0:
        k1, k2, k3, v = data[idx:idx+4]
        if round(100/(k1*k2*k3*v), 2) < 9.58:
            print("YES")
        else:
            print("NO")
        T -= 1
        idx += 4


# Time : 0.21s
