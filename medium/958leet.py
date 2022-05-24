import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isCompleteTree(self, root):
        Que = collections.deque([root])
        incomplete = False

        while(Que):
            elem = Que.popleft()

            if elem and incomplete:
                return False
            if elem:
                Que.append(elem.left)
                Que.append(elem.right)
            elif not elem:
                incomplete = True
            

            
        return True




s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(s.isCompleteTree(root))
