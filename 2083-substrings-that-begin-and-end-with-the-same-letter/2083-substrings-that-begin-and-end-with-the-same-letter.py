class Solution(object):
   
    def numberOfSubstrings(self, s):
        Map = Counter(s)
        ans = len(s)
        
        for key in Map:
            val = Map[key]
            ans += ((val * (val - 1)) / 2)
                 
        return ans
                
            
        
        