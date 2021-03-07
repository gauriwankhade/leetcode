#Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
		

class Solution:
	def delNodes(self, root: TreeNode, to_delete):
		self.to_delete = self.listToDict(to_delete)
		self.result = []

		if not self.to_delete.get(root):
			print(',./lko',root)
			self.result.append(root)

		self.traverseNodes(root,parent=None)

		for i in self.result:
			print(i.val)
		return self.result

	def traverseNodes(self,root,parent):
		if not root:
			return

		self.traverseNodes(root.left,root)
		self.traverseNodes(root.right,root)

		if self.to_delete.get(root.val):
			if root.left and root.left.val:
				self.result.append(root.left)
			if root.right and root.right.val:
				self.result.append(root.right)
			if parent:
				if parent.left and parent.left.val == root.val:
					parent.left = None
				elif parent.right and parent.right.val == root.val:
					parent.right = None
		
	def listToDict(self,to_delete):
		Dict = {}
		for i in to_delete:
			Dict[i]=i
		return Dict

root = TreeNode(1)
root.left = TreeNode(2)
root.right= TreeNode(3)
root.left.left = TreeNode(None)
root.left.right = TreeNode(None)
root.right.left = TreeNode(None)
root.right.right = TreeNode(4)

d = [2,1]
s = Solution()
print(s.delNodes(root,d))
		






