# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:10:16 2025

@author: KC Cheuk
Given an array of integers arr, return the number of subarrays with an odd sum.
Since the answer can be very large, return it modulo 109 + 7.

    Example 1:
        Input: arr = [1,3,5]
        Output: 4
        Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
        All sub-arrays sum are [1,4,9,3,8,5].
        Odd sums are [1,9,3,5] so the answer is 4.

    Example 2:
        Input: arr = [2,4,6]
        Output: 0
        Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
        All sub-arrays sum are [2,6,12,4,10,6].
        All sub-arrays have even sum and the answer is 0.

    Example 3:
        Input: arr = [1,2,3,4,5,6,7]
        Output: 16
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
    
