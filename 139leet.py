#This is recursive solution for the word break problem

class Solution(object):
    def __init__(self):
		self.Dict = []
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.Dict = wordDict
        if self.recursion(s):
            return True
        return False
    
    def recursion(self,part2):
        if part2=='':
          return True
        for i in range(len(part2)):
          part1 = part2[0:i+1]
          if part1 in self.Dict:
            if self.recursion(part2[i+1:]):
              return True
        return False
        
