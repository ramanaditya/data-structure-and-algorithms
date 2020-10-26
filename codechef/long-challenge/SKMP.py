"""
[Smallest KMP](https://www.codechef.com/AUG20B/problems/SKMP)
Chef has a string S. He also has another string P, called pattern. He wants to find the pattern in S, but that might
be impossible. Therefore, he is willing to reorder the characters of S in such a way that P occurs in the resulting
string (an anagram of S) as a substring.

Since this problem was too hard for Chef, he decided to ask you, his genius friend, for help. Can you find the
lexicographically smallest anagram of S that contains P as substring?

Note: A string B is a substring of a string A if B can be obtained from A by deleting several (possibly none or all)
characters from the beginning and several (possibly none or all) characters from the end.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test
cases follows.
The first line of each test case contains a single string S.
The second line contains a single string P.

Output
For each test case, print a single line containing one string ― the smallest anagram of S that contains P.

Constraints
1≤T≤10
1≤|P|≤|S|≤105
S and P contain only lowercase English letters
there is at least one anagram of S that contains P

Subtasks
Subtask #1 (20 points): |S|≤1,000
Subtask #2 (80 points): |S|≤105

Example Input
3
akramkeeanany
aka
supahotboy
bohoty
daehabshatorawy
badawy

Example Output
aaakaeekmnnry
abohotypsu
aabadawyehhorst
"""
from collections import Counter

if __name__ == "__main__":
    T = int(input())
    while T:
        S = input()
        P = input()
        pi = 0
        dictS = Counter(S)
        pend = len(P)
        while pi < pend:
            dictS[P[pi]] -= 1
            pi += 1
        res = []
        for k, v in dictS.items():
            if v > 0:
                res.append(k * v)
        res.append(P)
        print("".join(sorted(res)))
        T -= 1

# Partially Correct
# Subtask 1 Task 5 WA
