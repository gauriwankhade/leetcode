"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
    	nodeMap = {}
    	queue = [node]
    	visited = {}
    	current = None

    	if not node:
    		return
    		
    	while(queue):
    		elem = queue.pop(0)
    		if visited.get(elem.val):
    			continue

    		visited[elem.val] = True
    		if not nodeMap.get(elem.val):
    			nodeMap[elem.val] = Node(elem.val)

    		current = nodeMap[elem.val]

    		for neighbor in elem.neighbors:
    			if not nodeMap.get(neighbor.val):
    				nodeMap[neighbor.val] = Node(neighbor.val)

    			current.neighbors.append(nodeMap[neighbor.val])
    			queue.append(neighbor)

    	return nodeMap[node.val]