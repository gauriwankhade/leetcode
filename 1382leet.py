
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def __init__(self):
        self.array = []
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        self.BST_to_SortedArray(root)
        
        start =  0
        end = len(self.array)-1
       
        return self.SortedArray_to_AVL(start,end)
            
           
    def BST_to_SortedArray(self,root) :
        if root == None:
            return
        
        self.BST_to_SortedArray(root.left)
        self.array.append(root.val)
        self.BST_to_SortedArray(root.right)
    
    def SortedArray_to_AVL(self,start,end):
        if start > end :
            return
        mid = (start + end)/2
        n= self.array[mid]
        n= TreeNode(n)
        
        n.left = self.SortedArray_to_AVL(start,mid-1)
        n.right = self.SortedArray_to_AVL(mid+1,end)
        
        return n
        
        
        
        
        
        
        
        
        