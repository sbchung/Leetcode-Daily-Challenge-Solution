"""
Author : K C Cheuk
Date : 10 March 2025

        3208. Alternating Groups II
        https://leetcode.com/problems/alternating-groups-ii/description/?envType=daily-question&envId=2025-03-09
        
"""

"""
        This Solutions Beats 82.39%
"""
class Solution:
    def numberOfAlternatingGroups(self, colors: list[int], k: int) -> int:
        if len(colors) == 1:
            return k if k == 1 else 0
        
        diff = (colors[0] == colors[1])

        colors += colors[:k-1]
        ans = 0
        left = 0
        for i in range(len(colors)-1):
            # when diff=1, != diff mean looking for two same vale
            # when diff = 0, != diff mean looking for two diff value 
            if diff == 1:
                # look for difference
                if colors[i] != colors[i+1]:
                    left = i
                    diff = 0
            else:
                # look for same
                if colors[i] == colors[i+1]:
                    if i - left +1 >= k:
                        ans += i - left - k + 2
                        # left = i
                    diff = 1
        
        if diff == 0:
            if len(colors)-left>=k:
                ans += len(colors)-left-k+1
                
        return ans
