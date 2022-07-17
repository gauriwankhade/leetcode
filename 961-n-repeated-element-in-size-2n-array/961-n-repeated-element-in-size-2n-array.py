class Solution(object):
    def repeatedNTimes(self, nums):
        start = 0
        end = len(nums) - 1
        
        while(start < end):
            if start + 1 < end and nums[start + 1] in [nums[start], nums[end]]:
                return nums[start + 1]
            if end - 1 > start and nums[end - 1] in [nums[start], nums[end]]:
                return nums[end - 1]
            if nums[start] == nums[end]:
                return nums[start]
            
            start += 1
            end -= 1
            
            
            
        