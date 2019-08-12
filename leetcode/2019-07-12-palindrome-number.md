---
layout: page
title: "9. Palindrome Number"
subtitle: 
description: ""
author: "aditya"
comments: true
image: assets/images/code_pic.png
meta_image: assets/images/code_pic_meta.png
categories: [code,leetcode]
tags: [python,array,easy]
extra_tags: 
leetcode_slno: 9
featured: false
excerpt: ""
hidden: true
permalink: /:categories/:title
---


## Question

### 9. [Palindrome Number](https://leetcode.com/problems/palindrome-number/)

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

**Example 1:**
<pre>
Input: 121
Output: true
</pre>

**Example 2:**

<pre>
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right 
to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

**Example 3:**

<pre>
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is 
not a palindrome.
</pre>

**Follow up:**

Coud you solve it without converting the integer to a string?



## Solutions

### Python

{% highlight python %}

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s[0] == '-':
            return False
        else:
            s = int(s[::-1])
            if s == x:
                return True
            else:
                return False

# Runtime: 80 ms
# Memory Usage: 13.2 MB
{% endhighlight %}

### C

{% highlight C %}

bool isPalindrome(int x) {
    int n,rev=0,rem;
    n=x;
    while(x>0)
    {
        rem=x%10;
        rev=rev*10+rem;
        x=x/10;
    }
    if(n==rev)
        return true;
    else
        return false;
}

# Runtime: 188 ms
# Memory Usage: -
{% endhighlight %}