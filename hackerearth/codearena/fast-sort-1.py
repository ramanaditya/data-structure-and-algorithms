"""
[Fast Sort](https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/fast-sort-1/)
PROBLEM STATEMENT
Points: 30
From the childhood we are taught that a comes before b then b comes before c and so on.So whenever we try to sort any
given string we sort it in that manner only placing a before b and so on.But what happens if we initially change the
pattern of sorting .This question arrived in Arav's young mind. He thought what would the final string be like if z
comes before a and a comes after c and so on. He got really puzzled in finding out the final sorted string.So he asks
you for help.

He gives you two strings.One the pattern string P which decides the order of alphabets and the second that is the final
string F which needs to be sorted. Help him by telling him the final sorted string.

Input:
The first line contains T denoting the number of test cases.Each test case consists of two lines.The first line
contains the pattern string P indicating the relative ordering of alphabets and the second line contains the final
string F to be sorted.

Output:
Print T lines where each line contains the sorted string.

Constraints:
1 <= T <= 10
|P| = 28
1 <= |P| <= 10^5

Both the string consists only of characters 'a'-'z'.

SAMPLE INPUT
2
wcyuogmlrdfphitxjakqvzbnes
jcdokai
miruqopsxthzdcnvkfbglwayje
wgfsyvno
SAMPLE OUTPUT
codijak
osnvfgwy
Time Limit: 3.0 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
"""
import sys


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(str, input.split()))
    T = int(data[0])
    it = 1
    while T:
        P = {}
        S = data[it + 1]
        count = 0
        sorted = []
        for j in range(0, 26):
            sorted.append([])
        for i in data[it]:
            P[i] = count
            count += 1
        for j in S:
            sorted[P[j]].append(j)
        new_sorted = ""
        for i in sorted:
            new_sorted += "".join(i)
        print(new_sorted)
        it += 2
        T -= 1
