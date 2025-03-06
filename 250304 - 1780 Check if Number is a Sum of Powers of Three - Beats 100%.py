"""
Date : 250304
Author : KC Cheuk
Content : 1780 Check if Number is a Sum of Powers of Three
Link : https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
"""

"""
            This Solution beast 100% of python submission
"""

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        while n>0:
            if n%3 == 2:
                return False
            else:
                if n%3 == 1:
                    n -= 1
                n = n//3
        return True