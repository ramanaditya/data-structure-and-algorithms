"""
[Valid Pair](https://www.codechef.com/APRIL21C/problems/SOCKS1)
Chef has three socks in his drawer. Each sock has one of 10 possible colours, which are represented by integers between
1 and 10. Specifically, the colours of the socks are A, B, and C.

Chef has to wear two socks which have the same colour. Help Chef find out if that is possible or not.

Input
The first and only line of the input contains three space-separated integers A, B and C.

Output
Print a single line containing the string "YES" if it is possible for Chef to wear two socks with the same colour or
"NO" if it is impossible (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes"
and "YES" will all be treated as identical).

Constraints
1≤A,B,C≤10

Subtasks
Subtask #1 (100 points): original constraints

Example Input 1
5 4 3
Example Output 1
NO
Explanation
Since there are no two socks with the same colour, Chef cannot wear a pair of socks with the same colour.

Example Input 2
5 5 5
Example Output 2
YES
Explanation
Since all three socks have the same colour, Chef can wear a pair of socks with the same colour.
"""


import sys

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    if data[0] == data[1] or data[0] == data[2] or data[1] == data[2]:
        print("YES")
    else:
        print("NO")

# Time : 0.01s
