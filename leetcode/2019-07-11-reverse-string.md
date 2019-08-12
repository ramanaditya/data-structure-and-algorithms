---
layout: page
title: "344. Revese String"
subtitle: 
description: ""
author: "aditya"
comments: true
image: assets/images/code_pic.png
meta_image: assets/images/code_pic_meta.png
categories: [code,leetcode]
tags: [python,array,easy]
extra_tags: 
leetcode_slno: 344
featured: false
excerpt: ""
hidden: true
permalink: /:categories/:title
---

## Question

### 344. [Revese String](https://leetcode.com/problems/reverse-string/)

Write a function that reverses a string. The input string is given as an array of characters `char[]`.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of `printable ascii characters`.

 

**Example 1:**

```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

**Example 2:**

```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Solutions

{% highlight python %}

class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1

# Runtime: 164 ms
# Memory Usage: 17.6
{% endhighlight %}

{% highlight python %}

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

# Runtime: 164 ms
# Memory Usage: 17.6
{% endhighlight %}