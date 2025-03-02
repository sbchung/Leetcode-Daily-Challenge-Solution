# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:10:16 2025

@author: KC Cheuk
    
        1524 Number of Sub-arrays With Odd Sum
        https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/
"""

"""
                    *** THIS SOLUTION Beat 18.98% ****

"""

class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        arr2 = [arr[0]%2]*len(arr)
        for i in range(1, len(arr)):
            arr2[i] = (arr2[i-1]+arr[i])%2
            
        odd = sum(arr2)
        even = len(arr2)-odd
        
        ans = odd
        flip = False
        
        for x in arr2:
            if x^flip:
                odd -= 1
                odd, even = even, odd
                flip = not flip
            else:
                even -= 1
                
            ans += odd
            
        return ans%(10**9+7)
    
