
class Solution(object):
	def subsets(self, nums):
		result = [[]]
		length = len(nums)

		def helper(num, stack):	
			for neighbor in range(num+1, length):
				helper(neighbor, stack + [nums[neighbor]])

			if len(stack) > 1:
				result.append(stack)


		for num in range(length):
			result.append([nums[num]])
			helper(num, [nums[num]])


		return result