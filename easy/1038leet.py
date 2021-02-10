# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.result = 0
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return 
        return self.update(root)
    def update(self,curr):
        if curr == None:
            return
        
        self.update(curr.right)
        self.result+= curr.val
        curr.val = self.result
        self.update(curr.left)
        
        return curr
        
