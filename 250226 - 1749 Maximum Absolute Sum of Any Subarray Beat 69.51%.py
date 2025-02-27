# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:04:01 2025

@author: KC CHEUK

    You are given an integer array nums. The absolute sum of a subarray 
    [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
    
    Return the maximum absolute sum of any (possibly empty) subarray of nums.
    
    Note that abs(x) is defined as follows:
        If x is a negative integer, then abs(x) = -x.
        If x is a non-negative integer, then abs(x) = x.
     
    Example 1:
        Input: nums = [1,-3,2,3,-4]
        Output: 5
        Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
    
    Example 2:
        Input: nums = [2,-5,1,-4,3,-2]
        Output: 8
        Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

"""

"""
                This solution beats 69.51%
                
                Follow the hints use Kadane's algorithm and run the max and 
                min sum in one pass
"""

class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        maxEnding = nums[0]
        minEnding = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            maxEnding = nums[i] if maxEnding<0 else maxEnding+nums[i]
            minEnding = nums[i] if minEnding>0 else minEnding+nums[i]
            ans = max( abs(minEnding), maxEnding, ans)

        return ans
    
    
s = Solution()
nums = [1,-3,2,3,-4]
s.maxAbsoluteSum(nums)