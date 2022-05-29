
class Solution(object):
	def subsets(self, nums):
		result = [[]]

		for num in nums:
			newRes = []
			for res in result:
				newRes.append(res + [num])
			result.extend(newRes)

		return result
