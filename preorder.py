
DFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res=[]
        stack=[root]
        while stack:
            a=stack.pop()
            if a:
                res.append(a.val)
            if a.right:
                stack.append(a.right)
            if a.left:
                stack.append(a.left)
        return res
      ###################################################RECURSIVE APPROACH#######################################
def preorderTraversal(self,rott:Optional[TreeNode])->List[int]):
  res=[]
  def preorder(root,res):
    if root is None:
      return
    res.append(root.val)
    preorder(root.left,res)
    preorder(root.right,res)
  preorder(root,res)
  return res
  #############################################################################################
    
