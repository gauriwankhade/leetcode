import time
import gc

t1 = time.time()
class Solution(object):

	def cleanNums(self, nums):
		nums = sorted(nums)
		newList = []
		counter = 0
		prev = nums[0]

		for i in range(len(nums)):
			if prev != nums[i]:
				counter = 0
			if prev == nums[i]:
				counter += 1
			if counter < 5:
				newList.append(nums[i])
			prev = nums[i]
			
		return newList


	def fourSum(self, nums, target):
		hashmap = {}
		result = []
		count2 = count = 0
		seen = {}

		nums = self.cleanNums(nums)
		length = len(nums)

		for i in range(length):
			for j in range(i+1, length):
				count += 1
				if hashmap.get(nums[i] + nums[j]):
					hashmap[nums[i] + nums[j]].append([i, j])
				else:
					hashmap[nums[i] + nums[j]] = [[i, j]]

	

		for key in hashmap:
			val1 = hashmap.get(key)
			val2 = hashmap.get(target - key)
			if val1 and val2 :
				for p in val1:
					for q in val2:
						count2 += 1 
						if len(set(p+q)) == 4 :
							result.append(p + q)

				hashmap[key] = None

			


		Nresult = []
		for item in result:
			arr = sorted([nums[item[0]], nums[item[1]], nums[item[2]], nums[item[3]]])
			if not seen.get(str(arr)):
				seen[str(arr)] = True
				Nresult.append(arr)


		t2 = time.time()
		return  Nresult, t2 - t1, f'count - {count}, count2 - {count2}'


s = Solution()
nums = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]
print(s.fourSum(nums, 200))













