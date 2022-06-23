class Solution(object):
	def permuteUnique(self, nums):
		result = set()
		limit = len(nums)
		visited = {}
		
		def backtrack(curr, arr, limit):
			if len(arr) == limit:
				result.add(tuple(arr))
				return result

			for i in range(limit):
				if not visited.get(i):
					visited[i] = True
					backtrack(i + 1, arr + [nums[i]], limit)
					visited[i] = False

		backtrack(0, [], limit)
		return [list(tup) for tup in result]
