class Solution(object):
	def permuteUnique(self, nums):
		result = defaultdict(list)
		visited = defaultdict(bool)

		def backtrack(curr, arr):
			if len(arr) == len(nums):
				result[tuple(arr)] = arr
				return 

			for i in range(len(nums)):
				if not visited[i]:
					visited[i] = True
					backtrack(i + 1, arr + [nums[i]])
					visited[i] = False

			return result

		return backtrack(0, []).values()
		