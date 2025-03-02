# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:46:07 2025

@author: KC Cheuk
"""

"""
        1980. Find Unique Binary String
        https://leetcode.com/problems/find-unique-binary-string/description/
"""

"""
                    *** THIS SOLUTION BEATS 100% ****
        //Running time = 0 ms
        
        The idea is to create a string with a different char from each 
        element of the nums
        
        For example if nums = ["01", "00"]
        as 1st char in first element ("01") is "0"
        so ANS = "1"
        
        then we make sure ANS is different from the 1st element
        consdier the 2nd char in the 2nd element ("00"), which is "0"
        so ANS = "11"
        as the 2nd char is different from the second element, we make sure
        the ANS is different from 2nd element.
        
        Hence, the ANS us unique and different from all the elements in nums
"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])

        ans = ""
        
        for i, x in enumerate(nums):
            ans += "0" if x[i]=="1" else "1"
            i += 1
        
        return ans.ljust(n, "0")
