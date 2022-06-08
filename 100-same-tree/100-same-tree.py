# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        pArr, qArr = [], []

        def helper(curr, arr):
            if not curr:
                arr.append(None)
                return

            arr.append(curr.val)

            helper(curr.left, arr)
            helper(curr.right, arr)

        helper(p, pArr)
        helper(q, qArr)

        return pArr == qArr
           