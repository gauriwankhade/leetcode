# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
       

        def isSameTree(p, q):
            if not p and not q:
                return True
            if (p and not q) or (q and (not p)):
                return False

            if p.val == q.val:
                if isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
                    return True

        def findSubRoot(curr, sub, ans):
            if not curr:
                return ans

           
            ans = findSubRoot(curr.left, sub, ans)
            ans = findSubRoot(curr.right, sub, ans)
            
            if curr.val == sub.val and isSameTree(curr, sub):
                ans = True
                
            return ans

        return findSubRoot(root, subRoot, False)

        #return self.ans