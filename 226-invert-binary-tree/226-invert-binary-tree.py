class Solution(object):
    def invertTree(self, root):
        if not root:
            return

        curr = root 
        curr.left, curr.right = self.invertTree(curr.right), self.invertTree(curr.left)
   

        return root