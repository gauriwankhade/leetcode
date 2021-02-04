class Solution(object):
    def findTheDifference(self, s, t):
        
        l1 = len(s)
        l2 = len(t)
        
        t=sm_str = sorted(t)
        s=lg_str = sorted(s)
        
        if l1<l2:  
            sm_str = s
            lg_str = t
          
        for i in range(min(l1,l2)):
            if sm_str[i]!=lg_str[i]:
                return lg_str[i]
       
        return lg_str[-1]
    
