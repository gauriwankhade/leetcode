# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        self.sub = []

        def isSameTree(p, q):
            if not p and not q:
                return True
            if (p and not q) or (q and (not p)):
                return False

            if p.val == q.val:
                if isSameTree(p.left, q.left) and isSameTree(p.right, q.right):
                    return True

        def findSubRoot(curr, sub):
            if not curr:
                return

            if curr.val == sub.val:
                self.sub.append(curr)

            findSubRoot(curr.left, sub)
            findSubRoot(curr.right, sub)

        findSubRoot(root, subRoot)

        for node in self.sub:
            if isSameTree(node, subRoot):
                return True