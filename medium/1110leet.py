
class node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
	def delNodes(self,root,to_delete):
		
		self.to_delete = self.list_to_dict(to_delete)
		self.result = [root]
		
		#if root to be deleted
		exception = self.check_exception(root)

		while self.to_delete:
			self.recursion(self.result[0])

		#delete root node from result array
		if exception:
			self.result.pop(0)

		return self.result
		
	def recursion(self,root):
		if not root :
			return

		#postorder traversal
		root.left = self.recursion(root.left)
		root.right = self.recursion(root.right)

		try:
			#check condition, current node value present in to_delete dictionary
			self.to_delete[root.val]

			#add left and right nodes to the result array as seperate roots
			if root.left :
				self.result.append(root.left)
								
			if root.right :
				self.result.append(root.right)
				
			self.to_delete.pop(root.val)
			return None

		except:
			pass

		return root

	
	def list_to_dict(self,to_delete):
		Dict = {}
		for i in to_delete:
			Dict[i]=i
		return Dict

	def check_exception(self,root):
		try:
			self.to_delete[root.val]
			return True
		except:
			return False

        
root = node(1)
root.left = node(2)
root.right= node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

d = [1,6]
s = Solution()
print(s.delNodes(root,d))
		
