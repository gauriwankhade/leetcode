class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        
        r = S.replace('-','').upper()[::-1]
        count = 0
        ans = ''

        for i in r:
            if count>=K:
                ans+= '-'
                ans+= i
                count = 1
            else:
                ans+=i
                count+=1
                
        return ans[::-1]

