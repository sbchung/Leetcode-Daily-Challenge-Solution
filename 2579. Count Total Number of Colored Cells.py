# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 19:12:20 2025

@author: KC Cheuk

2579. Count Total Number of Colored Cells
https://leetcode.com/problems/count-total-number-of-colored-cells/description/?envType=daily-question&envId=2025-03-05
"""

"""
            This Solutions Beats 100%
"""

class Solution:
    def coloredCells(self, n: int) -> int:
        return n**2 + (n-1)**2

