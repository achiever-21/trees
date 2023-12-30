##############################################################postorder traversal###################################################################################################
Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
***********************************************code RECURSION*********************************************************************************
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def postorder(root,res):
            if root is not None:
                postorder(root.left,res)
                postorder(root.right,res)
                res.append(root.val)
        postorder(root,res)
        return res
#####################################################################
        