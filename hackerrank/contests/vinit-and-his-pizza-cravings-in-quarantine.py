"""
[Vinit and His Pizza Cravings in Quarantine](https://www.hackerrank.com/contests/mentorshipkarona-webinar-by-vinit-shahdeo/challenges/vinit-and-his-pizza-cravings-in-quarantine)

Vinit loves Pizza! He visits the Binary Pizza Shop to buy some of his favorite flavors.

The owner of the bakery, Sharmishtha, is a clever woman. As she knows that Vinit is a BIG foodie guy, She does not want
Vinit to finish all her Pizzas as there is shortage of raw materials due to COVID-19 lockdown. Hence, she plays a game.

Vinit is given N numbers and has to select K of these numbers. For each number that Vinit chooses, he will get as many
pizza as the number of 1's in the Binary representation of the number.

Help Vinit to find the maximum number of Pizzas that he can have.

In return, he will treat you with a Pizza after the COVID-19 lockdown ends! :XD :P
Ping him on Twitter(@Vinit_Shahdeo)

Input Format
The first line of input contains T. T test cases follow.
First line of each test cases contains 2 space-separated integers N and K.
The next line contains N space-separated integers.

Constraints
1 ≤ T ≤ 10
1 ≤ N ≤ 103
0 ≤ K ≤ N
0 ≤ Numbers ≤ 105

Output Format
For each test cases, print the answer in a new line.

Sample Input 0
1
4 2
6 1 2 0
Sample Output 0
3

Explanation 0
He chooses numbers 6 (110) and 1 (001) with 2 and 1 set bits respectively.
"""


from operator import itemgetter

T = int(input())
while T:
    N, K = list(map(int, input().split()))
    pizza = list(map(int, input().split()))
    res = []
    for p in pizza:
        temp = [p]
        temp.append(bin(p)[2:].count("1"))
        res.append(temp)
    ret = 0
    new_pizza = sorted(res, key=itemgetter(1), reverse=True)
    for i in range(K):
        ret += new_pizza[i][1]
    print(ret)
    T -= 1
