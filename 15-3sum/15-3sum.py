class Solution(object):
     def threeSum(self, nums):

        length = len(nums) 
        result = []
        nums = sorted(nums)

        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            left = index + 1
            right = length - 1

            while(left < right):
                if nums[left] + nums[right] > -nums[index]:
                    right -= 1
                elif nums[left] + nums[right] < -nums[index]:
                    left += 1
                else:
                    if not result or result[-1] != [nums[index], nums[left], nums[right]]:
                        result.append([nums[index], nums[left], nums[right]])
                    left += 1

        return result