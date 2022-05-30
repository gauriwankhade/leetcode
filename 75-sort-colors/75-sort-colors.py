from collections import defaultdict

class Solution(object):
	def sortColors(self, nums):
		colorMap = defaultdict(int)

		for key in nums:
			colorMap[key] += 1

		for index in range(len(nums)):
			if colorMap[0]:
				nums[index] = 0
				colorMap[0] -= 1
			elif colorMap[1]:
				nums[index] = 1
				colorMap[1] -= 1
			elif colorMap[2]:
				nums[index] = 2
				colorMap[2] -= 1


		

