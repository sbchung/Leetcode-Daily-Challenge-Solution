# -*- coding: utf-8 -*-
"""
    2375. Construct Smallest Number From DI String
    https://leetcode.com/problems/construct-smallest-number-from-di-string/description/
"""

"""
                    *** THIS SOLUTION BEATS 100% ****
        //Running time = 0 ms
        
"""

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        def countD(p, i):
            j = 0
            while i<len(p):
                if  p[i]=="D":
                    j += 1
                    i += 1
                else:
                    break
            return j

        ans = ""
        available = ["1","2","3","4","5","6","7","8","9"]
        for i, x in enumerate(pattern):
            if x == "I":
                ans += available.pop(0)
            else:
                # x == "D"
                # count the number of continuous D
                
                n = countD(pattern, i)
                ans += available.pop(n)
        
        ans += available[0]
        return ans