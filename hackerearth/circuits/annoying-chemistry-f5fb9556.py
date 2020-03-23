"""
[Annoying Chemistry](https://www.hackerearth.com/challenges/competitive/march-circuits-20/algorithm/annoying-chemistry-f5fb9556/)
Max. Marks: 100
You are given a chemical equation of the following format:
Your task is to calculate the balancing factor b1, b2, and b3 such that the number of atoms of each of the elements is
equal on both sides.

Note: The answer must be in a reduced form.

Input format

The first line consists of four integers x, y, p, and q.

Output format

The output must contain b1, b2, and b3.

Constraints
1 <= x,y,p,q <= 10^4

SAMPLE INPUT
2 3 4 5

SAMPLE OUTPUT
6 5 3

Explanation
Given chemical equation is :

C2  +  H3     -------->    C4 H5

The balanced chemical equation is:

6 C2  + 5 H3     -------->    3 C4 H5

Time Limit:	2.0 sec(s) for each input file.
Memory Limit:	256 MB
Source Limit:	1024 KB
Marking Scheme:	Marks are awarded if any testcase passes.
Allowed Languages:	Bash, C, C++, C++14, Clojure, C#, D, Erlang, F#, Go, Groovy, Haskell, Java, Java 8,
JavaScript(Rhino), JavaScript(Node.js), Julia, Kotlin, Lisp, Lisp (SBCL), Lua, Objective-C, OCaml, Octave, Pascal,
Perl, PHP, Python, Python 3, Racket, Ruby, Rust, Scala, Swift, Swift-4.1, TypeScript, Visual Basic
"""
import sys


def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    a, b, c, d = data[:]
    p = c * b
    q = d * a
    r = a * b
    gcd = find_gcd(p, find_gcd(q, r))
    print(p // gcd, q // gcd, r // gcd)
