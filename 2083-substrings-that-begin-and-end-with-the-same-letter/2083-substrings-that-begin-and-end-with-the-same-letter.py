class Solution(object):
   
    def numberOfSubstrings(self, s):
        Map = Counter(s)
        ans = len(s)
        
        for key in Map:
            ans += ((Map[key] * (Map[key] - 1)) / 2)
                 
        return ans
                
            
        
        