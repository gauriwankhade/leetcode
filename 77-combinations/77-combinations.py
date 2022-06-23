class Solution(object):
    
    def combine(self, n, k):
		# loop over all elements - range(1, n - k + 1)
		# in each iteration find combinations includes - current and length is k

		result = []
		def backtrack(curr, arr, limit, n, currLen):
			if currLen == limit:
				result.append(arr)
				return

			for i in range(curr, n):
				backtrack(i + 1, arr + [i], limit, n, currLen + 1)

			return result
    
		return backtrack(1, [], k, n + 1, 0)

		#return result


        
       