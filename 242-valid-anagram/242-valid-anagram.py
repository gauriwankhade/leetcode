class Solution(object):
    def isAnagram(self, s, t):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        s = sorted(s)
        t = sorted(t)
        length = len(s)
        
        if length != len(t):
            return
        
        for idx in range(length):
            if s[idx] != t[idx]:
                return False
        
        return True
        
        
            