# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 17:32:56 2025

@author: KC Cheuk

        2523. Cloest Prime Numbers in Range
        https://leetcode.com/problems/closest-prime-numbers-in-range/description/?envType=daily-question&envId=2025-03-07
        
"""

"""
            This Solution Beats 57.50%
"""
from math import sqrt
from math import ceil
import itertools

class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        
        # prime number for efficent finding multiple
        p1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 1009]
        
        if left ==1:
            left = 2
            
        cand = list( range(left, right+1) )
        top = ceil( sqrt(right) )
        
        for i in range(len(p1)):
            
            prime = p1[i]
            if prime > top:
                break
            multiple = (left//prime + (1 if left%prime>0 else 0))
            if multiple == 1:
                multiple = 2
            x = prime*multiple
            while x <= right:
                cand[x-left] = 0
                multiple += 1
                x = prime*multiple
        
        p = [x for x in cand if x > 0]
        
        def find_diff( pair ):
            return pair[1]-pair[0]
        
        if len(p)<2:
            return [-1,-1]
        else:
            min_diff =list( map(find_diff, itertools.pairwise(p)))
            idx = min_diff.index(min(min_diff))
            return p[idx:idx+2]
        

        
