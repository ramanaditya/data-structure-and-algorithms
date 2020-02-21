/*
## Question

### 1. [Two Sum](https://leetcode.com/problems/two-sum/)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

// Solutions

import java.util.Scanner;
import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i = 0;
        int j = nums.length - 1;
        int[] res = new int[]{-1,-1};
        int new_target;
        for(i=0;i<j;i++){
            res[0] = i;
            new_target = target - nums[i];
            for(int k = i+1;k<=j;k++){
                if(nums[k] == new_target){
                    res[1] = k;
                    break;
                }
            }
            if(res[1] != -1){
                break;
            }
        }
        return res;
    }

    public static void main(String[] args){
        Solution sol = new Solution();
        Scanner sc = new Scanner(System.in);
        int n, target;
        int res[] = new int[2];
        System.out.println("Size of Array : ");
        n = sc.nextInt();
        int arr[] = new int[n];
        System.out.println("Enter the array : ");
        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
        }
        System.out.println("Target : ");
        target = sc.nextInt();
        res = sol.twoSum(arr, target);
        for(int i=0;i<2;i++){
            System.out.print(res[i]+" ");
        }
        sc.close();
    }
}

// Runtime: 35 ms, faster than 26.39% of Java online submissions
// Memory Usage: 39.3 MB, less than 5.65% of Java online submissions
