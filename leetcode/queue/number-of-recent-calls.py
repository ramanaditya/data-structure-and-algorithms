"""
## Questions: EASY

### 933. [Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)

Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.

Example 1:
Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]

Note:
Each test case will have at most 10000 calls to ping.
Each test case will call ping with strictly increasing values of t.
Each call to ping will have 1 <= t <= 10^9.
"""

# Solutions

from collections import deque


class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()
        self.q.append(t)
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

# Runtime: 308 ms, faster than 74.88% of Python3 online submissions
# Memory Usage: 18.5 MB, less than 49.02% of Python3 online submissions
