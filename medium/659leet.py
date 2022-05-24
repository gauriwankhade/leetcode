from collections import Counter, defaultdict

class Solution(object):
	def isPossible(self, nums):
		# Approach-1 ->> 

		# step 1.
		# 	create new subarray with current element as first element 
		# 		if current element is already exists in previous subarray
		# 		if difference between last element of last-added-subarray & current element is greater than 1
		# 			if length of last-added-subarray is less than 3:
		# 				return False
		# step 2.
		# 	else add element to existing subarray
		#
		# step 3.
		# 	check
		# 		if any subarray with length less than 3 found after processing all elements
		# 			return False
		# 		else
		# 			return True


		# Dry run ->>

		# index -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		# nums  -> [1, 2, 3, 3, 4, 4, 5, 5, 7, 7]

		# initial empty sublist
		# sublist = []

		# i  num  sublist 
		# 0  1     [[1]]
		# 1  2     [[1, 2]]
		# 2  3	   [[1, 2, 3]]
		# 3  3     [[3], [1, 2, 3]]
		# 4  4     [[3, 4], [1, 2, 3]]
		# 5  4     [[3, 4], [1, 2, 3, 4]]
		# 6  5     [[3, 4, 5], [1, 2, 3, 4]]
		# 7  5     [[3, 4, 5], [1, 2, 3, 4, 5]]
		# 8  7 	   [[7], [3, 4, 5], [1, 2, 3, 4, 5]]
		# 9  7     [[7], [7], [3, 4, 5], [1, 2, 3, 4, 5]]


		# code ->>

		# subList = [[nums[0], nums[0]]]

		# for num in nums[1: ]:
		# 	flag = 1

		# 	for subArr in subList:
		# 		if num - subArr[-1] == 1:
		# 			subArr[1] = num
		# 			flag = 0
		# 			break

		# 		if num - subArr[-1] > 1:
		# 			if subArr[1] - subArr[0] < 2:
		# 				return False
		# 			else:
		# 				flag = 1
		# 				break						
		# 	if flag:
		# 		subList.insert(0, [num, num])

		
		# for item in subList:
		# 	if item[1] - item[0] < 2:
		# 		return False

		# return True




		# ===========================================================================


		""" Approach-2 ->>

		if subarray exists with last-element < curr-element by 1
			add curr-element to subarray
		else
			if curr-element + 1  and curr-element + 2 exists in nums
				create new subarray
			else
				return False


		Dry run ->>

		index   -> [0, 1, 2, 3, 4, 5, 6, 7]

		nums    -> [1, 2, 3, 3, 4, 4, 5, 5]

		count 	-> {1 : 1, 2: 1, 3: 2, 4: 2, 5: 2}

		lastSub -> {1 : 0, 2: 0, 3: 0, 4: 0, 5: 0} 


		i  num   lastSub                                 count
		0  1     {1 : 0, 2: 0, 3: 1, 4: 0,  5: 0}  		{1 : 0, 2: 0, 3: 1, 4: 2, 5: 2}

		1  2     {1 : 0, 2: 0, 3: 1, 4: 0,  5: 0}  		{1 : 0, 2: 0, 3: 1, 4: 2, 5: 2}

		2  3     {1 : 0, 2: 0, 3: 1, 4: 0,  5: 1} 		{1 : 0, 2: 0, 3: 0, 4: 1, 5: 1}

		3  3     {1 : 0, 2: 0, 3: 1, 4: 0,  5: 1} 		{1 : 0, 2: 0, 3: 0, 4: 1, 5: 1}

		4  4  	 {1 : 0, 2: 0, 3: 0, 4: 1,  5: 1} 		{1 : 0, 2: 0, 3: 0, 4: 1, 5: 1}

		5  4     {1 : 0, 2: 0, 3: 0, 4: 1,  5: 1} 		{1 : 0, 2: 0, 3: 0, 4: 0, 5: 1}

		6  5     {1 : 0, 2: 0, 3: 0, 4: 0,  5: 2}  		{1 : 0, 2: 0, 3: 0, 4: 0, 5: 0}

		7  5     {1 : 0, 2: 0, 3: 0, 4: 0,  5: 2}  		{1 : 0, 2: 0, 3: 0, 4: 0, 5: 0}
		
		""" 


		count = Counter(nums)
		numLen = len(nums)
		lastSub = defaultdict(int)

		for num in nums:
			if not count[num]:
				continue

			# remove element from count after being visited
			count[num] -= 1

			# append to the existing sub list
			if lastSub[num - 1]:
				lastSub[num - 1] -= 1
				lastSub[num] += 1

			# add new sub list
			elif count.get(num + 1) and count.get(num + 2):
				count[num + 1] -= 1
				count[num + 2] -= 1
				lastSub[num + 2] += 1

			else:
				return False

		return True

		

s = Solution()
numlist = \
	[[5,6,7,25,26,27,28,29,30,31,32,32,33,33,34,34,35,35,36,36,37,37,38,38,39,39,40,40,40,41,41,41,42,42,42,43,43,43,44,44,44,45,45,45,46,46,47,47,47,48,48,48,49,49,49,50,50,50,51,51,51,52,52,52,53,53,53,54,54,54,55,55,55,56,56,56,57,57,57,58,58,58,59,59,59,60,60,60,61,61,61,62,62,62,63,63,63,64,64,64,65,65,65,66,66,66,67,67,67,68,68,68,69,69,69,70,70,70,71,71,71,72,72,72,73,73,73,74,74,74,75,75,75,76,76,76,77,77,78,78,79,79,79,79,80,80,80,80,81,81,81,81,82,82,82,82,83,83,83,83,84,84,84,84,85,85,85,85,86,86,86,86,87,87,87,87,88,88,88,88,89,89,89,89,90,90,90,90,91,91,91,91,92,92,92,92,93,93,93,93,93,94,94,94,94,94,95,95,95,95,95,96,96,96,96,96,97,97,97,97,97,98,98,98,98,98,99,99,99,99,99,100,100,100,100,100,101,101,101,101,101,102,102,102,102,102,103,103,103,103,103,104,104,104,104,105,105,105,105,106,106,106,106,107,107,107,107,108,108,108,108,109,109,109,109,110,110,110,110,111,111,111,111,112,112,112,112,113,113,113,114,114,114,115,115,116,116,117,117,118,118,119,120],
	[1],
	[1,2,3,3,4,5],
	[1,2,3,3,4,4,5,5,5,5],
	[1,2,3,4,4,5],
	[1,2,3],
	[1,2,3,5,5,6,7],
	[1,2,5,5,6,6,7,8,8,9]]

counter = 0
for nums in numlist:
	counter += 1
	print(counter, s.isPossible(nums))




		






