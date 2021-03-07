# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
    	if not preorder:
    		return 
        self.root = TreeNode(preorder[0])
       
        for i in preorder[1:]:
        	r = self.create_bst(self.root,i)
        return r

    def create_bst(self,root,item):
    	if root.val > item:
    		if not root.left:
    			root.left = TreeNode(item)
    		else:
    			self.create_bst(root.left,item)

    	if root.val < item:
    		if not root.right:
    			root.right = TreeNode(item)
    		else:
    			self.create_bst(root.right,item)
    	return root


s = Solution()
preorder = [8,5,1,7,10,12]
r = s.bstFromPreorder(preorder)
