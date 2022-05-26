class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ans = []
        numLen = len(nums) 
        
        for index in range(numLen):
            newInd = abs(nums[index]) - 1 
            if nums[newInd] < 0:
                ans.append(newInd + 1)
            else:
            	nums[newInd] =  - nums[newInd] 
        
        
        return ans
    
    

        
        
        
    
    