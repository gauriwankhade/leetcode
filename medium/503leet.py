

# class Solution(object):
# 	def nextGreaterElements(self, nums):
# 		length = len(nums)
# 		counter = 0
# 		ans = [-1] * length

# 		for index in range(length):
# 			curr = nums[index]
# 			start = (index + 1) % length
			
# 			while(start != index):
# 				if nums[start] > nums[index]:
# 					ans[index] = nums[start]
# 					break
# 				start = (start + 1) % length


# 		return ans




class Solution(object):
	def nextGreaterElements(self, nums):
		length = len(nums)
		counter = 0
		ans = [-1] * length
		print(nums)
		for index in range(length):
			left = 0
			right = length - 1
			
			while(True):
				print(ans, left, right, index)
				if (right <= index) and (left >= index):
					break
				if left < index and (nums[left] > nums[index]):
					ans[index] = nums[left]
					print(f'updated left- for {index}\n', ans[index])
				if right > index and (nums[right] > nums[index]):
					ans[index] = nums[right]
					print(f'updated right- for {index}\n', ans[index])
				
				if right > index:
					right -= 1
				
				if left < index:
					left += 1 
				


		return ans





s = Solution()
nums = [5,4,3,2,1]
print(s.nextGreaterElements(nums))


# [0        3        6]
# [1, 2, 2, 4, 3, 1, 5]

# [(1, 0), (1, 5), (2, 1), (2, 2), (3, 4), (4, 3), (5, 6)]

# [(1, 0),
# (2, 1),
# (2, 2),
# (4, 3),
# (3, 4),
# (1, 5),
# (5, 6)]

[(1, 0), (1, 4), (2, 3), (2, 5), (3, 2), (4, 1)]

 0, 1, 2, 3, 4, 5
[1, 4, 3, 2, 1, 2]




















