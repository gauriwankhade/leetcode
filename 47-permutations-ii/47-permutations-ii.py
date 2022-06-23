class Solution(object):
	def permuteUnique(self, nums):
		result = defaultdict(list)
		limit = len(nums)
		visited = {}

		def backtrack(curr, arr, limit):
			if len(arr) == limit:
				result[tuple(arr)] = arr
				return result

			for i in range(limit):
				if not visited.get(i):
					visited[i] = True
					backtrack(i + 1, arr + [nums[i]], limit)
					visited[i] = False

			return result

		return backtrack(0, [], limit).values()
		
