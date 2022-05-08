
class Solution(object):
	def lengthOfLongestSubstring(self, s):
		Map = {}
		result = 0
		start = 0


		for index in range(len(s)):
			if s[index] in Map and Map[s[index]] >= start:
				start = Map[s[index]] + 1
			else:
				print(result, index - start + 1)
				result = max(result, index - start + 1)
			
			Map[s[index]] = index 


		return result

s = Solution()
string = "aabcdbadaacc"
print(s.lengthOfLongestSubstring(string))


