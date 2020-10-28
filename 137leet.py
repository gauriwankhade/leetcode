class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while len(nums)>3:
            if nums[i] == nums[i+1] == nums[i+2]:
                nums.pop(i)
                nums.pop(i)
                nums.pop(i)
            else:
                i+=1
        return nums[-1]
            