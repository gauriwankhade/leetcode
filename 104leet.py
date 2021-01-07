# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.result = 0
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.recursion(root)
        return self.result
        
    def recursion(self,node):
        if not node:
            return
        self.count+=1
        self.recursion(node.left)
        self.recursion(node.right)
        
        self.result = max(self.result,self.count)
        self.count-=1
        return 
        
