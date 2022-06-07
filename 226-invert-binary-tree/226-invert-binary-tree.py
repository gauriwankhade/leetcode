class Solution(object):
    def invertTree(self, root):
        if not root:
            return

#         def swapNodes(curr):
#             if not curr:
#                 return
        curr = root 
        curr.left, curr.right = self.invertTree(curr.right), self.invertTree(curr.left)
   
        # swapNodes(root)

        return root