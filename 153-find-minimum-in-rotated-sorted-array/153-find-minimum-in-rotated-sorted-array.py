class Solution(object):
	def findMin(self, nums):
		mid = low = 0
		high = len(nums) - 1
        

		while(low < high):
			mid = int((low + high) // 2)
			
			if nums[low] < nums[mid] > nums[high]:
				low = mid
				continue
			if nums[low] > nums[mid] < nums[high]:
				high = mid 
				continue
			
			
			return min(nums[high], nums[low])
			

		return nums[mid]