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
                            *** THIS SOLUTION BEATS 12.4% ****
                //Running time = 536 ms
                
                I have don't have much time to think of the answer
                Therefore, brute force to generate each possilbe answer and eleminate
                those exist. See if I can find another soluction later tdaoy
        """
        n = len(nums[0])
        s = set()
        
        #generate each possible combination
        for i in range(2**n):
            s.add( bin(i)[2:].zfill(n) )
        
        #remove those exist
        for x in nums:
            s.remove(x)
        
        return next(iter(s))