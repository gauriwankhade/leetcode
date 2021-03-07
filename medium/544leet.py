

class Solution(object):
	def findContestMatch(self, n):
		result = [i for i in range(1,n+1)]

		while(n>1):	
			n = int(n/2)
			for k in range(n):
				s= result.pop()
				result[k] = '('+ str(result[k]) + ',' + str(s) + ')'
		return result[0]

s = Solution()
print(s.findContestMatch(8))
