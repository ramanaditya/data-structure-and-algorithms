"""
[Minimum AND xor OR](https://www.hackerearth.com/challenges/competitive/march-circuits-20/algorithm/minimum-and-xor-or-6a05bbd4/)
Max. Marks: 100
You are given an array  of  integers. Determine the minimum value of the following expression for all valid :

, where .

Input format
First line: A single integer  denoting the number of test cases
For each test case:
First line contains a single integer , denoting the size of the array
Second line contains  space-separated integers

Output format
For each test case, print a single line containing one integer that represents the minimum value of the given expression

Constraints
Note: Sum of  overall test cases does not exceed

SAMPLE INPUT
2
5
1 2 3 4 5
3
2 4 7

SAMPLE OUTPUT
1
3

Explanation
For test case #1, we can select elements  and , the value of the expression is , which is the minimum possible value.
Another possible pair is 4 and 5.

For test case #2, we can select elements 4 and 7, the value of the expression is , which is the minimum possible value.

Time Limit:	1.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Marks are awarded if any testcase passes.
Allowed Languages:	Bash, C, C++, C++14, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8,
JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal, Perl,
PHP, Python, Python 3, Racket, Ruby, Rust, Scala, Swift, Swift-4.1, TypeScript, Visual Basic
"""
import sys


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = data[0]
    it = 1
    while T:
        prev = float("inf")
        n = data[it]
        row = data[it + 1 : it + 1 + n]
        row.sort()
        min_ = float("inf")
        for i in range(n - 1):
            if row[i + 1] ^ row[i] < min_:
                min_ = row[i + 1] ^ row[i]
        print(min_)
        it += n + 1
        T -= 1
