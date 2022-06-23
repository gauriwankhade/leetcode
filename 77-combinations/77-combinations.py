class Solution(object):
	## Aproach 1 - Backtracking
	def combine(self, n, k):
		# loop over all elements - range(1, n - k + 1)
		# in each iteration find combinations includes - current and length is k

		result = []
		#arr = []
		def backtrack(curr, limit, n, arr):
			if len(arr) == limit:
				result.append(arr.copy())
				return 

			for i in range(curr, n):
				arr.append(i)
				backtrack(i + 1, limit, n, arr)
				arr.pop()

			return result


		return backtrack(1, k, n + 1, [])

