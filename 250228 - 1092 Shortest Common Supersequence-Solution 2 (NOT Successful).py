# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 04:31:30 2025

@author: KC Cheuk

1092 Shortest Common Supersequence
https://leetcode.com/problems/shortest-common-supersequence/description/
"""

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        p1, p2 = 0, 0
        
        ans = ""
        
        while p1<len(str1) and p2<len(str2):
            if str1[p1] == str2[p2]:
                ans += str1[p1]
                p1 += 1
                p2 += 1
            else:
                i1 = 1
                i2 = 1
                while 1:
                    if p2+i2<len(str2):
                        if str1[p1] != str2[p2+i2]:
                            if p1+i1<len(str1):
                                if str1[p1+i1] != str2[p2]:
                                    i1 += 1
                                    i2 += 1
                                else:
                                    ans += str1[p1:p1+i1+1]
                                    p1 += i1 + 1
                                    p2 += 1
                                    break
                        else:
                            ans += str2[p2:p2+i2+1]
                            p1 += 1
                            p2 += i2 + 1
                            break
                    else:
                        #str2 end
                        ans += str2[p2:] + str1[p1:]
                        p1=len(str1)
                        break
        
        if p1 < len(str1):
            ans += str1[p1:]
        
        if p2<len(str2):
            ans += str2[p2:]
            
        return ans
                
                    
                    
                    
    











s = Solution()
str1 = "kqpabce"
str2 = "cabccc"

str1 = "baabaaabb"
str2 = "bbabbbaab"

str1 = "abckkk"
str2 = "pppabc"
print(s.shortestCommonSupersequence(str1, str2))
