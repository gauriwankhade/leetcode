class Solution(object):
    def threeSum(self, nums):
        if not nums:
            return

        length = len(nums) - 1
        result = []
        nums = sorted(nums) 

        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left = index + 1
            right = length 

            while(left < right):
                if nums[left] + nums[right] + nums[index] > 0:
                    right -= 1
                elif nums[left] + nums[right] + nums[index] < 0:
                    left += 1
                else:
                    result.append([nums[index], nums[left], nums[right]])
                    left += 1
                    while(left < right and (nums[left - 1] == nums[left])):
                        left += 1

        return result