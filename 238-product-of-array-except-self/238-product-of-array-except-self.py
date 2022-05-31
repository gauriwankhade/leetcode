class Solution(object):
    def productExceptSelf(self, nums):
        posProd = 1
        zeroCount = 0
        
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                posProd *= num
                
        
        for index in range(len(nums)):
            if zeroCount > 1:
                return [0] * len(nums)
            if nums[index] == 0:
                nums[index] = posProd
            else:
                nums[index] = posProd * (zeroCount == 0) // nums[index]
                
        return nums
                
                
                
                
            