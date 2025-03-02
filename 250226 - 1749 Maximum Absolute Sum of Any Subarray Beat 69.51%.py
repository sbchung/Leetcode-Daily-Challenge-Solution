# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:04:01 2025

@author: KC CHEUK

    1749 Maximum Absolute Sum of Any Subarray
    https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/
    
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