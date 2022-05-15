

class Solution(object):
	def canJump(self, nums):
		limit = len(nums) - 1
		lastElem = 0
		for elem in range(limit + 1):
			if lastElem >= elem :
				lastElem = max(lastElem, nums[elem] + elem)
			if lastElem >= limit:
				return True
			

		return False


s = Solution()
nums = [0, 2, 3]
print(s.canJump(nums))




