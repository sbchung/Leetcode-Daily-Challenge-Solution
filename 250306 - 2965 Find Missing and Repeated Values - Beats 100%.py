# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 00:28:59 2025

@author: KC Cheuk

        2965. Find Missing and Repeated Values
        https://leetcode.com/problems/find-missing-and-repeated-values/description/?envType=daily-question&envId=2025-03-06
"""

"""
            This solution beats 100%
"""

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        ttl = sum(map(sum, grid))
        seen = set()
        ans = [0,0]
        for row in grid:
            for x in row:
                if x not in seen:
                    seen.add(x)
                else:
                    ans[0] = x
                    break
        
        n = len(grid)**2
        ans[1] = int((n+1)*n/2 - ttl + ans[0])
        return ans
        
        
