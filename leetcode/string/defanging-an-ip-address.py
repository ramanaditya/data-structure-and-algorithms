'''
## Questions

### 1108. [Defanging an IP Address](https://leetcode.com/problems/defanging-an-ip-address/)

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:

- The given address is a valid IPv4 address.
'''

## Solutions


class Solution:
    def defangIPaddr(self, address: str) -> str:
        b = ''
        for i in address:
            if i == '.':
                b += '[.]'
            else:
                b += i
        return b
            

# Runtime: 24 ms
# Memory Usage: 13.8 MB