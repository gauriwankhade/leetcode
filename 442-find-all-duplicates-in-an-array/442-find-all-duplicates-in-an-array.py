class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        numLen = len(nums) 
        
        for index in range(numLen):
            if nums[abs(nums[index]) - 1] < 0:
            	ans.append(abs(nums[index]))
            elif nums[abs(nums[index]) - 1] > 0:
            	nums[abs(nums[index]) - 1] =  -1 * nums[abs(nums[index]) - 1] 
        
        
        return ans