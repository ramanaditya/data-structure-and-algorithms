"""
EASY
[705. Design HashSet](https://leetcode.com/problems/design-hashset/)
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

Note:
All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
"""

# Solutions


class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = dict()

    def add(self, key: int) -> None:
        self.hashset[key] = self.hashset.get(key, key)

    def remove(self, key: int) -> None:
        val = self.hashset.get(key)
        if val is not None:
            del self.hashset[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        val = self.hashset.get(key)
        return True if val is not None else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Runtime: 208 ms, faster than 70.83% of Python3 online submissions
# Memory Usage: 18.3 MB, less than 57.14% of Python3 online submissions
