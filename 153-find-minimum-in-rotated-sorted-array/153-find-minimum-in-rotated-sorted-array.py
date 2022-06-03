class Solution(object):
	def findMin(self, nums):
		mid = low = 0
		high = len(nums) - 1
        

		while(low < high):
			mid = int((low + high) // 2)

			

			if nums[low] < nums[mid] > nums[high]:
				low = mid 
			elif nums[low] > nums[mid] < nums[high]:
				high = mid 
			elif nums[low] >= nums[mid] >= nums[high]:
				return nums[high]
			elif nums[low] <= nums[mid] <= nums[high]:
				return nums[low]
			



		return nums[mid]