# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 18:10:51 2025

@author: KC Cheuk

    2379. Minimum Recolors to Get K Consecutive Black Blocks
    https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/?envType=daily-question&envId=2025-03-08
    
"""
"""
            This Solution Beat 100%
"""

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        left, right = 1, k
        move = blocks[:k].count("W")
        ans = move
        
        while right<len(blocks):
            if blocks[left-1] == "W":
                move -= 1
            
            if blocks[right] == "W":
                move += 1
            
            ans = min(move, ans)
            left += 1
            right += 1
            
            
        return ans
    
