class Solution(object):
   
    def numberOfSubstrings(self, s):
        Map = defaultdict(list)
        ans = 0
        
        for key in s:
            if not Map[key]:
                Map[key] = [1, 1]
            else:
                Map[key][0] += 1
                Map[key][1] = Map[key][0] + Map[key][1] 
            
        
        return sum([Map[i][1] for i in Map])
                
            
        
        