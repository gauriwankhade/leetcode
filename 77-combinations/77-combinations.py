class Solution(object):
	## Aproach 1 - Backtracking
	def combine(self, n, k):
		result = []
		arr = []
        
		def backtrack(curr, limit, n):
			if len(arr) == limit:
				result.append(arr[0: ])
				return 

			for i in range(curr, n):
				arr.append(i)
				backtrack(i + 1, limit, n)
				arr.pop()

			return result

		return backtrack(1, k, n + 1)

