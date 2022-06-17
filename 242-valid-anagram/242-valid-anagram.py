class Solution(object):
    def isAnagram(self, s, t):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        
        length = len(s)
        
        if length != len(t):
            return False
        
        sList = [''] * 26
        tList = [''] * 26
        
        for index in range(length):
            sList[alpha.find(s[index])] += s[index]
            tList[alpha.find(t[index])] += t[index]
            
        if sList == tList:
            return True
            