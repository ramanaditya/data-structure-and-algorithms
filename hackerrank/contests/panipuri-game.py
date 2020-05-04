"""
[COVID-19 Lockdown after-party](https://www.hackerrank.com/contests/mentorshipkarona-webinar-by-vinit-shahdeo/challenges/panipuri-game)

Shreya and Vinit are besties. Due to this global pandemic, they're not hanging out together. As Shreya is missing her
street foods badly so they decided that they will go out daily to eat Panipuri after India wins the battle with Corona
Virus.

Is there anyone who doesn't know, what is Panipuri?

Panipuri is a crispy hollow ball made of semolina or wheat, filled with spicy potatoes and topped with tangy, spicy
tamarind water made fragrant by mint leaves and black salt.image

They started fighting that who'll pay the money?

As always, they decided that the looser will pay the money!

Of course! Winner will be the one who eats more number of Panipuri on the particular day!

Note - There is no tie i.e. there doesn't exist a day when both eat same number of Panipuris.

As both are busy in conducting Webinars, can you please help them to decide who has to pay the money on the given day?

As the nation battles to curb the impact of the coronavirus, our one and only responsibility right now is to stay safe
and practice social distancing. Are you also waiting to have Panipuri like Vinit/Shreya? Tweet to him at @Vinit_Shahdeo

Input Format
The first line will contain an array of size 7. This will represent the Panipuris eaten by Shreya on each day of a week
starting from Sunday.

Second line will also contain an array of size 7. This will represent the Panipuris eaten by Vinit on each day of a
week starting from Sunday.

Third line will contain an integer Q representing the number of queries.

Next Q lines will contain a string i.e. Sunday, Monday, . . . . , Saturday.

Constraints
|size of array| = 7

Elements of the given array cannot exceed 70.

Output Format
For each day, print the name of person, who will pay the money.

Note - The looser (not winner) will pay the money.

Sample Input 0
10 20 15 20 30 40 10
20 10 30 40 50 10 20
5
Monday
Wednesday
Saturday
Friday
Sunday

Sample Output 0
Vinit
Shreya
Shreya
Vinit
Shreya

Explanation 0

Day	        No. of Panipuris eaten by Shreya	No. of Panipuris eaten by Vinit
--------------------------------------------------------------------------------
Sunday	                10	                                20
Monday	                20	                                10
Tuesday	                15	                                30
Wednesday	            20	                                40
Thursday	            30	                                50
Friday	                40	                                10
Saturday	            10	                                20

Now, it's clear that Shreya has eaten more number of Panipuris on Monday and Friday. Also, Vinit has eaten more number
of Panipuris on Sunday, Tuesday, Wednesday, Thursday and Saturday.

According to the question, the one who will eat more number of Panipuri on particular day, he/she will be the winner.

Day	        Winner	    Who'll pay the money?
-----------------------------------------------
Sunday      Vinit	    Shreya
Monday      Shreya	    Vinit
Tuseday     Vinit	    Shreya
Wednesday   Vinit	    Shreya
Thursday	Vinit	    Shreya
Friday	    Shreya	    Vinit
Saturday	Vinit	    Shreya

For queries,
Monday
Wednesday
Saturday
Friday
Sunday

Output will be -
Vinit
Shreya
Shreya
Vinit
Shreya
"""


S = list(map(int, input().split()))
V = list(map(int, input().split()))
days = {
    "Sunday": 0,
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
}
Q = int(input())
while Q:
    day = input()
    if S[days[day]] < V[days[day]]:
        print("Shreya")
    else:
        print("Vinit")
    Q -= 1
