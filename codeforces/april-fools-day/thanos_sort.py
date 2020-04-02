"""
[Thanos Sort](https://codeforces.com/contest/1145/problem/A)
Thanos sort is a supervillain sorting algorithm, which works as follows: if the array is not sorted, snap your fingers*
to remove the first or the second half of the items, and repeat the process.

Given an input array, what is the size of the longest sorted array you can obtain from it using Thanos sort?

*Infinity Gauntlet required.

Input
The first line of input contains a single number 𝑛 (1≤𝑛≤16) — the size of the array. 𝑛 is guaranteed to be a power of 2.
The second line of input contains 𝑛 space-separated integers 𝑎𝑖 (1≤𝑎𝑖≤100) — the elements of the array.

Output
Return the maximal length of a sorted array you can obtain using Thanos sort. The elements of the array have to be sorted in non-decreasing order.

Examples
input
4
1 2 2 4
output
4

input
8
11 12 1 2 13 14 3 4
output
2

input
4
7 6 5 4
output
1

Note
In the first example the array is already sorted, so no finger snaps are required.

In the second example the array actually has a subarray of 4 sorted elements, but you can not remove elements from
different sides of the array in one finger snap. Each time you have to remove either the whole first half or the whole
second half, so you'll have to snap your fingers twice to get to a 2-element sorted array.

In the third example the array is sorted in decreasing order, so you can only save one element from the ultimate
destruction.


"""


def thanos(arr):
    if arr == sorted(arr):
        return len(arr)
    else:
        return max(thanos(arr[: len(arr) // 2]), thanos(arr[len(arr) // 2 :]))


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    res = thanos(a)
    print(res)
