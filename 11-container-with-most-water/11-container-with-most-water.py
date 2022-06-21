class Solution(object):
	def maxArea(self, height):
		start = 0
		end = len(height) - 1
		maxArea =  min(height[start], height[end]) * (end - start)


		while(start < end):
			if height[start] > height[end]:
				end -= 1
			elif height[end] > height[start]:
				start += 1
			else:
				start += 1

			maxArea = max(maxArea, min(height[start], height[end]) * (end - start))

		return maxArea

