class Solution(object):
    def reverseString(self, s):
        limit = len(s)
        
        for i in range(limit/2):
            s[i],s[limit-1-i] = s[limit-1-i],s[i]
        
        return s
