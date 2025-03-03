# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:19:02 2025

@author: KC CHEUK

    873. Length of Longest Fibonacci Subsequence
        https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/

"""
"""
                ***** THIS SOLUTION BEATS 91.72% *******
                
"""
from itertools import combinations

class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        dic = {x:i for i, x in enumerate(arr)}
        candidates = []
        
        for a, b in combinations(arr, 2):
            if a+b in dic:
                candidates.append([a,b,a+b])
        
        if len(candidates) == 0:
            return 0
        

        for seq in candidates:
            a, b, c = seq
            a = b+c
            while a in dic:
                seq.append(a)
                b, c = c, a
                a = b+c
        
        ans = max( candidates, key=len)
        return len(ans)
    

            
            