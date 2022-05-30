from collections import defaultdict

class Solution(object):
	def sortColors(self, nums):
		colorMap = defaultdict(int)

		for key in nums:
			colorMap[key] += 1

		elem = 0
		for index in range(len(nums)):
			if colorMap[0]:
				elem = 0
			elif colorMap[1]:
				elem = 1
			elif colorMap[2]:
				elem = 2 

			nums[index] = elem
			colorMap[elem] -= 1
	