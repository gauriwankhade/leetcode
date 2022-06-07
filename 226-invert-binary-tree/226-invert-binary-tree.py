class Solution(object):
    def invertTree(self, root):
        if not root:
            return

        def helper(curr):
            if not curr:
                return

           
            curr.left, curr.right = curr.right, curr.left
            

            helper(curr.left)
            helper(curr.right)

        helper(root)

        return root