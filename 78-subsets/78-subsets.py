
class Solution(object):
	def subsets(self, nums):
		result = [[]]
		length = len(nums)

		def helper(num, curr):	
			for neighbor in range(num+1, length):
				helper(neighbor, curr + [nums[neighbor]])

			if len(curr) > 1:
				result.append(curr)


		for num in range(length):
			result.append([nums[num]])
			helper(num, [nums[num]])


		return result