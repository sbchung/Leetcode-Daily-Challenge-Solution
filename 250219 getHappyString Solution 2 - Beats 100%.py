# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:30:36 2025

@author: KC Cheuk
"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        """
        Solution 2 :
            Beats 100% 0ms
        """

        if k> 3*(2**(n-1)):
            return ""
            
        happy = "abc"
        if n==1:
            return happy[k-1]

        def smallest(t):
            return "a" if t!="a"  else "b"
        
        k = k-1
        ans = ""
        
        quotient = k
        #remainder = k
        
        for i in range(1, n+1):
            d = 2**(n-i)
            remainder = quotient%d
            quotient = quotient//d
            
            if i < n:
                if ans=="":
                    ans = happy[ quotient ]
                else:
                    if quotient:
                        ans += "c" if ans[-1]!="c" else "b"
                    else:
                        #quotient = 0
                        ans += smallest( ans[-1] )
                quotient = remainder
            else:
                #i==n, last char
                if quotient:
                    ans += "c" if ans[-1]!="c" else "b"
                else:
                    ans += smallest( ans[-1] )
        return ans
    
    