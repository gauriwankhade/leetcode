class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        
        result = ["" for i in range(numRows)]
        start = 0
        flag = 1
        ans = ''

        for char in s:
            #print(char, start, flag)
            if start >= numRows - 1:
                flag = 0
            
            elif start <= 0:
                flag = 1

            result[start] += char
            start = self.reverse(flag, start)
            
        
        for item in result:
            ans += item
            
            
        return ans



    def reverse(self, flag, start):
        if flag:
            start += 1
        else:
            start -= 1

        return start

