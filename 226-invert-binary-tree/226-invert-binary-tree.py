class Solution(object):
    def invertTree(self, root):
        if not root:
            return

        def swapNodes(curr):
            if not curr:
                return
           
            curr.left, curr.right = curr.right, curr.left
            
            swapNodes(curr.left)
            swapNodes(curr.right)

        swapNodes(root)

        return root