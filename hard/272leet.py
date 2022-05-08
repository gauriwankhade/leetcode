import math
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def closestKValues(self, root, target, k):
        self.diffList = []
        self.sortedNums = []
        self.traverseBST(root, target)
        maxArr = self.sortedNums[0:k]
        prevArr = self.sortedNums[0:k]
        maxDiff = prevDiff = sum(self.diffList[0:k])
        counter = 0

        for i in range(1, len(self.sortedNums)) :
            print(prevArr, prevDiff, maxArr, maxDiff, 'i- ', i, 'counter- ', counter)
            if k + i > len(self.sortedNums):
                break
            currArr = self.sortedNums[counter + 1: k + i]
            currDiff = prevDiff - self.diffList[counter] + self.diffList[i + k - 1]
            if currDiff < prevDiff :
                maxArr = currArr
                maxDiff = currDiff
            prevArr = currArr
            prevDiff = currDiff
            counter += 1
        
        return maxArr
    
    
    def traverseBST(self, curr, target):
        if not curr:
            return
        left = self.traverseBST(curr.left, target)
        self.sortedNums.append(curr.val)
        self.diffList.append(abs(curr.val - target))
        right = self.traverseBST(curr.right, target)
        
       



s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
# root.right = TreeNode(15)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(16)

print(s.closestKValues(root, 6.123, 1))
        
        