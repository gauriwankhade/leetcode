class Solution(object):
	def maxSubArray(self, nums):
		maxCount = lastSum  = nums[0]

		for num in nums[1: ]:
			if lastSum >= 0:
				lastSum += num
			else:
				lastSum = num 


			maxCount = max(maxCount, lastSum)

		return maxCount