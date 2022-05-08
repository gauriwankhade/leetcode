#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def verticalOrder(self, root):
       sequence = 0
       result = {}
       self.maxSequence = 0
       self.bfs(root, result)
       result = self.formatResult(result)
       return result


    def formatResult(self, result):
        counter = self.maxSequence
        newResult = []
        while(True):
            try:
                newResult.append(result[counter])
            except:
                break
            counter -= 1

        return newResult

    def bfs(self, root, result):
        queue = [(root, 0)]

        while(queue):
            ele = queue.pop(0)
            self.maxSequence = max(self.maxSequence, ele[1])
            try:
                result[ele[1]] += [ele[0].val]
            except:
                result[ele[1]] = [ele[0].val]

            print(ele[0].val)
            if ele[0].left:
                queue.append((ele[0].left, ele[1] + 1))
            if ele[0].right:
                queue.append((ele[0].right, ele[1] - 1))

           
        return result





s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(8)
root.left.left = TreeNode(4)
root.left.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(7)
# root.left.left.left = TreeNode(13)
# root.left.left.left.right = TreeNode(10)
# root.right.left.right = TreeNode(16)
# root.right.right.right = TreeNode(12)
root.left.right.right = TreeNode(2)
root.right.left.left = TreeNode(5)

print(s.verticalOrder(root))
#print(s.bfs(root))



