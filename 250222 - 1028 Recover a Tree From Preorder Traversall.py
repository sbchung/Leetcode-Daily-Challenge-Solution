# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:44:18 2025

@author: kaich

1028. Recover a Tree From Preorde Traveral

We run a preorder depth-first search (DFS) on the root of a binary tree.
At each node in this traversal, we output D dashes (where D is the depth of this node),
 then we output the value of this node.  If the depth of a node is D, the depth 
 of its immediate child is D + 1.  The depth of the root node is 0.
If a node has only one child, that child is guaranteed to be the left child.
Given the output traversal of this traversal, recover the tree and return its root.
"""

"""
                    *** THIS SOLUTION BEATS 83.82% ****
                //Running time = 15 ms

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) :
        self.depth_dic = dict()
        self.root = TreeNode()
        ptr = self.root
        i = 0

        #get the value and index of next "-"
        ptr.val, i = self.get_val(traversal, i)
        last_level = 0

        while i<len(traversal):
            level = self.get_level(traversal, i)
            i += level
            val, i = self.get_val(traversal, i)

            if level == last_level:
                #load the parent node 
                ptr = self.depth_dic[level-1]
            elif level - last_level == 1:
                #next level, save the current node in the current level
                self.depth_dic[last_level] = ptr
                last_level = level
            else:
                #return to a certain level before
                last_level = level
                ptr = self.depth_dic[level-1]
            
            # assign the pointer to the left node first if left is empty
            if ptr.left is None:
                ptr.left = TreeNode()
                ptr = ptr.left
            else:
                ptr.right = TreeNode()
                ptr = ptr.right
                
            ptr.val = val
            
        return self.root
    
    def get_val(self, trav, i):
        #convert string to integer
        j = 1
        while i+j<len(trav) and trav[i+j] != "-":
            j += 1

        return int(trav[i:i+j]), i+j

    
    def get_level(self, trav, i):
        #find the level of the following value
        j = 0
        while trav[i]=="-":
            i+=1
            j+=1

        return j
    