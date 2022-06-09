# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        self.ans = False
        
        def isSameTree(p, q):
            if not p and not q:
                return True

            if p and q and p.val == q.val:
                return(isSameTree(p.left, q.left) and isSameTree(p.right, q.right))
                    

        def findSubRoot(curr, sub):
            if not curr:
                return
           
            findSubRoot(curr.left, sub)
            findSubRoot(curr.right, sub)
            
            if curr.val == sub.val and isSameTree(curr, sub):
                self.ans = True
                
            return self.ans

        return findSubRoot(root, subRoot)

