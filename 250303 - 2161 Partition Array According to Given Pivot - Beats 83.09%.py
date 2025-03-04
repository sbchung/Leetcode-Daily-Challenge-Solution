# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 18:12:50 2025

@author: KC Cheuk

2161. Partition Array According to Given Pivot
https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=daily-question&envId=2025-03-03
"""

"""
             This solution Beats 83.09%
             
"""
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equal = []
        larger = []

        for x in nums:
            if x < pivot:
                smaller.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                larger.append(x)
        
        return smaller + equal + larger