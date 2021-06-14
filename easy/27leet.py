class Solution(object):
    # def removeElement(self, nums, val):
    #     count = 0
    #     while(count < len(nums)):
    #         if nums[count] == val :
    #             nums.pop(count)
    #         else:
    #             count += 1
    #     return count, nums


    def removeElement(self, nums, val):

        n = len(nums)
        last = n - 1
        count = 0

        for i in range(n) :
            if last == i :
                break

            if nums[i] == val:
                if nums[last] == val:
                    last-=1
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
                count += 1

        print(count, last, n)
        if count >= n:
            return last
        
        return last+1

        

s = Solution()
nums = [0,0]
val = 0
print(s.removeElement(nums, val))