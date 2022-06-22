class Solution(object):
    def threeSum(self, nums):
        result = set()

        if not nums:
            return

        def removeDuplicates(nums):
            nums = sorted(nums)
            newNums = [nums[0]]
            count = 1

            for num in nums[1: ]:
                if newNums[-1] == num and count >= 3:
                    continue
                if newNums[-1] != num :
                    newNums.append(num)
                    count = 1
                else:
                    newNums.append(num)
                    count += 1

            return newNums
        nums = removeDuplicates(nums)
        
        numMap = {}
        for idx in range(len(nums)):
            numMap[nums[idx]] = idx + 1

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                thirdNum = numMap.get(- (nums[i] + nums[j]))
                if thirdNum and (thirdNum - 1 not in [i, j]):
                    result.add((- (nums[i] + nums[j]), nums[i], nums[j]))

      
        finalRes = {}

        for res in result:
            finalRes[tuple(sorted(res))] = list(res)

        return finalRes.values()