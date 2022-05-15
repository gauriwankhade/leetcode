
#***************** problem 1 ****************************************

# class Solution(object):
# 	def removeAnagrams(self, words):
# 		result = []
# 		start = 0
# 		end = 1
# 		limit = len(words)

# 		while(start < limit > end):
# 			if start == end:
# 				end += 1
# 			if start < limit > end and sorted(words[start]) == sorted(words[end]):
# 				words[end] = ''
# 				end += 1
# 			else:
# 				start += 1

# 		for item in words:
# 			if item:
# 				result.append(item)

# 		return result



# s = Solution()
# words = ["meh","iqfgmpec","qefigmpc","jawtcmf","fdkbqb"]
# print(s.removeAnagrams(words))






#***************** problem 2 ****************************************



# class Solution(object):
# 	def maxConsecutive(self, bottom, top, special):
# 		special = sorted(special)
# 		specStart = special[0]
# 		specEnd = special[-1]

# 		result = max(abs(specStart - bottom), abs(specEnd - top))

# 		for index in range(len(special) - 1):
# 			result = max(special[index + 1] - special[index] - 1, result)


# 		return result



# s = Solution()
# print(s.maxConsecutive(28,  50, [35, 48]))









#****************** problem 4 ******************************************



class CountIntervals(object):
	def __init__(self):
		self.map = {}

	def add(self, left, right):
		if not left:
			return

		for key in range(left, right + 1):
			self.map[key] = True


	def count(self):
		return len(self.map)



# Your CountIntervals object will be instantiated and called as such:
s = CountIntervals()
s.add(2, 3)
print(s.count())
s.add(6, 8)
print(s.count())
s.add(1, 1000000000)
print(s.count())




























        