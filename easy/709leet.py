import string

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """      
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase

        for i in range(len(str)):
            if str[i].isupper():
                ind = upper.index(str[i])
                str = str[0:i] + lower[ind] +str[i+1:]
                

        return str

s = Solution()
print(s.toLowerCase(input()))
                
                
           