

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverFromPreorder(self, traversal):
        """
        As, given input traversal is in the form of string. To process data we need to
        seperate out numbers and dashes.

        maintain hashmap for each node and dashes.
        key - TreeNode object, value - number of dashes in front of respective number

        Ex. traversal =  "1--3---4" 
            treeMap = {TreeNode(1):0, TreeNode(3): 2, TreeNode(4): 3}
        """

        treeMap = {}
        traversal = traversal + '-'
        num = dash = ''
        stack = []

        #loop through traversal to fill up treeMap
        for idx in range(len(traversal)):
            if traversal[idx] == '-':
                dash += '-'
            if traversal[idx].isnumeric():
                num += traversal[idx]
            if traversal[idx].isnumeric() and traversal[idx + 1] == '-':
                intNum = int(num)
                node = TreeNode(intNum)
                treeMap[node] = len(dash)
                num = dash = ''


                # use stack to create tree
                if not stack:
                    stack.append(node)
                else:
                    while(treeMap[stack[-1]] >= treeMap[node]):
                        stack.pop() 
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                    stack.append(node)

        return stack[0]

    
    

        
s = Solution()
print(s.recoverFromPreorder("1-2--3--4-5--6--7"))

        