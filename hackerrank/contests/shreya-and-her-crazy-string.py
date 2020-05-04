"""
[Shreya and her Crazy String](https://www.hackerrank.com/contests/mentorshipkarona-webinar-by-vinit-shahdeo/challenges/shreya-and-her-crazy-string)

Shreya is President of VinnovateIT. She assigns a question to core members. The question is -

You have given a non-empty string. This string consists of lowercase or uppercase or both English letters. The length
of the string will not exceed 1000.

Convert the string using following cases:

Case 1: If first character of string is in lowercase then second character should be in uppercase, third character
should be in lowercase and so on till the last character of the string.

For example :

Input:   vinitshahdeo

Output:   vInItShAhDeO

Case 2: If first character of string is in uppercase then second character should be in lowercase, third character
should be in uppercase and so on till the last character of the string.

For example :
Input:    Vinitshahdeo

Output:   ViNiTsHaHdEo

Input Format
The first line of the input contains a single integer T denoting the number of test cases.

The first line of each test case contains a string.

Constraints
1 ≤ T ≤ 100

Output Format
For each test case, output the require string in newline.

Sample Input 0
2
vinitshahdeo
Shreyaanand

Sample Output 0
vInItShAhDeO
ShReYaAnAnD
"""


T = int(input())
while T:
    s = input()
    lower = True if ord(s[0]) >= 97 else False
    res = ""
    for i in s:
        if lower:
            res += i.lower()
            lower = False
        else:
            res += i.upper()
            lower = True
    print(res)
    T -= 1
