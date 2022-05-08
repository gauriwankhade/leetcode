
## Approach 1

# class Solution(object):
#     def firstMissingPositive(self, nums):
#         numsLen = len(nums)
#         ans = 1

#         for item in nums:
#             num = item
#             if type(item) == str:
#                 num = int(item.split(',')[0])
#             if (0 < num <= numsLen) and type(nums[num - 1]) == int:
#                 nums[num - 1] = str(nums[num - 1]) + ',' + str(num)

          

#         for num in nums:
#             if type(num) == str:
#                 if int(num.split(',')[1]) == ans:
#                     ans+= 1
#         return ans



## Approach 2

class Solution(object):
    def firstMissingPositive(self, nums):
        numsLen = len(nums)
        ans = 1
        check = None

        for idx in range(numsLen):
            if nums[idx] == 1:
                check = True
            if nums[idx] > numsLen or nums[idx] <= 0:
               nums[idx] = 1


        if not check:
            return 1
        
        for item in nums:
            if nums[abs(item) - 1] > 0:
                nums[abs(item) - 1] = -1 * nums[abs(item) - 1]
                print('item -', item, nums[item - 1], nums)
        print('nums 2:- ', nums)

        for i in nums:
            if i < 0:
                ans += 1
            else:
                break

        return nums, ans


s = Solution()
nums = [3,4,-1,1]
print('initial-', nums)
print(s.firstMissingPositive(nums))










