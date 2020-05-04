"""
[Count Numbers](https://www.hackerrank.com/contests/mentorshipkarona-webinar-by-vinit-shahdeo/challenges/count-numbers-1)

Vinit is a bad student. Once his teacher asked him to find the total count of numbers present in the given string S.
The task is pretty simple but he took three hours to solve it. The teacher got agitated at Vinit and asked you the same
question.

Can you solve it?

Input Format
The first line contains T , the number of test cases. The first line of each and every test case will contain a integer
N, the length of the string .

The second line of each and every test case will contain a string S of length N.

Constraints
0 < T < 200
0 < N < 10000

Output Format
For each and every testcase , output the total count of numbers present in the string.

Sample Input 0
1
26
vinit96shah4deo2vit100btec
Sample Output 0
4

Explanation 0
For the first test case , the string given is "vinit96shah4deo2vit100btec". There are total of 4 numbers in the
string - [96,4,2,100]. So , we output 4.
"""


T = int(input())
while T:
    N = int(input())
    S = input()
    before = False
    count = 0
    for i in range(0, N):
        if S[i].isnumeric():
            if before == True:
                pass
            else:
                count += 1
                before = True
        else:
            before = False
    print(count)
    T -= 1
