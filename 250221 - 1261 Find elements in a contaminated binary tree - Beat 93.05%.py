# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:34:33 2025

@author: kaich

1261. Find elements in a contaminated binary tree

https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/

"""

"""
                    *** THIS SOLUTION BEATS 93.05% ****
        //Running time = 3 ms
        
        Simiply follow the instruction to perform DFS and use hash table to store the value.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.s = set([0])
        self.root = root
        self.root.val = 0
        self.recover(self.root)

    def recover(self, node):
        if node.left != None:
            node.left.val = 2*node.val + 1
            self.s.add(node.left.val)
            self.recover(node.left)

        if node.right != None:
            node.right.val = 2*node.val + 2
            self.s.add(node.right.val)
            self.recover(node.right)


    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)