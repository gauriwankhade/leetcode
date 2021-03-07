class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
	def pruneTree(self,curr):
		if curr == None:
			return None

		curr.left= self.pruneTree(curr.left)
		curr.right= self.pruneTree(curr.right)

	
		if curr.val == 0 and curr.left==None and curr.right==None:
			curr = None

		return curr	
		
	
#sample test
s = Solution()
root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)
root.left.left.left = TreeNode(0)

s.pruneTree(root)



