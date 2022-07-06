class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        Map = defaultdict(int)
        
        for edge in edges:
            if Map[edge[0]]:
                return edge[0]
            if Map[edge[1]]:
                return edge[1]
            
            Map[edge[0]] = True
            Map[edge[1]] = True
            
            
        