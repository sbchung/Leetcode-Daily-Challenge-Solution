# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:34:33 2025

@author: kaich

1261. Find elements in a contaminated binary tree

Given a binary tree with the following rules:

root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.

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