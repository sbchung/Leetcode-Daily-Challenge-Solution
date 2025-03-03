# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:46:07 2025

@author: kaich
"""
"""
        1980. Find Unique Binary String
        https://leetcode.com/problems/find-unique-binary-string/description/
        
        
                            *** THIS SOLUTION BEATS 12.4% ****
                //Running time = 536 ms
                
                I have don't have much time to think of the answer
                Therefore, brute force to generate each possilbe answer and eleminate
                those exist. See if I can find another soluction later tdaoy
"""
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        

        n = len(nums[0])
        s = set()
        
        #generate each possible combination
        for i in range(2**n):
            s.add( bin(i)[2:].zfill(n) )
        
        #remove those exist
        for x in nums:
            s.remove(x)
        
        return next(iter(s))