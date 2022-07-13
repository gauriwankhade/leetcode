# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        if not root:
            return
        
        self.res = True
        
        def helper(root, left, right):
            if not root:
                return 
                
            helper(root.left, left, root.val)
            helper(root.right, root.val, right)
            
            if left >= root.val or right <= root.val:
                self.res = False
                
            return self.res

        return helper(root, float('-inf'), float('inf'))
       
        
        
                



            
        
        
        
        