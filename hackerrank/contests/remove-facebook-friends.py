"""
[Remove Facebook Friends](https://www.hackerrank.com/contests/mentorshipkarona-webinar-by-vinit-shahdeo/challenges/remove-facebook-friends)

Due to quarantine, Sherry is feeling so bored at home. 2 days back, she decided to join Facebook. And yes, she became
popular on Facebook in two days and her Facebook profile is full of friend requests. Being the nice girl she is, Sherry
has accepted all the requests.

Now Winit is jealous of all the attention she is getting from other guys, so he asks her to delete some of the guys
from her friend list.

To avoid a 'scene', Sherry decides to remove some friends from her friend list, since she knows the importance of each
of the friend she has, she uses the following algorithm to delete a friend.


DeleteFriend=false
    for i = 1 to Friend.length-1
         if(Friend[i].mutualFriends<minValue)
             delete i th friend
             DeleteFriend=true
         for j=i+1 to Friend.length
             if(Friend[i].name==Friend[j].name)
                 if(Friend[i].mutualFriends>Friend[j].mutualFriends)
                     delete j th friend
                     DeleteFriend=true
                 else
                     delete i the friend
                     DeleteFriend=true
            DeleteFriend=true
            break
    if(DeleteFriend == false)
        print "Sorry Winit!"


Input Format
First line contains T number of test cases. First line of each test case contains N, the number of friends Shreya
currently has and K, the minumum number of mutual friends she must have. Next N lines contains name of her friend and
her mutual friends.

Constraints
1<=T<=1000
1<=N<=100000
0<=K< N

Output Format
For each test case print name of her friend (in lexagraphical order) and their mutual friends separated by space in
new line. Print "Sorry Winit" if none of the friends are deleted according to the alogrithm.

Sample Input 0
1
7 4
Vinit 8
Yashna 5
Rasika 6
Akansha 5
Akansha 6
Archit 2
Raghav 4

Sample Output 0
Akansha 6
Raghav 4
Rasika 6
Vinit 8
Yashna 5

Sample Input 1
1
4 2
Prerna 12
Nandini 12
Samriddhi 2
Ashika 8

Sample Output 1
Sorry Winit!
"""

from operator import itemgetter

T = int(input())
while T:
    N, K = list(map(int, input().split()))
    d = []
    for i in range(int(N)):
        data = list(map(str, input().split()))
        d.append(data)

    DeleteFriend = False
    delete = []

    for i in range(0, len(d)):
        if int(d[i][1]) < int(K):
            delete.append(d[i])
            DeleteFriend = True
        for j in range(i + 1, len(d)):
            if d[i][0] == d[j][0]:
                if int(d[i][1]) > int(d[j][1]):
                    delete.append(d[j])
                    DeleteFriend = True
                else:
                    delete.append(d[i])
                    DeleteFriend = True

    if len(delete) == 0:
        print("Sorry Winit!")
    else:
        for i in sorted(d, key=itemgetter(0)):
            if not i in delete:
                print("{0} {1}".format(i[0], i[1]))
    T -= 1
