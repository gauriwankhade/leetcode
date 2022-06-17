class Solution(object):
    def isAnagram(self, s, t):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        length = len(s)
        
        if length != len(t):
            return
        
        for char in alpha:
            if s.count(char) != t.count(char):
                return False
        
        return True
        
        
            