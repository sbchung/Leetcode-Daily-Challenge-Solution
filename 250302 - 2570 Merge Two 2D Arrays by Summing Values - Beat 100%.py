# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 19:00:05 2025

@author: KC Cheuk

    2570. Merge Two 2D Arrays by Summing Values
    https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/
"""

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = dict()

        i = 0
        j = 0

        while i<len(nums1) and j<len(nums2):
            x1,y1 = nums1[i]
            x2,y2 = nums2[j]
            if x1 == x2:
                dic[x1] = y1 + y2
                i += 1
                j += 1
            elif x1<x2:
                dic[x1] = dic.get(x1,0) + y1
                i += 1
            else: #x1>x2
                dic[x2] = dic.get(x2,0) + y2
                j += 1

        ans = [ (x, y) for x, y in dic.items()]
        
        if i == len(nums1):
            ans += nums2[j:]
        else:
            ans += nums1[i:]

        return ans