class Solution(object):
	def longestConsecutive(self, nums):
		visited = {}
		maxCount = 0

		for key in nums:
			visited[key] = 0


		def helper(num, count):
			if num not in visited or visited.get(num) > 0:
				return count

			visited[num] += 1
			count += 1

			count = helper(num - 1, count)
			count = helper(num + 1, count)

			return count



		for num in nums:
			count = helper(num, 0)
			maxCount = max(count, maxCount)

		
		return maxCount