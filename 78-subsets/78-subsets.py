
class Solution(object):
	def helper(self, num, stack):
		
		for neighbor in range(num+1, self.length):
			self.helper(neighbor, stack + [self.nums[neighbor]])

		if len(stack) > 1:
			self.result.append(stack)



	def subsets(self, nums):
		self.graph = {}
		self.result = [[]]
		self.length = len(nums)
		self.nums = nums
		# for i in range(len(nums)):
		# 	for j in range(i + 1, len(nums)):
		# 		if not self.graph.get(nums[i]):
		# 			self.graph[nums[i]] = [nums[j]]
		# 		else:
		# 			self.graph[nums[i]].append(nums[j])


		for num in range(self.length):
			self.result.append([nums[num]])
			self.helper(num, [nums[num]])


		return self.result