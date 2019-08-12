---
layout: page
title: "189. Rotate Array"
subtitle: 
description: ""
author: "aditya"
comments: true
image: assets/images/code_pic.png
meta_image: assets/images/code_pic_meta.png
categories: [code,leetcode]
tags: [python,array,easy]
extra_tags: 
leetcode_slno: 189
featured: false
excerpt: ""
hidden: true
permalink: /:categories/:title

---

## Questions

### 189. [Rotate Array](https://leetcode.com/problems/rotate-array/)

Given an array, rotate the array to the right by k steps, where k is non-negative.

**Example 1:**

<pre>
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
</pre>

**Example 2:**

<pre>
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]

Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

</pre>

**Note:**

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

## Solutions

{% highlight python %}

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        while k > 0:
            nums.append(nums.pop(0))
            k = k - 1
        nums.reverse()

# Runtime: 80 ms
# Memory Usage: 13.4 MB
{% endhighlight %}