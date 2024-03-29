# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def verticalOrder(self, root):
        Map = defaultdict(list)
        
        
        queue = [(root, 0)]
        firstCol = float('inf')
        
        while(queue):
            elem = queue.pop(0)
            if elem[0]:
                Map[elem[1]].append(elem[0].val)
                queue.append((elem[0].left, elem[1] - 1))
                queue.append((elem[0].right, elem[1] + 1))
                
                firstCol = min(firstCol, elem[1])
                
        res = []
       
        while(Map[firstCol]):
            res.append(Map[firstCol])
            firstCol += 1
                             
        return res
            
            
     