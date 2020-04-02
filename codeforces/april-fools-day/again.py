"""
[Again ?](https://codeforces.com/contest/1331/problem/D)
The only line of the input contains a 7-digit hexadecimal number. The first "digit" of the number is letter A, the rest
of the "digits" are decimal digits 0-9.

Output
Output a single integer.

Examples
input
A278832
output
0

input
A089956
output
0

input
A089957
output
1

input
A144045
output
1

"""
if __name__ == "__main__":
    n = input()
    res = int(bin(int(n, 16))[-1])
    print(res)
