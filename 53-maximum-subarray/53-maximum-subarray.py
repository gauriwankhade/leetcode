class Solution(object):
	def maxSubArray(self, nums):
		maxCount = lastSum  = nums[0]

		for num in range(1, len(nums)):
			if lastSum >= 0:
				lastSum += nums[num]
			else:
				lastSum = nums[num] 


			maxCount = max(maxCount, lastSum)

		return maxCount