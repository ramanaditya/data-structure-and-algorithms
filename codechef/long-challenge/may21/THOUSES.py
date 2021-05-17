"""
[Tree House](https://www.codechef.com/MAY21C/problems/THOUSES)

1-2
    2-2
        5-2
            9-2
            10-4
            11-6
            12-8
        6-4
    3-4
        13-4
        14-8
    4-6

"""

import sys


class Node:
    def __init__(self, name=None, val=None, count=None):
        self.name = name
        self.val = val
        self.count = count
        self.children = []


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        rs = []
        next_level = [root]
        while next_level:
            cur_level = next_level
            next_level = []
            rs.append([(c.name, c.val) for c in cur_level])
            for c in cur_level:
                if c.children:
                    next_level.extend(c.children)

        return rs


def get_count(d: dict, N: int):
    x = dict()
    for i in range(1, N+1):
        q = d.get(i, []).copy()
        for ele in q:
            q.extend(d.get(ele, []).copy())
        x[i] = len(q)
    return x


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    T = data[0]
    mod = 1000000007
    idx = 1
    while T > 0:
        N, x = data[idx: idx + 2]
        idx += 2

        i = 0
        d = dict()
        while i < 2 * (N - 1):
            u, v = data[idx + i: idx + i + 2]
            d[u] = d.get(u, [])
            d[u].append(v)
            i += 2

        y = get_count(d, N)
        for k, v in d.items():
            for i in range(len(v)):
                d[k][i] = (v[i], y.get(v[i], 0))
            d[k] = sorted(d[k], key=lambda item: item[1], reverse=True)

        res = 0
        roots = Node(name=1, val=x, count=N-1)
        root = [roots]
        while root:
            node = root.pop(0)
            gcd = node.val
            res += node.val
            count = 0
            for ele in d.get(node.name, []):
                count += 1
                node.children.append(Node(name=ele[0], val=gcd*count, count=ele[1]))
            root.extend(node.children)

        print(res % mod)
        T -= 1
        idx += 2*(N-1)

# Time : 0.58s
