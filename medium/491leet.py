

class Solution(object):
	def findSubsequences(self, nums):
		
		limit = len(nums)
		result = []
		arr = []

		for index in range(len(nums) - 1):
			arr = [[nums[index]]]
			end = index + 1
			PrevLen = arrLen = 1
			while(end < limit):
				i = 0
				arrLen = PrevLen
				while(i < arrLen):
					# print('i- ', i, 'end- ', end, arr)
					if arr[i][-1] <= nums[end] and arr[i] + [nums[end]] not in result:
						arr.append(arr[i] + [nums[end]])
						PrevLen += 1
					i += 1
				end += 1
			arr.remove(arr[0])
			result.extend(arr)
					

		res = set()
		for item in result:
			res.add(tuple(item))

		return [list(k) for k in res]





s = Solution()
nums = [4, 6, 7, 7]
print(sorted(nums))
print(s.findSubsequences(nums))








