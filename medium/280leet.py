class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()

        for i in range(len(nums)-1):
        	if i%2 == 1:
        		nums[i],nums[i+1] = nums[i+1],nums[i]
        return nums


s = Solution()
nums = [3,5,2,1,6,4,7]
s.wiggleSort(nums)