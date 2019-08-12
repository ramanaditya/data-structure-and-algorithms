---
layout: page
title: "349. Intersection of Two Arrays"
subtitle: 
description: ""
author: "aditya"
comments: true
image: assets/images/code_pic.png
meta_image: assets/images/code_pic_meta.png
categories: [code,leetcode]
tags: [python,array,easy]
extra_tags: 
leetcode_slno: 349
featured: false
excerpt: ""
hidden: true
permalink: /:categories/:title

---

## Questions

### 349. [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)

Given two arrays, write a function to compute their intersection.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

**Note:**

- Each element in the result must be unique.
- The result can be in any order.

## Solutions

{% highlight python %}

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        j = 0
        nums1.sort()
        nums2.sort()
        res = []
        k = len(nums1)
        l = len(nums2)
        while i < k and j < l:
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i = i + 1
                j = j + 1
            elif nums1[i] < nums2[j]:
                i = i + 1
            else:
                j = j + 1
        res = list(set(res))
        return res

# Runtime: 68 ms
# Memory Usage: 14 MB

{% endhighlight %}


{% highlight python %}

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1.intersection(nums2))

# Runtime: 56 ms
# Memory Usage: 13.8 MB

{% endhighlight %}

{% highlight python %}

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums2) & set(nums1)

# Runtime: 48 ms
# Memory Usage: 14.1 MB

{% endhighlight %}