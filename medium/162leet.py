class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        numLen = len(nums) - 1
        left = 0
        right = numLen
        
        if numLen <3:
            return nums.index(max(nums))
        
        while(left<=right):
            mid = (left + right)/2
            if (0 >= mid) :
                return mid + 1 if nums[mid + 1] > nums[mid] else mid
            if mid >= numLen :
                return mid - 1 if nums[mid - 1] > nums[mid] else mid
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                result = mid
                break
            if nums[mid - 1] > nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
                
        return mid
                
        