intuition :In this probelem what i followed is before problem we find max depth of a binary  in a recursive way in this also same method to find a each of the node but there is condiyion for balanced tree if the left subtrre and right subtree  diff should be les than or equal to 1:

class Solution:
  def __init__(self,right=None,left=None,val=0):
    self.left=left 
    self.right=right 
    self.val=0 
  def Balanaced(root):
    def deep(root):
      if root is None :
        return 0 
      left=deep(root.left)
      right=deep(root.right)
      if (abs(left-right)>1 or left==-1 or right==-1):
        return -1 
      retur max(left,right)+1
  if deep(root)==-1:
    return False 
else:
  return True
