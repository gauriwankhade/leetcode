class Solution(object):
    def validPalindrome(self, s):
        start = 0
        end = len(s) - 1
        
        while(start < end):
            if s[start] != s[end]:
                return self.checkPalindrome(s, start + 1, end) or self.checkPalindrome(s, start, end - 1)
            start += 1
            end -= 1
            
        return True
                
        
    def checkPalindrome(self, s, start, end): 
        while(start < end):
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
            
        return True