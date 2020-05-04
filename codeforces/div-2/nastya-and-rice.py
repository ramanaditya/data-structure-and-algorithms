"""
[A. Nastya and Rice](https://codeforces.com/contest/1341/problem/A)
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output

Nastya just made a huge mistake and dropped a whole package of rice on the floor. Mom will come soon. If she sees this,
then Nastya will be punished.

In total, Nastya dropped 𝑛 grains. Nastya read that each grain weighs some integer number of grams from 𝑎−𝑏 to 𝑎+𝑏,
inclusive (numbers 𝑎 and 𝑏 are known), and the whole package of 𝑛 grains weighs from 𝑐−𝑑 to 𝑐+𝑑 grams, inclusive
(numbers 𝑐 and 𝑑 are known). The weight of the package is the sum of the weights of all 𝑛 grains in it.

Help Nastya understand if this information can be correct. In other words, check whether each grain can have such a
mass that the 𝑖-th grain weighs some integer number 𝑥𝑖 (𝑎−𝑏≤𝑥𝑖≤𝑎+𝑏), and in total they weigh from 𝑐−𝑑 to 𝑐+𝑑,
inclusive (𝑐−𝑑≤∑𝑖=1𝑛𝑥𝑖≤𝑐+𝑑).

Input
The input consists of multiple test cases. The first line contains a single integer 𝑡 (1≤𝑡≤1000)  — the number of test
cases.

The next 𝑡 lines contain descriptions of the test cases, each line contains 5 integers: 𝑛 (1≤𝑛≤1000)  — the number of
grains that Nastya counted and 𝑎,𝑏,𝑐,𝑑 (0≤𝑏<𝑎≤1000,0≤𝑑<𝑐≤1000)  — numbers that determine the possible weight of
one grain of rice (from 𝑎−𝑏 to 𝑎+𝑏) and the possible total weight of the package (from 𝑐−𝑑 to 𝑐+𝑑).

Output
For each test case given in the input print "Yes", if the information about the weights is not inconsistent, and print
"No" if 𝑛 grains with masses from 𝑎−𝑏 to 𝑎+𝑏 cannot make a package with a total mass from 𝑐−𝑑 to 𝑐+𝑑.

Example
inputCopy
5
7 20 3 101 18
11 11 10 234 2
8 9 7 250 122
19 41 21 321 10
3 10 8 6 1

outputCopy
Yes
No
Yes
No
Yes

Note
In the first test case of the example, we can assume that each grain weighs 17 grams, and a pack 119 grams, then really
Nastya could collect the whole pack.

In the third test case of the example, we can assume that each grain weighs 16 grams, and a pack 128 grams, then really
Nastya could collect the whole pack.

In the fifth test case of the example, we can be assumed that 3 grains of rice weigh 2, 2, and 3 grams, and a pack is 7
grams, then really Nastya could collect the whole pack.

In the second and fourth test cases of the example, we can prove that it is impossible to determine the correct weight
of all grains of rice and the weight of the pack so that the weight of the pack is equal to the total weight of all collected grains.


"""


import sys


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = int(data[0])
    it = 1
    while T > 0:
        n = data[it]
        a = data[it + 1]
        b = data[it + 2]
        c = data[it + 3]
        d = data[it + 4]
        mini = c - d
        maxi = c + d
        min_rice = mini / n if n != 0 else 0
        max_rice = maxi / n if n != 0 else 0
        if max_rice < (a - b) or min_rice > (a + b):
            print("No")
        else:
            print("Yes")
        it += 5
        T -= 1
