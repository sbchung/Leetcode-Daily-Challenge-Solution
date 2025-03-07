# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 17:32:56 2025

@author: KC Cheuk
"""

class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        prime = [x for x in range(1, right+1)]
        # print( "original prime:", prime, len(prime))
        i = 1
        while 1:
            #find the next prime
            while i<right and prime[i]==0:
                i += 1
            
            if i == right:
                break
            
            step = prime[i]
            p = step*2
            
            while p<=len(prime):
                prime[p-1] = 0
                p += step
            
            i += 1
            if i > right:
                break
        
        prime = [x for x in prime[1:] if x > 0 and x >= left and x <= right]
        print(prime)
        if len(prime)>=2:
            return prime[:1]
        else:
            return [-1,-1]



s = Solution()
s.closestPrimes(1, 1000000)