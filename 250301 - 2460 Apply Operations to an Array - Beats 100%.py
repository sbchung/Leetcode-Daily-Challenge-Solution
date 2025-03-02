# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 18:28:39 2025

@author: KC CHEUK

    2460.Apply Operations to an Array
    https://leetcode.com/problems/apply-operations-to-an-array/description/

"""
"""
                    This Solution BEAT 100%
"""

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        ans = [0] * len(nums)
        ptr = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            if nums[i] != 0:
                ans[ptr] = nums[i]
                ptr += 1
        
        ans[ptr] = nums[-1]
        
        return ans