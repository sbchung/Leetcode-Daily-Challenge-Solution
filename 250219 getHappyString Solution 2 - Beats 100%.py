# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 22:30:36 2025

@author: KC Cheuk
"""

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        """
        1415. The k-th Lexicographical String of All Happy Strings of Length n
        https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
        
        """
                                   
        """
        
        
                                       *** THIS SOLUTION BEATS 100% ****
        //Running time = 0 ms
        
        
        The idea is to construct the k-th happy string directly by counting permutations
        instead of generating all possible happy strings and selecting the k-th one.
        
        For example, if n = 3 and k = 9:
        - A happy string of length 3 consists of 3 characters, where each character must
          be different from the previous one.
        - The first character determines a group of strings, where each choice of the
          first character leads to multiple valid strings.
        - Since we have 3 possible starting characters ('a', 'b', or 'c'), and each
          choice leads to (2^(n-1)) valid strings, we can determine the first character
          by dividing k by this count.
        - By iteratively reducing k and determining subsequent characters, we efficiently
          construct the desired string without generating all possibilities.
        """
        
        #Number of valid string is less the the required kth string, return ""
        if k> 3*(2**(n-1)):
            return ""
            
        happy = "abc"
        
        #Special case for the "for" loop, handle here
        if n==1:
            return happy[k-1]

        #Return the next smalles possible char which is different from the preious char
        #to make sure the answer is sorted, 
        def smallest(t):
            return "a" if t!="a"  else "b"
        
        # Because the k-th answer is 1-indexed
        # to compensate for the offset
        k = k-1  
        
        ans = ""
        quotient = k

        
        for i in range(1, n+1):
            d = 2**(n-i)
            remainder = quotient%d
            quotient = quotient//d  #quotient can either be 0 or 1
            
            if i < n:
                if ans=="":
                    ans = happy[ quotient ]
                else:
                    if quotient:
                        ans += "c" if ans[-1]!="c" else "b"
                    else:
                        # i.e. quotient = 0
                        ans += smallest( ans[-1] )
                quotient = remainder
            else:
                # i==n, i.e. last char
                if quotient:
                    ans += "c" if ans[-1]!="c" else "b"
                else:
                    ans += smallest( ans[-1] )
        return ans
    
    