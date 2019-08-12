---
layout: page
title: "242. Valid Anagram"
subtitle: 
description: ""
author: "aditya"
comments: true
image: assets/images/code_pic.png
meta_image: assets/images/code_pic_meta.png
categories: [code,leetcode]
tags: [python,string,easy]
extra_tags: 
leetcode_slno: 242
featured: false
excerpt: ""
hidden: true
permalink: /:categories/:title

---

## Questions

### 242. [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

Given two strings s and t , write a function to determine if t is an anagram of s.

**Example 1:**

```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**

```
Input: s = "rat", t = "car"
Output: false
```
**Note:**

You may assume the string contains only lowercase alphabets.

**Follow up:**

What if the inputs contain unicode characters? How would you adapt your solution to such case?

## Solutions

{% highlight python %}

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        
        if len(s) != len(t):
            return False
        
        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for j in t:
            if j in d2:
                d2[j] += 1
            else:
                d2[j] = 1
        
        return d1 == d2

# Runtime: 52 ms
# Memory Usage: 14.2 MB

{% endhighlight %}


{% highlight python %}

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        
        return True

# Runtime: 40 ms
# Memory Usage: 14 MB

{% endhighlight %}