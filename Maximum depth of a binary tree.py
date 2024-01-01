# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dep(root):
            if root is None:
                return 0
            left=dep(root.left)
            right=dep(root.right)
            return 1+max(left,right)
        ans=dep(root)
        return ans
