# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        stack = [root]
        self.count = 0
        self.targetSum = targetSum

        while(stack):
            top = stack.pop()
            
            if top:
                stack.insert(0, top.left)
                stack.insert(0, top.right)
            self.traverseTree(top, 0)


        return self.count



    def traverseTree(self, curr, summ):
        if not curr:
            return

        
        summ += curr.val

        if summ == self.targetSum:
            self.count += 1

        self.traverseTree(curr.left, summ)
        self.traverseTree(curr.right, summ)
