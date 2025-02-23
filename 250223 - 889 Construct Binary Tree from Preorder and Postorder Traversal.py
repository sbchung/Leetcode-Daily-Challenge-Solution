# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 19:26:45 2025

@author: KC Cheuk

889. Construct Binary Tree from Preorder and Postorder Traversal

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.

 
"""

"""
                    *** THIS SOLUTION BEATS 100% ****
                //Running time = 0 ms

"""
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        parent_dic = dict()

        post_idx = 0
        root = TreeNode(preorder[0])
        ptr = root

        for pre_idx in range(1, len(preorder)):

            
            if postorder[post_idx] not in parent_dic:
                ptr.left = TreeNode(preorder[pre_idx])
                parent_dic[ preorder[pre_idx] ] = ptr
                ptr = ptr.left
            else:
                # postorder element exist in parent_dic:
                # find the element's parent and check if
                # the next postorder element exist in parent_dic
                # repeat until the current postorder element is not in 
                # parent dic, and create node in the ptr.right

                while postorder[post_idx] in parent_dic:
                    ptr = parent_dic[ postorder[post_idx] ]
                    post_idx += 1
                
                ptr.right = TreeNode( preorder[pre_idx] )
                parent_dic[ preorder[pre_idx] ] = ptr
                ptr = ptr.right
        
        return root
    

    