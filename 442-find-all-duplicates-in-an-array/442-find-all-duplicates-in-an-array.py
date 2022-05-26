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
            elif nums[newInd] > 0:
            	nums[newInd] =  -1 * nums[newInd] 
        
        
        return ans
    
    

        
        
        
    
    