# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:25:20 2025

@author: KC Cheuk

    1079 Letter Title Possibilities
    https://leetcode.com/problems/letter-tile-possibilities/description/
"""

"""
                    *** THIS SOLUTION BEATS 76.38% ****
        //Running time = 23 ms
        
        Generate all the possible outcome and count the distinct permutation
        although this solution is not the fastest, but it definitely simple enough
"""
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        t = set()

        ans = 0
        
        for i in  range(1, len(tiles)+1):
            for x in permutations(tiles, i):
                if not x in t:
                    ans += 1
                    t.add(x)
        
        return ans
