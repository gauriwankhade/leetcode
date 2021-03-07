class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
	def __init__(self):
		self.visited = {}

	def correctBinaryTree(self, root):
		if not root:
			return
		if root.right and self.visited.get(root.right.val):
			return None
		self.visited[root.val] = root.val
		root.right = self.correctBinaryTree(root.right)
		root.left = self.correctBinaryTree(root.left)

		return root


