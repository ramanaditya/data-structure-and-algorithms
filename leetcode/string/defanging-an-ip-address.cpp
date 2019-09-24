/*
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
*/

// Solutions

class Solution
{
public:
    string defangIPaddr(string address)
    {
        int i = 0;
        while (i < address.length())
        {
            if (address[i] == '.')
            {
                address.replace(i, 1, "[.]");
                i += 3;
            }
            else
            {
                i += 1;
            }
        }
        return address;
    }
};

// Runtime: 4 ms
// Memory Usage: 8.2 MB