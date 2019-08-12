---
layout: page
title: "7. Reverse Integer"
subtitle: 
description: ""
author: "aditya"
comments: true
image: assets/images/code_pic.png
meta_image: assets/images/code_pic_meta.png
categories: [code,leetcode]
tags: [python,array,easy]
extra_tags: 
leetcode_slno: 7
featured: false
excerpt: ""
hidden: true
permalink: /:categories/:title
---

## Questions :

### 7. [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**
<pre>
Input: 123
Output: 321
</pre>

**Example 2:**
<pre>
Input: -123
Output: -321
</pre>

**Example 3:**
<pre>
Input: 120
Output: 21
</pre>

**Note:**

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


## Solutions

{% highlight python %}

import math
class Solution:
    def reverse(self, x: int) -> int:
        if (x > ((2 ** 31) - 1) or x < ((-1)*(2**31))):
            return 0
        else:
            if x < 0:
                x = abs(x)
                flag = 1
            else:
                flag = 0
            s = str(x)
            s = s[::-1]
            s = int(s)
            if s > ((2 ** 31) - 1):
                return 0
            else:
                if flag == 1:
                    s = (-1)*s
                    if s < ((-1)*(2**31)):
                        return 0
                    else:
                        return s
                else:
                    return s

# Runtime: 28 ms
# Memory Usage: 13.3 MB

{% endhighlight %}
