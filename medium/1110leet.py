
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
	def delNodes(self, root: TreeNode, to_delete):
		queue = [root]
		result = []
		to_delete = self.listToDict(to_delete)
		parent = {root:None}

		
		while(queue):
			current = queue[0]
			if current:
				left  = None
				right = None
				
				if current.left:
					left = current.left
					parent[left] = current
					
	
				if current.right:
					right = current.right
					parent[right] = current

				queue.append(left)
				queue.append(right)

				if to_delete.get(current.val):
					p = parent.get(current)

					if queue[-1] and (not to_delete.get(queue[-1].val)) and queue[-1].val:
						#print('added to result: ',queue[-1].val)
						result.append(queue[-1])
					if queue[-2] and (not to_delete.get(queue[-2].val)) and queue[-2].val:
						#print('added to result: ',queue[-2].val)
						result.append(queue[-2])
					if p:
						if p.left and (p.left.val == current.val):
							p.left = None
						elif p.right and (p.right.val == current.val):
							p.right = None

						
			queue.pop(0)
			
		if not to_delete.get(root.val):
			result.append(root)

		for k in result:
			print(k.val)

		return result


	def listToDict(self,to_delete):
		Dict = {}
		for i in to_delete:
			Dict[i]=i
		return Dict

	# def printTree(self,root):
	# 	if not root:
	# 		return
	# 	print(root.val)
	# 	self.printTree(root.left)
	# 	self.printTree(root.right)


        
root = TreeNode(1)
root.left = TreeNode(2)
root.right= TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

d = [3,5]
s = Solution()
print(s.delNodes(root,d))





