class Solution(object):
    def convert(self, s, numRows):
        result = ["" for i in range(numRows)]
        start = 0
        flag = 1
        ans = ''

        def reverse(flag, start):
	        if flag:
	            start += 1
	        else:
	            start -= 1

	        return start


        for char in s:
            if start >= numRows - 1:
                flag = 0
            
            elif start <= 0:
                flag = 1

            result[start] += char
            start = reverse(flag, start)
            
        
        for item in result:
            ans += item
            
        return ans