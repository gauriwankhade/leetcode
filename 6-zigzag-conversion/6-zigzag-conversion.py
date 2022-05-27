class Solution(object):
    def convert(self, s, numRows):
        result = ["" for i in range(numRows)]
        start, add, ans = 0, 1, ''

        def reverseDirection(add, start):
	        if add:
	            start += 1
	        else:
	            start -= 1

	        return start


        for char in s:
            if start >= numRows - 1:
                add = 0
            
            elif start <= 0:
                add = 1

            result[start] += char
            start = reverseDirection(add, start)
            
        
        for item in result:
            ans += item
            
        return ans