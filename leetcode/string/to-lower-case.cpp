/*
## Questions

### 709. [To Lower Case](https://leetcode.com/problems/to-lower-case/)

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
*/

// Solutions

class Solution
{
public:
    string toLowerCase(string str)
    {
        for (int i = 0; i < str.length(); i++)
        {
            if (str[i] >= 'A' && str[i] <= 'Z')
            {
                str[i] += 32;
            }
        }
        return str;
    }
};

// Runtime: 0 ms
// Memory Usage: 6.6 MB
