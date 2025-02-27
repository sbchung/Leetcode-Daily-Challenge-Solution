# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:19:02 2025

@author: KC CHEUK

    873. Length of Longest Fibonacci Subsequence
    A sequence x1, x2, ..., xn is Fibonacci-like if:

    n >= 3
    xi + xi+1 == xi+2 for all i + 2 <= n
    Given a strictly increasing array arr of positive integers forming a sequence, 
    return the length of the longest Fibonacci-like subsequence of arr. If one 
    does not exist, return 0.
    
    A subsequence is derived from another sequence arr by deleting any number of 
    elements (including none) from arr, without changing the order of the remaining 
    elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

 

    Example 1:
        Input: arr = [1,2,3,4,5,6,7,8]
        Output: 5
        Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

    Example 2:
        Input: arr = [1,3,7,11,12,14,18]
        Output: 3
        Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].

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
    

            
            