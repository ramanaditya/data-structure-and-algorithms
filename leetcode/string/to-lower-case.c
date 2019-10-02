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

char * toLowerCase(char * str){
    int len = sizeof(str)/sizeof(str[0])
    int i = 0
    while(str[i]){
        if(isalpha(str[i])){
            str[i] = tolower(str[i])
        }
        i += 1
    }
    return str
}

// Runtime: 0 ms
// Memory Usage: 6.6 MB
