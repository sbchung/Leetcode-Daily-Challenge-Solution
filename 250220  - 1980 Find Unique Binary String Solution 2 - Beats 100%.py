# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:46:07 2025

@author: kaich
"""

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        """
        Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
            Example 1:
            
            Input: nums = ["01","10"]
            Output: "11"
            Explanation: "11" does not appear in nums. "00" would also be correct.
            Example 2:
            
            Input: nums = ["00","01"]
            Output: "11"
            Explanation: "11" does not appear in nums. "10" would also be correct.
            Example 3:
            
            Input: nums = ["111","011","001"]
            Output: "101"
            Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
             
            
            Constraints:
            
            n == nums.length
            1 <= n <= 16
            nums[i].length == n
            nums[i] is either '0' or '1'.
            All the strings of nums are unique.
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
