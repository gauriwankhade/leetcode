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
                return True
                
            helper(root.left, left, root.val)
            helper(root.right, root.val, right)

            # if left:
            #     maxLeft = max(left.val, maxLeft)
            # if right:
            #     minRight = min(right.val, minRight)
            
            if left >= root.val or right <= root.val:
                self.res = False
                
        
        helper(root, float('-inf'), float('inf'))
        return self.res
        
        
                



            
        
        
        
        