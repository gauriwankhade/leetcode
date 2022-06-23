class Solution(object):
	def permuteUnique(self, nums):
		result = defaultdict(list)
		limit = len(nums)
		visited = defaultdict(bool)

		def backtrack(curr, arr, limit):
			if len(arr) == limit:
				result[tuple(arr)] = arr
				return 

			for i in range(limit):
				if not visited[i]:
					visited[i] = True
					backtrack(i + 1, arr + [nums[i]], limit)
					visited[i] = False

			return result

		return backtrack(0, [], limit).values()
		