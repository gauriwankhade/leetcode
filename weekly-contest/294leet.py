

# class Solution(object):
# 	def percentageLetter(self, s, letter):
# 		count = 0
# 		for i in s:
# 			if i == letter:
# 				count += 1

# 		return int((count / len(s)) * 100)



# sol = Solution()
# s = "foobar"
# letter = "o"
# print(sol.percentageLetter(s, letter))
#       



#*************************** problem 2 *********************************


# class Solution(object):
# 	def maximumBags(self, capacity, rocks, additionalRocks):
# 		arr = []
# 		ans = 0

# 		for index in range(len(capacity)):
# 			arr.append((index, capacity[index] - rocks[index]))

# 		arr.sort(key = lambda x:x[1])

# 		for i in range(len(capacity)):
# 			if arr[i] == 0:
# 				ans += 1
# 				continue

# 			if additionalRocks <= 0:
# 				return ans
			
# 			if additionalRocks >= arr[i][1]:
# 				additionalRocks -= arr[i][1]
# 				ans += 1


# 		return ans


# s = Solution()
# capacity = [2,3,4,5] 
# rocks = [1,2,4,4]
# additionalRocks = 3

# print(s.maximumBags(capacity, rocks, additionalRocks))



# ************************** problem 3 *********************************

class Solution(object):
	def minimumLines(self, stockPrices):
		stockPrices.sort(key = lambda x:x[0])

		lastState = None
		currState = None
		ans = 1


		for index in range(len(stockPrices) - 1):
				print(index, lastState, currState, ans)
				if stockPrices[index][1] < stockPrices[index + 1][1]:
					currState = 1
				if stockPrices[index][1] > stockPrices[index + 1][1]:
					currState = 2
				if stockPrices[index][1] == stockPrices[index + 1][1]:
					currState = 3
				if currState != 3 and (stockPrices[index + 1][0] - stockPrices[index][0] > 1):
					ans += 1 
					lastState = currState
					continue
				if not lastState:
					lastState = currState
				if lastState and (lastState != currState):
					lastState = currState
					ans += 1

				lastState = currState
				

		return ans


s = Solution()
stockPrices = [[36,9],[17,93],[34,4],[30,11],[11,41],[53,36],[5,92],[81,92],[28,36],[3,45],[72,33],[64,1],[4,70],[16,73],[99,20],[49,33],[47,74],[83,91]]
print(s.minimumLines(stockPrices))

[[3, 45], [4, 70], [5, 92], [11, 41], [16, 73], [17, 93], [28, 36],
 [30, 11], [34, 4], [36, 9], [47, 74], [49, 33], [53, 36], [64, 1],
  [72, 33], [81, 92], [83, 91], [99, 20]]



1
































