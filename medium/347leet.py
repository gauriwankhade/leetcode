

class Solution(object):
    def topKFrequent(self, nums, k):
        numMap = {}
        maxIndex = 0

        for num in nums:
            key = numMap.get(num)
            if not key:
                numMap[num] = 1
            else:
                numMap[num] += 1

            maxIndex = max(maxIndex, numMap[num])

        Arr = [None] * (maxIndex + 1)
        for key in numMap:
        	if not Arr[numMap[key]]:
        		Arr[numMap[key]] =  [1, key]
        	else:
        		Arr[numMap[key]].append(key)
        		Arr[numMap[key]][0] += 1

        result = []
        for i in Arr[::-1]:
        	if i:
        		result = result + i[1:]
        	if i  and i[0] >= k:
        		break




        return result[0: k]

s = Solution()
nums = [1,1,1,2,2,3, 4, 4, 4, 4, 2, 5, 9, 1, 2, 9, 5]
print(s.topKFrequent(nums, 4))
