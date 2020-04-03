"""
[A. Dreamoon and Ranking Collection](https://codeforces.com/contest/1330/problem/A)
time limit per test1 second
memory limit per test256 megabytes
input : standard input
output : standard output
Dreamoon is a big fan of the Codeforces contests.

One day, he claimed that he will collect all the places from 1 to 54 after two more rated contests. It's amazing!

Based on this, you come up with the following problem:

There is a person who participated in 𝑛 Codeforces rounds. His place in the first round is 𝑎1, his place in the second
round is 𝑎2, ..., his place in the 𝑛-th round is 𝑎𝑛.

You are given a positive non-zero integer 𝑥.

Please, find the largest 𝑣 such that this person can collect all the places from 1 to 𝑣 after 𝑥 more rated contests.

In other words, you need to find the largest 𝑣, such that it is possible, that after 𝑥 more rated contests, for each
1≤𝑖≤𝑣, there will exist a contest where this person took the 𝑖-th place.

For example, if 𝑛=6, 𝑥=2 and 𝑎=[3,1,1,5,7,10] then answer is 𝑣=5, because if on the next two contest he will take
places 2 and 4, then he will collect all places from 1 to 5, so it is possible to get 𝑣=5.

Input
The first line contains an integer 𝑡 (1≤𝑡≤5) denoting the number of test cases in the input.

Each test case contains two lines. The first line contains two integers 𝑛,𝑥 (1≤𝑛,𝑥≤100). The second line contains
𝑛 positive non-zero integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤100).

Output
For each test case print one line containing the largest 𝑣, such that it is possible that after 𝑥 other contests, for
each 1≤𝑖≤𝑣, there will exist a contest where this person took the 𝑖-th place.

Example
input
5
6 2
3 1 1 5 7 10
1 100
100
11 1
1 1 1 1 1 1 1 1 1 1 1
1 1
1
4 57
80 60 40 20

output
5
101
2
2
60

Note
The first test case is described in the statement.

In the second test case, the person has one hundred future contests, so he can take place 1,2,…,99 and place 101 on
them in some order, to collect places 1,2,…,101.
"""
import sys


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = int(data[0])
    it = 1
    while T > 0:
        a = data[it]
        x = data[it + 1]
        array = data[it + 2 : it + 2 + a]
        count = 1
        check = 1
        while x:
            if not check in array:
                count += 1
                x -= 1
            check += 1
        for i in range(a):
            if check in array:
                check += 1
            else:
                break
        print(check - 1)
        it += 2 + a
        T -= 1
