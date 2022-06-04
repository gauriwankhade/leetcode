class Solution(object):
	def longestConsecutive(self, nums):
		visited = {}
		maxCount = 0	

		for key in nums:
			visited[key] = 0

		for num in nums:
			if not visited[num]:
				stack = [num]
				count = 1

				while(stack):
					top = stack.pop()
					visited[top] += 1

					if top - 1 in visited and not visited[top - 1]:
						stack.append(top - 1)
						count += 1
					if top + 1 in visited and not visited[top + 1]:
						stack.append(top + 1)
						count += 1
				maxCount = max(count, maxCount)

		
		return maxCount