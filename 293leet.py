class Solution(object):
    def __init__(self):
        self.result = []
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        limit = len(s)
        for i in range(limit-1):
            if s[i] + s[i+1] == '++':
                try:
                    new = s[0:i] + '--' + s[i+2:]
                except:          	
                    new = s[0:i] + '--'
                self.result.append(new)
        return self.result

                
        
