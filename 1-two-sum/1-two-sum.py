class Solution(object):
    def twoSum(self, nums, target):
        Map = {}
        
        for num in range(len(nums)):    
            if target - nums[num] in Map:
                return [num,  Map[target - nums[num]]]
            
            Map[nums[num]] = num
            
       
                
        
        