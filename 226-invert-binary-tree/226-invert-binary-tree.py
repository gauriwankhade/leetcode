class Solution(object):
    def invertTree(self, root):
        if not root:
            return

        def helper(curr):
            if not curr:
                return

            temp = curr.left
            curr.left = curr.right
            curr.right = temp

            helper(curr.left)
            helper(curr.right)

        helper(root)

        return root