A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty pathH
***********************************code************************************************************************************************************************************************************************************
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max1=-10**9
        def deep(root):
            if root is None:
                return 0
            left=max(deep(root.left),0)
            right=max(deep(root.right),0)
            new1=root.val+left+right 
            self.max1=max(self.max1,new1)
            return root.val+max(left,right)
        deep(root)
        return self.max1
