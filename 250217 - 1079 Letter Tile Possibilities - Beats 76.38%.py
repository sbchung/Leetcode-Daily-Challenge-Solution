# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:25:20 2025

@author: KC Cheuk

    You have n  tiles, where each tile has one letter tiles[i] printed on it.
    
    Return the number of possible non-empty sequences of letters you can make using
     the letters printed on those tiles.
    
    Example 1:
        Input: tiles = "AAB"
        Output: 8
        Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
    
    Example 2:
        Input: tiles = "AAABBC"
        Output: 188

    Example 3:
        Input: tiles = "V"
        Output: 1

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
