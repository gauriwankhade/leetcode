
class Solution(object):
	def helper(self, num, stack):
		if self.graph.get(num):
			for neighbor in self.graph[num]:
				self.helper(neighbor, stack + [neighbor])

		if len(stack) > 1:
			self.result.append(stack)



	def subsets(self, nums):
		self.graph = {}
		self.result = [[]]
		for i in range(len(nums)):
			for j in range(i + 1, len(nums)):
				if not self.graph.get(nums[i]):
					self.graph[nums[i]] = [nums[j]]
				else:
					self.graph[nums[i]].append(nums[j])


		for num in nums:
			self.result.append([num])
			self.helper(num, [num])


		return self.result